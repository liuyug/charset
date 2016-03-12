#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct

from .base import CharsetBase


class GBK(CharsetBase):
    title = 'CODE TABLE OF GBK'
    description = [
        u'GBK即汉字内码扩展规范，K为汉语拼音Kuo Zhan（扩展）中“扩”字的声母。英文全称Chinese Internal Code Specification。',
        u'由于GB 2312-80只收录6763个汉字，有不少汉字，如部分在GB 2312-80推出以后才简化的汉字（如“啰”），部分人名用字（如中国前总理朱镕基的“镕”字），台湾及香港使用的繁体字，日语及朝鲜语汉字等，并未有收录在内。于是厂商微软利用GB 2312-80未使用的编码空间，收录GB 13000.1-93全部字符制定了GBK编码。',
        u'GBK自身并非国家标准，只是曾由国家技术监督局标准化司、电子工业部科技与质量监督司公布为“技术规范指导性文件”。',
        u'字符有一字节和双字节编码，00–7F范围内是第一个字节，和ASCII保持一致，此范围内严格上说有96个文字和32个控制符号。',
        u'之后的双字节中，前一字节是双字节的第一位。总体上说第一字节的范围是81–FE（也就是不含80和FF），第二字节的一部分领域在40–7E，其他领域在80–FE。',
    ]
    detail = [
        u'GBK/1 	A1–A9 	A1–FE',
        u'GBK/2 	B0–F7 	A1–FE',
        u'GBK/3 	81–A0 	40–FE (7F除外)',
        u'GBK/4 	AA–FE 	40–A0 (7F除外)',
        u'GBK/5 	A8–A9 	40–A0 (7F除外)',
        u'用户定义 	AA–AF 	A1–FE',
        u'用户定义 	F8–FE 	A1–FE',
        u'用户定义 	A1–A7 	40–A0 (7F除外)',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/GBK'

    encoding = 'gbk'
    define = {
        'panel0': {
            'desc': ['ASCII', 'One Byte'],
            'range': (0x00, 0x00, 0x00, 0x7f),
        },
        'panel1': {
            'desc': ['GB', 'Two Bytes'],
            'range': (0x81, 0xfe, 0x40, 0xfe),
        },
    }
    category = {
        'panel0': [
            {
                'name': 'Control',
                'range': ((0x00, 0x00, 0x00, 0x1f),),
                'desc': 'Control',
            },
            {
                'name': 'Text',
                'range': ((0x00, 0x00, 0x20, 0x7f),),
                'desc': 'Text',
            },
        ],
        'panel1': [
            {
                'name': 'gbk1',
                'range': ((0xa1, 0xa9, 0xa1, 0xfe),),
                'desc': 'GBK 1 (GB2312 Symboal)',
            },
            {
                'name': 'gbk2',
                'range': ((0xb0, 0xf7, 0xa1, 0xfe),),
                'desc': 'GBK 2 (GB2312 Level1, Level2)',
            },
            {
                'name': 'gbk3',
                'range': ((0x81, 0xa0, 0x40, 0x7e), (0x81, 0xa0, 0x80, 0xfe)),
                'desc': 'GBK 3',
            },
            {
                'name': 'gbk4',
                'range': ((0xaa, 0xfe, 0x40, 0x7e), (0xaa, 0xfe, 0x80, 0xa0)),
                'desc': 'GBK 4',
            },
            {
                'name': 'gbk5',
                'range': ((0xa8, 0xa9, 0x40, 0x7e), (0xa8, 0xa9, 0x80, 0xa0)),
                'desc': 'GBK 5',
            },
            {
                'name': 'user1',
                'range': ((0xaa, 0xaf, 0xa1, 0xfe),),
                'desc': 'User 1 (GB2312 User 1)',
            },
            {
                'name': 'user2',
                'range': ((0xf8, 0xfe, 0xa1, 0xfe),),
                'desc': 'User 2 (GB2312 User 2)',
            },
            {
                'name': 'user3',
                'range': ((0xa1, 0xa7, 0x40, 0x7e), (0xa1, 0xa7, 0x80, 0xa0)),
                'desc': 'User 3',
            },
        ],
    }

    def __init__(self, errors=None):
        super(GBK, self).__init__(errors=errors)

    def get_category(self, b_code):
        code, = struct.unpack('>H', b_code)
        f = code >> 8
        s = code & 0xff
        for k, v in self.category.items():
            for vv in v:
                for f1, f2, s1, s2 in vv['range']:
                    if f1 <= f <= f2 and s1 <= s <= s2:
                        return vv['name']
        return None

    def do_panel_as_html(self, define, err_ch):
        x1, x2, y1, y2 = define['range']
        if x1 == x2 == 0x0:
            return self.panel_as_html_1B(define, err_ch)
        else:
            return self.panel_as_html_2B(define, err_ch)
        return []

    def panel_as_html_1B(self, define, err_ch):
        html = []
        x1, x2, y1, y2 = define['range']
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
                name = self.get_category(b'\x00' + b_code)
                if name:
                    row.append('<td class="%s">%s</td>' % (name, ch))
                else:
                    row.append('<td>%s</td>' % ch)
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def panel_as_html_2B(self, define, err_ch):
        html = []
        x1, x2, y1, y2 = define['range']
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
    parser = argparse.ArgumentParser(description='Output GBK code table to HTML.')
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--output-html', action='store_true', help='output html table')
    parser.add_argument('--char', dest='code', help='output character for GBK code')
    parser.add_argument('--code', dest='char', help='output GBK code for character')
    args = parser.parse_args()

    gbk = GBK()
    if args.output_html:
        html = gbk.as_html()
        print(html.encode(args.encoding))
    elif args.char:
        chars = args.char.decode('utf-8')
        print('GBK code:')
        print(gbk.codes(chars))
    elif args.code:
        if '-' in args.code:
            codes = args.code.split('-')
        elif ',' in args.code:
            codes = args.code.split(',')
        else:
            codes = [args.code[x * 4:(x + 1) * 4] for x in range(len(args.code) / 4)]
        print('GBK char:')
        print(''.join(gbk.chars(codes)))
    else:
        parser.print_help()
