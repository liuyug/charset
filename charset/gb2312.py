#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct

from .base import CharsetBase


class GB2312(CharsetBase):
    title = 'CODE TABLE OF GB2312'
    description = [
        u"GB 2312标准共收录6763个汉字，其中一级汉字3755个，二级汉字3008个；同时收录了包括拉丁字母、希腊字母、日文平假名及片假名字母、俄语西里尔字母在内的682个字符。",
    ]
    detail = [
        u'01-09区为特殊符号',
        u'16-55区为一级汉字，按拼音排序',
        u'56-87区为二级汉字，按部首／笔画排序',
        u'10-15区及88-94区则未有编码',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/GB_2312'
    sec_desc = u'区'
    pos_desc = u'位'
    encoding = 'gb2312'
    offset = 0xa0
    define = {
        'panel0': {
            'desc': ['GB2312'],
            'range': (1, 94, 1, 94),
        },
    }
    category = {
        'panel0': [
            {
                'name': 'symbol',
                'range': ((1, 9, 1, 94),),
                'desc': 'Symbol',
            },
            {
                'name': 'user1',
                'range': ((10, 15, 1, 94),),
                'desc': 'User 1',
            },
            {
                'name': 'level1',
                'range': ((16, 55, 1, 94),),
                'desc': 'Level 1',
            },
            {
                'name': 'level2',
                'range': ((56, 87, 1, 94),),
                'desc': 'Level 2',
            },
            {
                'name': 'user2',
                'range': ((88, 94, 1, 94),),
                'desc': 'User 2',
            },
        ],
    }

    def __init__(self, errors=None):
        super(GB2312, self).__init__(errors=errors)

    def get_category(self, b_code):
        code, = struct.unpack('>H', b_code)
        f = (code >> 8 & 0xff) - self.offset
        s = (code & 0xff) - self.offset
        for k, v in self.category.items():
            for vv in v:
                for f1, f2, s1, s2 in vv['range']:
                    if f1 <= f <= f2 and s1 <= s <= s2:
                        return vv['name']
        return None

    def chars(self, codes):
        chars = []
        for code in codes:
            b_code = struct.pack('>2B', int(code[:2]) + 0xa0, int(code[2:]) + 0xa0)
            ch = b_code.decode(self.encoding)
            chars.append(ch)
        return chars

    def codes(self, chars):
        codes = []
        for ch in chars:
            b_code = ch.encode(self.encoding)
            code = ''.join(['%02d' % (x - self.offset) for x in struct.unpack('>2B', b_code)])
            codes.append(code)
        return codes

    def as_txt(self, errors=None):
        err_ch = errors if errors else ''
        lines = []
        lines.append(self.title)
        lines.append('=' * len(self.title))
        lines += self.description
        lines += self.detail
        lines.append(self.wiki)
        lines.append('')
        lines.append(' ' * 6 + ' '.join(['%02X' % (self.offset + x + 1) for x in range(94)]))
        lines.append(' ' * 6 + ' '.join(['%02d' % (x + 1) for x in range(94)]))
        for x in range(94):
            sec = x + 1
            row = []
            row.append('%02X' % (sec + self.offset))
            row.append('%02d' % sec)
            for y in range(94):
                pos = y + 1
                b_code = struct.pack('>2B', sec + self.offset, pos + self.offset)
                ch = b_code.decode(self.encoding, errors='ignore')
                if not ch:
                    ch = err_ch
                row.append(ch)
            lines.append(' '.join(row))
        return '\n'.join(lines)

    def do_panel_as_html(self, define, err_ch):
        html = []
        x1, x2, y1, y2 = define['range']
        html.append('<table>')
        html.append(
            '<tr>' +
            '<td colspan="2" rowspan="2">%s\%s</td>' % (self.sec_desc, self.pos_desc) +
            ''.join(['<td>%02X</td>' % (self.offset + x) for x in range(y1, y2 + 1)]) +
            '</tr>'
        )
        html.append(
            '<tr>' +
            ''.join(['<td>%02d</td>' % x for x in range(y1, y2 + 1)]) +
            '</tr>'
        )
        for sec in range(x1, x2 + 1):
            row = []
            row.append('<td>%02X</td>' % (sec + self.offset))
            row.append('<td>%02d</td>' % sec)
            for pos in range(y1, y2 + 1):
                b_code = struct.pack('>2B', sec + self.offset, pos + self.offset)
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

    def as_rst(self, errors=None):
        err_ch = errors if errors else ''
        lines = []
        lines.append(self.title)
        lines.append('=' * len(self.title))
        lines += ['%s\n' % desc for desc in self.description]
        lines.append('')
        lines += ['* %s' % detail for detail in self.detail]
        lines.append('')
        lines.append('wiki: %s' % self.wiki)
        lines.append('')

        chars = []
        for x in range(1, 95):
            for y in range(1, 95):
                b_code = struct.pack('>2B', x + self.offset, y + self.offset)
                ch = b_code.decode(self.encoding, errors='ignore')
                if not ch:
                    ch = err_ch
                chars.append(ch)
        data = []
        data.append(['', ''] + ['%02X' % (x + 1 + 0xa0) for x in range(94)])
        data.append(['', ''] + ['%02d' % (x + 1) for x in range(94)])
        data += [
            ['%02X' % (x + 1 + 0xa0), '%02d' % (x + 1)] +
            chars[x * 94:(x + 1) * 94] for x in range(94)
        ]
        from rsttable import RstTable
        a = RstTable(data, header=False, encoding=self.encoding)
        lines.append(a.table())
        return '\n'.join(lines)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--output-html', action='store_true', help='output html table')
    parser.add_argument('--output-txt', action='store_true', help='output txt table')
    parser.add_argument('--output-rst', action='store_true', help='output rst table')
    parser.add_argument('--code', dest='char', help='output GB2312 section and position for character')
    parser.add_argument('--char', dest='code', help='output character for GB2312 section and position code')
    args = parser.parse_args()

    gb2312 = GB2312()
    if args.output_txt:
        text = gb2312.as_txt(errors=u'　')
        # output str
        print(text.encode(args.encoding))
    elif args.output_html:
        html = gb2312.as_html()
        print(html.encode(args.encoding))
    elif args.output_rst:
        rst = gb2312.as_rst()
        print(rst.encode(args.encoding))
    elif args.char:
        chars = args.char.decode(args.encoding)
        print('GB2312 section and position:')
        print(gb2312.codes(chars))
    elif args.code:
        if '-' in args.code:
            codes = args.code.split('-')
        elif ',' in args.code:
            codes = args.code.split(',')
        else:
            codes = [args.code[x * 4:(x + 1) * 4] for x in range(len(args.code) / 4)]
        print('GB2312 characters:')
        print(''.join(gb2312.chars(codes)).encode(args.encoding))
    else:
        parser.print_help()
