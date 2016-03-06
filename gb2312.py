#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class GB2312(object):
    title = 'CODE TABLE OF GB2312'
    description = u"GB 2312标准共收录6763个汉字，其中一级汉字3755个，二级汉字3008个；同时收录了包括拉丁字母、希腊字母、日文平假名及片假名字母、俄语西里尔字母在内的682个字符。"
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
        'symbol': (1, 9),
        'user1': (10, 15),
        'level1': (16, 55),
        'level2': (56, 87),
        'user2': (88, 94),
    }
    color = {
        'symbol': '#f79646',
        'level1': '#4bacc6',
        'level2': '#8064a2',
        'user1': '#eeece1',
        'user2': '#ddd9c3',
    }

    def __init__(self, errors=None):
        self.charset = {}
        nSec = 94
        nPos = 94
        for x in range(nSec):
            sec = x + 1
            for y in range(nPos):
                pos = y + 1
                # int
                gb_code = (sec + self.offset) << 8 | (pos + self.offset)
                # bytes
                b_code = struct.pack('>1H', gb_code)
                # unicode
                ch = b_code.decode(self.encoding, errors='ignore')
                if not ch and errors:
                    ch = errors
                self.charset[gb_code] = ch

    def __repr__(self):
        return '<%s>' % self.title

    @classmethod
    def get_area_name(cls, code):
        sec = (code >> 8) - cls.offset
        for k, v in cls.define.items():
            if v[0] <= sec <= v[1]:
                return k

    def sp_search(self, chars):
        """section and postion"""
        inverse_charset = dict(zip(self.charset.values(), self.charset.keys()))
        codes = []
        for ch in chars:
            code = inverse_charset.get(ch)
            sec = (code >> 8) - self.offset
            pos = (code & 0xff) - self.offset
            codes.append('%s%s' % (sec, pos))
        return codes

    def as_txt(self, errors=None):
        err_ch = errors if errors else ''
        lines = []
        lines.append(self.title)
        lines.append('=' * len(self.title))
        lines.append(self.description)
        lines += self.detail
        lines.append(self.wiki)
        lines.append('')
        lines.append(' ' * 6 + ' '.join(['%02X' % (0xa0 + x + 1) for x in range(94)]))
        lines.append(' ' * 6 + ' '.join(['%02d' % (x + 1) for x in range(94)]))
        for x in range(94):
            sec = x + 1
            row = []
            row.append('%02X' % (sec + self.offset))
            row.append('%02d' % sec)
            for y in range(94):
                pos = y + 1
                code = (sec + self.offset) << 8 | (pos + self.offset)
                row.append('%s' % (self.charset.get(code, err_ch)))
            lines.append(' '.join(row))
        return '\n'.join(lines)

    def as_html(self, errors=None):
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
        html.append('.symbol {background-color:%s;}' % self.color['symbol'])
        html.append('.level1 {background-color:%s;}' % self.color['level1'])
        html.append('.level2 {background-color:%s;}' % self.color['level2'])
        html.append('.user1 {background-color:%s;}' % self.color['user1'])
        html.append('.user2 {background-color:%s;}' % self.color['user2'])
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
        html.append('<p>wiki: <a href="%s" target="_blank">%s</a></p>' % (self.wiki, self.wiki))
        html.append('<h2>Code Table</h2>')
        html.append('<p>')
        html.append('<span class="symbol">Symbol</span>')
        html.append('<span class="level1">Level 1</span>')
        html.append('<span class="level2">Level 2</span>')
        html.append('<span class="user1">User 1</span>')
        html.append('<span class="user2">User 2</span>')
        html.append('</p>')
        html.append('<table>')
        html.append(
            '<tr>' +
            '<td colspan="2" rowspan="2">%s\%s</td>' % (self.sec_desc, self.pos_desc) +
            ''.join(['<td>%02X</td>' % (self.offset + x + 1) for x in range(94)]) +
            '</tr>'
        )
        html.append(
            '<tr>' +
            ''.join(['<td>%02d</td>' % (x + 1) for x in range(94)]) +
            '</tr>'
        )
        for sec in range(1, 94 + 1):
            row = []
            row.append('<td>%02X</td>' % (sec + self.offset))
            row.append('<td>%02d</td>' % sec)
            for pos in range(1, 94 + 1):
                code = (sec + self.offset) << 8 | (pos + self.offset)
                name = self.get_area_name(code)
                row.append('<td class="%s">%s</td>' % (name, self.charset.get(code, err_ch)))
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)

    def as_rst(self, errors=None):
        lines = []
        lines.append(self.title)
        lines.append('=' * len(self.title))
        lines.append(self.description)
        lines.append('')
        lines += ['* %s' % detail for detail in self.detail]
        lines.append('')
        lines.append('wiki: %s' % self.wiki)
        lines.append('')

        charset_list = self.charset.values()
        data = []
        data.append(['', ''] + ['%02X' % (x + 1 + 0xa0) for x in range(94)])
        data.append(['', ''] + ['%02d' % (x + 1) for x in range(94)])
        data += [
            ['%02X' % (x + 1 + 0xa0), '%02d' % (x + 1)] +
            charset_list[x * 94:(x + 1) * 94] for x in range(94)
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
    parser.add_argument('--sp', help='output section and position for gb2312 character')
    args = parser.parse_args()

    gb2312 = GB2312()
    if args.output_txt:
        text = gb2312.as_txt(errors=u'　')
        # output str
        print(text.encode(args.encoding))
    if args.output_html:
        html = gb2312.as_html()
        print(html.encode(args.encoding))
    if args.output_rst:
        rst = gb2312.as_rst()
        print(rst.encode(args.encoding))
    if args.sp:
        chars = args.sp.decode(args.encoding)
        print('GB2312 section and position:')
        print(gb2312.sp_search(chars))
