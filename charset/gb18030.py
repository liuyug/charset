#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct

from .base import CharsetBase


class GB18030(CharsetBase):
    title = 'CODE TABLE OF GB18030'
    description = [
        u'GB 18030，全称：国家标准GB 18030-2005《信息技术　中文编码字符集》，是中华人民共和国现时最新的内码字集，是GB 18030-2000《信息技术　信息交换用汉字编码字符集　基本集的扩充》的修订版。与GB 2312-1980完全兼容，与GBK基本兼容，支持GB 13000及Unicode的全部统一汉字，共收录汉字70,244个。',
        u'此标准内的单字节编码部分、双字节编码部分，和四字节编码部分收录的中日韩统一表意文字扩展A区汉字，为强制性标准。其他部分则属于规模性标准。',
        u'GB18030有两个版本：GB18030-2000和GB18030-2005。GB18030-2000是GBK的取代版本，它的主要特点是在GBK基础上增加了CJK统一汉字扩充A的汉字。GB18030-2005的主要特点是在GB18030-2000基础上增加了CJK统一汉字扩充B的汉字。',
    ]
    detail = [
        u'单字节，其值从0x00到0x7F。',
        u'双字节，第一个字节的值从0x81到0xFE，第二个字节的值从0x40到0xFE（不包括0x7F）。',
        u'四字节，第一个字节的值从0x81到0xFE，第二个字节的值从0x30到0x39，第三个字节从0x81到0xFE，第四个字节从0x30到0x39。',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/GB_18030'

    encoding = 'gb18030'
    define = {
        'panel0': {
            'desc': ['ASCII', 'One Bytes'],
            'range': (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7f),
        },
        'panel1': {
            'desc': ['Two Bytes'],
            'range': (0x00, 0x00, 0x00, 0x00, 0x81, 0xfe, 0x40, 0xfe),
        },
        'panel2': {
            'desc': ['Four Bytes'],
            'range': (0x81, 0xfe, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),
        }
    }
    category = {
        'panel0': [
            {
                'name': 'Control',
                'range': ((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1f),),
                'desc': 'Control',
            },
            {
                'name': 'ascii',
                'range': ((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x7f),),
                'desc': 'ASCII',
            },
        ],
        'panel1': [
            {
                'name': 'gbk',
                'range': (
                    (0x00, 0x00, 0x00, 0x00, 0x81, 0xfe, 0x40, 0x7e),
                    (0x00, 0x00, 0x00, 0x00, 0x81, 0xfe, 0x80, 0xfe),
                ),
                'desc': 'GBK',
            },
        ],
        'panel2': [
            {
                'name': 'cjk_a',
                'range': ((0x81, 0x82, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),),
                'desc': 'CJK A',
            },
            {
                'name': 'cjk_b',
                'range': ((0x95, 0x98, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),),
                'desc': 'CJK A',
            },
        ],
    }

    def __init__(self, errors=None):
        super(GB18030, self).__init__(errors=errors)

    def get_category(self, b_code):
        code, = struct.unpack('>L', b_code)
        f = code >> 24 & 0xff
        s = code >> 16 & 0xff
        t = code >> 8 & 0xff
        fo = code & 0xff
        for k, v in self.category.items():
            for vv in v:
                for f1, f2, s1, s2, t1, t2, fo1, fo2 in vv['range']:
                    if f1 <= f <= f2 and s1 <= s <= s2 and t1 <= t <= t2 and fo1 <= fo <= fo2:
                        return vv['name']
        return None

    def do_panel_as_html(self, define, err_ch):
        f1, f2, s1, s2, t1, t2, fo1, fo2 = define['range']
        if f1 == f2 == s1 == s2 == t1 == t2 == 0x0:
            return self.panel_as_html_1B(define, err_ch)
        elif f1 == f2 == s1 == s2 == 0x0:
            return self.panel_as_html_2B(define, err_ch)
        else:
            return self.panel_as_html_4B_3D(define, err_ch)
        return []

    def panel_as_html_1B(self, define, err_ch):
        html = []
        m1, m2, n1, n2, x1, x2, y1, y2 = define['range']
        x1, x2 = (y1 >> 4 & 0xf, y2 >> 4 & 0xf)
        y1, y2 = (y1 & 0xf, y2 & 0xf)
        html.append('<table>')
        html.append(
            '<tr>' +
            '<td></td>' +
            ''.join(['<td>%02X</td>' % y for y in range(y1, y2 + 1)]) +
            '</tr>'
        )
        for x in range(x1, x2 + 1):
            row = []
            row.append('<td>%02X</td>' % x)
            for y in range(y1, y2 + 1):
                b_code = struct.pack('>B', x << 4 | y)
                ch = b_code.decode(self.encoding, errors='ignore')
                if not ch:
                    ch = err_ch
                name = self.get_category(b'\x00\x00\x00' + b_code)
                if name:
                    row.append('<td class="%s">%s</td>' % (name, ch))
                else:
                    row.append('<td>%s</td>' % ch)
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def panel_as_html_2B(self, define, err_ch):
        # two
        html = []
        m1, m2, n1, n2, x1, x2, y1, y2 = define['range']
        html.append('<table>')
        html.append(
            '<tr>' +
            '<td></td>' +
            ''.join(['<td>%02X</td>' % y for y in range(y1, y2 + 1)]) +
            '</tr>'
        )
        for x in range(x1, x2 + 1):
            row = []
            row.append('<td>%02X</td>' % x)
            for y in range(y1, y2 + 1):
                b_code = struct.pack('>2B', x, y)
                ch = b_code.decode(self.encoding, errors='ignore')
                if not ch:
                    ch = err_ch
                name = self.get_category(b'\x00\x00' + b_code)
                if name:
                    row.append('<td class="%s">%s</td>' % (name, ch))
                else:
                    row.append('<td>%s</td>' % ch)
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def panel_as_html_4B_2D(self, define, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = define['range']
        html.append('<table>')
        cols = []
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                cols.append('<td>%02X%02X</td>' % (y, z))
        html.append('<tr>' + '<td></td>' + ''.join(cols) + '</tr>')
        for a in range(a1, a2 + 1):
            for x in range(x1, x2 + 1):
                row = []
                row.append('<td>%02X%02X</td>' % (a, x))
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        b_code = struct.pack('>4B', a, x, y, z)
                        ch = b_code.decode(self.encoding, errors='ignore')
                        if not ch:
                            ch = err_ch
                        name = self.get_category(b_code)
                        if name:
                            row.append('<td class="%s">%s</td>' % (name, ch))
                        else:
                            row.append('<td>%s</td>' % ch)
                html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def panel_as_html_4B_3D(self, define, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = define['range']
        for a in range(a1, a2 + 1):
            html.append('<h4>%02X table</h4>' % a)
            html.append('<table>')
            cols = []
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    cols.append('<td>%02X%02X</td>' % (y, z))
            html.append(
                '<tr>' +
                '<td></td>' +
                ''.join(cols) +
                '</tr>'
            )
            for x in range(x1, x2 + 1):
                row = []
                row.append('<td>%02X</td>' % x)
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        b_code = struct.pack('>4B', a, x, y, z)
                        ch = b_code.decode(self.encoding, errors='ignore')
                        if not ch:
                            ch = err_ch
                        name = self.get_category(b_code)
                        if name:
                            row.append('<td class="%s">%s</td>' % (name, ch))
                        else:
                            row.append('<td>%s</td>' % ch)
                html.append('<tr>' + ''.join(row) + '</tr>')
            html.append('</table>')
        return html

    def panel_as_html_4B_4D(self, define, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = define['range']
        for a in range(a1, a2 + 1):
            for x in range(x1, x2 + 1):
                html.append('<h4>%02X %02X table</h4>' % (a, x))
                html.append('<table>')
                html.append(
                    '<tr>' +
                    '<td></td>' +
                    ''.join(['<td>%02X</td>' % z for z in range(z1, z2 + 1)]) +
                    '</tr>'
                )
                for y in range(y1, y2 + 1):
                    row = []
                    row.append('<td>%02X</td>' % y)
                    for z in range(z1, z2 + 1):
                        b_code = struct.pack('>4B', a, x, y, z)
                        ch = b_code.decode(self.encoding, errors='ignore')
                        if not ch:
                            ch = err_ch
                        name = self.get_category(b_code)
                        if name:
                            row.append('<td class="%s">%s</td>' % (name, ch))
                        else:
                            row.append('<td>%s</td>' % ch)
                    html.append('<tr>' + ''.join(row) + '</tr>')
                html.append('</table>')
        return html


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Output GB18030 code table to HTML.')
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--panel', help='UTF-8 encoding panel: 1, 2, 3')
    parser.add_argument('--char', dest='code', help='output character for GB18030 code')
    parser.add_argument('--code', dest='char', help='output GB18030 code for character')
    args = parser.parse_args()

    gb18030 = GB18030()
    if args.panel:
        html = gb18030.as_html(panel=args.panel)
        print(html.encode(args.encoding))
    elif args.char:
        chars = args.char.decode('utf-8')
        print('GB18030 code:')
        print(gb18030.codes(chars))
    elif args.code:
        if '-' in args.code:
            codes = args.code.split('-')
        elif ',' in args.code:
            codes = args.code.split(',')
        else:
            codes = [args.code[x * 4:(x + 1) * 4] for x in range(len(args.code) / 4)]
        print('GB18030 char:')
        print(''.join(gb18030.chars(codes)))
    else:
        parser.print_help()
