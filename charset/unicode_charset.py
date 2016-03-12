#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct

from .base import CharsetBase
from . import unicode_category


class Unicode(CharsetBase):
    title = 'CODE TABLE OF Unicode'
    description = [
        u'Unicode（中文：万国码、国际码、统一码、单一码）是计算机科学领域里的一项业界标准。它对世界上大部分的文字系统进行了整理、编码，使得电脑可以用更为简单的方式来呈现和处理文字。',
        u'统一码版本对应于UCS-2，使用16位的编码空间。也就是每个字符占用2个字节。这样理论上一共最多可以表示2 ** 16（即65536）个字符。基本满足各种语言的使用。16位统一码字符构成基本多文种平面。',
        u'最新（但未实际广泛使用）的统一码版本定义了16个辅助平面，两者合起来至少需要占据21位的编码空间，比3字节略少。但事实上辅助平面字符仍然占用4字节编码空间，与UCS-4保持一致。未来版本会扩充到ISO 10646-1实现级别3，即涵盖UCS-4的所有字符。UCS-4是一个更大的尚未填充完全的31位字符集，加上恒为0的首位，共需占据32位，即4字节。理论上最多能表示2 ** 31个字符，完全可以涵盖一切语言所用的符号。',
        u'在表示一個Unicode的字元時，通常會用「U+」然後緊接着一組十六進位的数字來表示這一個字元。',
    ]
    detail = [
        u'基本多文种平面的字符的编码为U+hhhh，其中每个h代表一个十六进制数字，与UCS-2编码完全相同。而其对应的4字节UCS-4编码后两个字节一致，前两个字节则所有位均为0。',
        u'目前的Unicode字元分為17組編排，每組稱為平面（Plane），而每平面擁有65536（即2 ** 16）個代碼點。然而目前只用了少數平面。',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/Unicode'

    encoding = 'utf-32-be'
    define = {
        'panel0': {
            'desc': [u'基本多文種平面', 'Basic Multilingual Plane (BMP)'],
            'range': (0x0000, 0xffff),
        },
        'panel1': {
            'desc': [u'多文種補充平面', 'Supplementary Multilingual Plane (SMP)'],
            'range': (0x10000, 0x1ffff),
        },
        'panel2': {
            'desc': [u'表意文字補充平面', 'Supplementary Ideographic Plane (SIP)'],
            'range': (0x20000, 0x2ffff),
        },
        'panel3': {
            'desc': [u'表意文字第三平面', 'Tertiary Ideographic Plane (TIP)'],
            'range': (0x30000, 0x3ffff),
        },
        'panel14': {
            'desc': [u'特別用途補充平', 'Supplementary Special-purpose Plane (SSP)'],
            'range': (0xe0000, 0xeffff),
        },
        'panel15': {
            'desc': [u'保留作為私人使用區（A區）', 'Private Use range-A (PUA-A)'],
            'range': (0xf0000, 0xfffff),
        },
        'panel16': {
            'desc': [u'保留作為私人使用區（B區）', 'Private Use range-B (PUA-B)'],
            'range': (0x100000, 0x10ffff),
        },
    }

    def __init__(self, errors=None):
        super(Unicode, self).__init__(errors=errors)
        for p in unicode_category.panels:
            category = []
            for c in getattr(unicode_category, 'panel%s' % p):
                category.append({
                    'name': c[2],
                    'range': c[0],
                    'desc': c[1],
                })
            self.category['panel%s' % p] = category

    def codes(self, chars):
        codes = super(Unicode, self).codes(chars)
        return ['U+' + code for code in codes]

    def get_category(self, b_code):
        code, = struct.unpack('>L', b_code)
        panel = code >> 16 & 0xff
        category = self.category.get('panel%s' % panel)
        if category:
            for c in category:
                if c['range'][0] <= code <= c['range'][1]:
                    return c['name']
        return None

    def do_panel_as_html(self, define, err_ch):
        html = []
        m, n = define['range']
        panel = m >> 16 & 0xff
        x1 = m >> 8 & 0xff
        x2 = n >> 8 & 0xff
        y1 = m & 0xff
        y2 = n & 0xff
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
                b_code = struct.pack('>4B', 0, int(panel), x, y)
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
    parser = argparse.ArgumentParser(description='Output Unicode code table to HTML.')
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--panel', help='Unicode panel')
    parser.add_argument('--char', dest='code', help='output character for Unicode code')
    parser.add_argument('--code', dest='char', help='output Unicode code for character')
    args = parser.parse_args()

    charset = Unicode()
    if args.panel:
        html = charset.as_html(panels=args.panel.split(','))
        print(html.encode(args.encoding))
    elif args.char:
        chars = args.char.decode('utf-8')
        print('Unicode code:')
        print(charset.codes(chars))
    elif args.code:
        if '-' in args.code:
            codes = args.code.split('-')
        elif ',' in args.code:
            codes = args.code.split(',')
        else:
            codes = [args.code]
        print('Unicode char:')
        print(''.join(charset.chars(codes)))
    else:
        parser.print_help()
