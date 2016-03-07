#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class UTF8(object):
    title = 'CODE TABLE OF UTF-8'
    description = u"UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，也是一种前缀码。它可以用来表示Unicode标准中的任何字符，且其编码中的第一个字节仍与ASCII兼容，这使得原来处理ASCII字符的软件无须或只须做少部分修改，即可继续使用。因此，它逐渐成为电子邮件、网页及其他存储或发送文字的应用中，优先采用的编码。"
    detail = [
        u'UTF-8使用一至六个字节为每个字符编码（尽管如此，2003年11月UTF-8被RFC 3629重新规范，只能使用原来Unicode定义的区域，U+0000到U+10FFFF，也就是说最多四个字节）',
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
        'one': (0x00, 0x7f),
        'two': (0xc0, 0xdf, 0x80, 0xbf),
        'three': (0xe0, 0xef, 0x80, 0xbf, 0x80, 0xbf),
        'four': (0xf0, 0xf7, 0x80, 0xbf, 0x80, 0xbf, 0x80, 0xbf),
    }

    def __init__(self, errors=None):
        pass

    def __repr__(self):
        return '<%s>' % self.title

    def codes(self, chars):
        """section and postion"""
        codes = []
        for ch in chars:
            ch = ch.encode(self.encoding)
            codes.append(ch)
        return codes

    def as_html(self, zone=None, errors=None):
        if zone is None:
            zone = ['two', 'three', 'four']
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
        if 'two' in zone:
            html.append('<h3>Two Bytes Table</h3>')
            html += self.as_html_2B(err_ch)
        if 'three' in zone:
            html.append('<h3>Three Bytes Table</h3>')
            html += self.as_html_3B(err_ch)
        if 'four' in zone:
            html.append('<h3>Four Bytes Table</h3>')
            html += self.as_html_4B(err_ch)
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)

    def as_html_2B(self, err_ch):
        # two
        html = []
        x1, x2, y1, y2 = self.define['two']
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
                row.append('<td>%s</td>' % ch)
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html

    def as_html_3B(self, err_ch):
        # three
        html = []
        x1, x2, y1, y2, z1, z2 = self.define['three']
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
                    row.append('<td>%s</td>' % ch)
                html.append('<tr>' + ''.join(row) + '</tr>')
            html.append('</table>')
        return html

    def as_html_4B(self, err_ch):
        # four
        html = []
        a1, a2, x1, x2, y1, y2, z1, z2 = self.define['four']
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
                        row.append('<td>%s</td>' % ch)
                    html.append('<tr>' + ''.join(row) + '</tr>')
                html.append('</table>')
        return html


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Output UTF-8 code table to HTML.')
    parser.add_argument('--zone', help='UTF-8 encoding zone: two, three, four')
    parser.add_argument('--code', help='code for UTF-8 character')
    args = parser.parse_args()

    utf8 = UTF8()
    if args.code:
        chars = args.code.decode('utf-8')
        print('UTF-8 code:')
        print(utf8.codes(chars))
    elif args.zone:
        html = utf8.as_html(zone=args.zone)
        print(html.encode('utf-8'))
    else:
        parser.print_help()
