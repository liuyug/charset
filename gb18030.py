#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class GB18030(object):
    title = 'CODE TABLE OF GB18030'
    description = u"GB 18030，全称：国家标准GB 18030-2005《信息技术　中文编码字符集》，是中华人民共和国现时最新的内码字集，是GB 18030-2000《信息技术　信息交换用汉字编码字符集　基本集的扩充》的修订版。与GB 2312-1980完全兼容，与GBK基本兼容，支持GB 13000及Unicode的全部统一汉字，共收录汉字70,244个。此标准内的单字节编码部分、双字节编码部分，和四字节编码部分收录的中日韩统一表意文字扩展A区汉字，为强制性标准。其他部分则属于规模性标准。 GB18030有两个版本：GB18030-2000和GB18030-2005。GB18030-2000是GBK的取代版本，它的主要特点是在GBK基础上增加了CJK统一汉字扩充A的汉字。GB18030-2005的主要特点是在GB18030-2000基础上增加了CJK统一汉字扩充B的汉字。"
    detail = [
        u'单字节，其值从0x00到0x7F。',
        u'双字节，第一个字节的值从0x81到0xFE，第二个字节的值从0x40到0xFE（不包括0x7F）。',
        u'四字节，第一个字节的值从0x81到0xFE，第二个字节的值从0x30到0x39，第三个字节从0x81到0xFE，第四个字节从0x30到0x39。',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/GB_18030'

    encoding = 'gb18030'
    define = {
        'two1': (0x81, 0xfe, 0x40, 0x7e),
        'two2': (0x81, 0xfe, 0x80, 0xfe),
        'cjk_a': (0x81, 0x82, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),
        'four1': (0x83, 0x94, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),
        'cjk_b': (0x95, 0x98, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),
        'four2': (0x99, 0xfe, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39),
    }
    color = {
        'cjk_a': '#f79646',
        'cjk_b': '#4bacc6',
    }

    def __init__(self, errors=None):
        pass

    def __repr__(self):
        return '<%s>' % self.title

    @classmethod
    def get_area_name(cls, code):
        if len(code) == 2:
            return ''
        elif len(code) == 4:
            if 0x81 <= code[0] <= 0x82:
                return 'cjk_a'
            elif 0x95 <= code[0] <= 0x98:
                return 'cjk_b'
        return None

    def chars(self, codes):
        chars = []
        for code in codes:
            b_code = struct.pack('>L', int(code, 16))
            ch = b_code.decode(self.encoding)
            chars.append(ch)
        return chars

    def codes(self, chars):
        codes = []
        for ch in chars:
            print(ch)
            b_code = ch.encode(self.encoding)
            fmt = '>%sB' % len(b_code)
            code = ''.join(['%02X' % x for x in struct.unpack(fmt, b_code)])
            codes.append(code)
        return codes

    def as_html(self, zone=None, errors=None):
        if zone is None:
            zone = ['two', 'four']
        err_ch = errors if errors else ''
        html = []
        html.append('<!DOCTYPE html>')
        html.append('<html>')
        html.append('<head>')
        html.append('<meta charset="UTF-8" />')
        html.append('<title>%s</title>' % self.title)
        html.append('<style type="text/css">')
        html.append('table {border-collapse:collapse;border-spacing:0;}')
        html.append('td {border:1px solid green;padding:0.3em;text-align:center;}')
        html.append('hr {border:width:75%;}')
        html.append('.cjk_a {background-color:%s;}' % self.color['cjk_a'])
        html.append('.cjk_b {background-color:%s;}' % self.color['cjk_b'])
        html.append('</style>')
        html.append('</head>')
        html.append('<body>')
        html.append('<h1>%s</h1>' % self.title)
        html.append('<p>Made by Yugang LIU</p>')
        html.append('<hr />')
        html.append('<h2>Description</h2>')
        html.append('<p>%s</p>' % self.description)
        html.append('<ul>')
        html += ['<li>%s</li>' % item for item in self.detail]
        html.append('</ul>')
        html.append('<h2>Reference</h2>')
        html.append('<ul>')
        html.append('<li>wiki: <a href="%s" target="_blank">%s</a></li>' % (self.wiki, self.wiki))
        html.append('</ul>')
        html.append('<h2>Code Table</h2>')
        html.append('<p>')
        html.append('<span class="cjk_a">CJK A</span>')
        html.append('<span class="cjk_b">CJK B</span>')
        html.append('</p>')
        if 'two' in zone:
            html.append('<h3>Two Bytes Table</h3>')
            html += self.as_html_2B(err_ch)
        if 'four' in zone:
            html.append('<h3>Four Bytes Table</h3>')
            html += self.as_html_4B_2(err_ch)
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)

    def as_html_2B(self, err_ch):
        # two
        html = []
        x1, x2, y1, y2 = (0x81, 0xfe, 0x40, 0xfe)
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
                if y == 0x7f:
                    ch = ''
                else:
                    b_code = struct.pack('>2B', x, y)
                    ch = b_code.decode(self.encoding, errors='ignore')
                    if not ch:
                        ch = err_ch
                row.append('<td>%s</td>' % ch)
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def as_html_4B_2(self, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = (0x81, 0xfe, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39)
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
                        name = self.get_area_name((a, x, y, z))
                        if name:
                            row.append('<td class="%s">%s</td>' % (name, ch))
                        else:
                            row.append('<td>%s</td>' % ch)
                html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def as_html_4B_3(self, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = (0x81, 0xfe, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39)
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
                        name = self.get_area_name((a, x, y, z))
                        if name:
                            row.append('<td class="%s">%s</td>' % (name, ch))
                        else:
                            row.append('<td>%s</td>' % ch)
                html.append('<tr>' + ''.join(row) + '</tr>')
            html.append('</table>')
        return html

    def as_html_4B_4(self, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = (0x81, 0xfe, 0x30, 0x39, 0x81, 0xfe, 0x30, 0x39)
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
                        name = self.get_area_name((a, x, y, z))
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
    parser.add_argument('--zone', help='UTF-8 encoding zone: two, four')
    parser.add_argument('--char', dest='code', help='output character for GB18030 code')
    parser.add_argument('--code', dest='char', help='output GB18030 code for character')
    args = parser.parse_args()

    gb18030 = GB18030()
    if args.zone:
        html = gb18030.as_html(zone=args.zone)
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
