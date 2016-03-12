#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct

from .base import CharsetBase


class UTF8(CharsetBase):
    title = 'CODE TABLE OF UTF-8'
    description = [
        u"UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，也是一种前缀码。它可以用来表示Unicode标准中的任何字符，且其编码中的第一个字节仍与ASCII兼容，这使得原来处理ASCII字符的软件无须或只须做少部分修改，即可继续使用。因此，它逐渐成为电子邮件、网页及其他存储或发送文字的应用中，优先采用的编码。",
        u'UTF-8使用一至六个字节为每个字符编码（尽管如此，2003年11月UTF-8被RFC 3629重新规范，只能使用原来Unicode定义的区域，U+0000到U+10FFFF，也就是说最多四个字节）',
    ]
    detail = [
        u'128个US-ASCII字符只需一个字节编码（Unicode范围由U+0000至U+007F）。ASCII字符范围，字节由零开始，0zzzzzzz（00-7F）',
        u'带有附加符号的拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文及它拿字母则需要两个字节编码（Unicode范围由U+0080至U+07FF）。第一个字节由110开始，接着的字节由10开始，110yyyyy（C0-DF) 10zzzzzz(80-BF）',
        u'其他基本多文种平面（BMP）中的字符（这包含了大部分常用字，如大部分的汉字）使用三个字节编码（Unicode范围由U+0800至U+FFFF）。第一个字节由1110开始，接着的字节由10开始，1110xxxx(E0-EF) 10yyyyyy 10zzzzzz',
        u'其他极少使用的Unicode 辅助平面的字符使用四至六字节编码（Unicode范围由U+10000至U+1FFFFF使用四字节，Unicode范围由U+200000至U+3FFFFFF使用五字节，Unicode范围由U+4000000至U+7FFFFFFF使用六字节）。将由11110开始，接着的字节由10开始，11110www(F0-F7) 10xxxxxx 10yyyyyy 10zzzzzz',
        u'对上述提及的第四种字符而言，UTF-8使用四至六个字节来编码似乎太耗费资源了。但UTF-8对所有常用的字符都可以用三个字节表示，而且它的另一种选择，UTF-16编码，对前述的第四种字符同样需要四个字节来编码，所以要决定UTF-8或UTF-16哪种编码比较有效率，还要视所使用的字符的分布范围而定。',
        u'对于UTF-8编码中的任意字节B，如果B的第一位为0，则B独立的表示一个字符(ASCII码)；',
        u'如果B的第一位为1，第二位为0，则B为一个多字节字符中的一个字节(非ASCII字符)；',
        u'如果B的前两位为1，第三位为0，则B为两个字节表示的字符中的第一个字节；',
        u'如果B的前三位为1，第四位为0，则B为三个字节表示的字符中的第一个字节；',
        u'如果B的前四位为1，第五位为0，则B为四个字节表示的字符中的第一个字节；',
        u'因此，对UTF-8编码中的任意字节，根据第一位，可判断是否为ASCII字符；根据前二位，可判断该字节是否为一个字符编码的第一个字节；根据前四位（如果前两位均为1），可确定该字节为字符编码的第一个字节，并且可判断对应的字符由几个字节表示；根据前五位（如果前四位为1），可判断编码是否有错误或数据传输过程中是否有错误。',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/UTF-8'

    encoding = 'utf-8'
    define = {
        'panel0': {
            'desc': ['One Bytes'],
            'range': (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7f),
        },
        'panel1': {
            'desc': ['Two Bytes'],
            'range': (0x00, 0x00, 0x00, 0x00, 0xc0, 0xdf, 0x80, 0xbf),
        },
        'panel2': {
            'desc': ['Three Bytes'],
            'range': (0x00, 0x00, 0xe0, 0xef, 0x80, 0xbf, 0x80, 0xbf),
        },
        'panel3': {
            'desc': ['Four Bytes'],
            'range': (0xf0, 0xf7, 0x80, 0xbf, 0x80, 0xbf, 0x80, 0xbf),
        },
    }
    category = {
        'panel0': [
            {
                'name': 'Control',
                'range': ((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1f),),
                'desc': 'Control',
            },
            {
                'name': 'Text',
                'range': ((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x7f),),
                'desc': 'Text',
            },
        ],
    }

    def __init__(self, errors=None):
        super(UTF8, self).__init__(errors=errors)

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
        elif f1 == f2 == 0x0:
            return self.panel_as_html_3B(define, err_ch)
        else:
            return self.panel_as_html_4B(define, err_ch)
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

    def panel_as_html_3B(self, define, err_ch):
        html = []
        m1, m2, x1, x2, y1, y2, z1, z2 = define['range']
        for x in range(x1, x2 + 1):
            html.append('<h4>%02X table</h4>' % x)
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
                    b_code = struct.pack('>3B', x, y, z)
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

    def panel_as_html_4B(self, define, err_ch):
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
    parser = argparse.ArgumentParser(description='Output UTF-8 code table to HTML.')
    parser.add_argument('--panel', help='UTF-8 encoding panel: 1, 2, 3, 4')
    parser.add_argument('--code', dest='char', help='output UTF-8 code for character')
    parser.add_argument('--char', dest='code', help='output character for UTF-8 code')
    args = parser.parse_args()

    utf8 = UTF8()
    if args.char:
        chars = args.char.decode('utf-8')
        code = utf8.codes(chars)
        print('UTF-8 code:')
        print(code)
    elif args.code:
        if '-' in args.code:
            codes = args.code.split('-')
        elif ',' in args.code:
            codes = args.code.split(',')
        print(''.join(utf8.chars(codes)))
    elif args.zone:
        html = utf8.as_html(panel=args.panel)
        print(html.encode('utf-8'))
    else:
        parser.print_help()
