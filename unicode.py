#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class Unicode(object):
    title = 'CODE TABLE OF Unicode'
    description = u"Unicode（中文：万国码、国际码、统一码、单一码）是计算机科学领域里的一项业界标准。它对世界上大部分的文字系统进行了整理、编码，使得电脑可以用更为简单的方式来呈现和处理文字。统一码版本对应于UCS-2，使用16位的编码空间。也就是每个字符占用2个字节。这样理论上一共最多可以表示216（即65536）个字符。基本满足各种语言的使用。16位统一码字符构成基本多文种平面。最新（但未实际广泛使用）的统一码版本定义了16个辅助平面，两者合起来至少需要占据21位的编码空间，比3字节略少。但事实上辅助平面字符仍然占用4字节编码空间，与UCS-4保持一致。未来版本会扩充到ISO 10646-1实现级别3，即涵盖UCS-4的所有字符。UCS-4是一个更大的尚未填充完全的31位字符集，加上恒为0的首位，共需占据32位，即4字节。理论上最多能表示231个字符，完全可以涵盖一切语言所用的符号。"
    detail = [
        u'基本多文种平面的字符的编码为U+hhhh，其中每个h代表一个十六进制数字，与UCS-2编码完全相同。而其对应的4字节UCS-4编码后两个字节一致，前两个字节则所有位均为0。',
        u'目前的Unicode字元分為17組編排，每組稱為平面（Plane），而每平面擁有65536（即216）個代碼點。然而目前只用了少數平面。',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/Unicode'

    encoding = 'utf-32-be'
    define = {
        'panel0': (0x00000, 0x0ffff),
        'panel1': (0x10000, 0x1ffff),
        'panel2': (0x20000, 0x2ffff),
        'panel3': (0x30000, 0x3ffff),
        'panel14': (0xd0000, 0xdffff),
        'panel15': (0xe0000, 0xeffff),
        'panel16': (0xf0000, 0xfffff),
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
            b_code = ch.encode(self.encoding)
            fmt = '>%sB' % len(b_code)
            code = ''.join(['%02X' % x for x in struct.unpack(fmt, b_code)])
            codes.append('U+' + code.strip('0'))
        return codes

    def as_html(self, panel=None, errors=None):
        if panel is None:
            panel = ['0']
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
        for p in panel:
            html.append('<h3>Panel %s Table</h3>' % p)
            html += self.as_html_2B(int(panel), err_ch)
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)

    def as_html_2B(self, panel, err_ch):
        # two
        html = []
        x1, x2, y1, y2 = (0x00, 0xff, 0x00, 0xff)
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
                b_code = struct.pack('>4B', 0, panel, x, y)
                ch = b_code.decode(self.encoding, errors='ignore')
                if not ch:
                    ch = err_ch
                row.append('<td>%s</td>' % ch)
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        return html


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Output Unicode code table to HTML.')
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--panel', help='Unicode panel')
    parser.add_argument('--char', dest='code', help='output character for Unicode code')
    parser.add_argument('--code', dest='char', help='output Unicode code for character')
    args = parser.parse_args()

    unicodee = Unicode()
    if args.panel:
        html = unicodee.as_html(panel=args.panel)
        print(html.encode(args.encoding))
    elif args.char:
        chars = args.char.decode('utf-8')
        print('Unicode code:')
        print(unicodee.codes(chars))
    elif args.code:
        if '-' in args.code:
            codes = args.code.split('-')
        elif ',' in args.code:
            codes = args.code.split(',')
        else:
            codes = [args.code[x * 4:(x + 1) * 4] for x in range(len(args.code) / 4)]
        print('Unicode char:')
        print(''.join(unicodee.chars(codes)))
    else:
        parser.print_help()
