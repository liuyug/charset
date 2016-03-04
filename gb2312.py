#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class GB2312(object):
    title = 'CODE TABLE OF GB2312-80'
    description = u"GB 2312标准共收录6763个汉字，其中一级汉字3755个，二级汉字3008个；同时收录了包括拉丁字母、希腊字母、日文平假名及片假名字母、俄语西里尔字母在内的682个字符。"
    detail = [
        u'01-09区为特殊符号',
        u'16-55区为一级汉字，按拼音排序',
        u'56-87区为二级汉字，按部首／笔画排序',
        u'10-15区及88-94区则未有编码',
    ]
    wiki = 'https://zh.wikipedia.org/wiki/GB_2312'

    def __init__(self, errors=None):
        self.charset = {}
        nSec = 94
        nPos = 94
        for x in range(nSec):
            sec = x + 1
            for y in range(nPos):
                pos = y + 1
                # int
                gb_code = (sec + 0xa0) << 8 | (pos + 0xa0)
                # bytes
                b_code = struct.pack('>1H', gb_code)
                # unicode
                ch = b_code.decode('gb2312', errors='ignore')
                if not ch and errors:
                    ch = errors
                self.charset[gb_code] = ch

    def __repr__(self):
        return '<%s>' % self.title

    def get_sections(self, sections=None):
        if not isinstance(sections, list):
            sections = range(1, 94 + 1)
        char_set = []
        nPos = 94
        for sec in sections:
            sec_set = []
            for x in range(nPos):
                pos = x + 1
                i_code = (sec + 0xa0) << 8 | (pos + 0xa0)
                sec_set.append(self.charset[i_code])
            char_set.append(sec_set)
        return char_set

    def get_symbols(self):
        return self.get_sections(range(1, 10))

    def sp_search(self, chars):
        """section and postion"""
        inverse_charset = dict(zip(self.charset.values(), self.charset.keys()))
        codes = []
        for ch in chars:
            code = inverse_charset.get(ch)
            sec = (code >> 8) - 0xa0
            pos = (code & 0xff) - 0xa0
            codes.append('%s%s' % (sec, pos))
        return codes

    def as_txt(self, errors=None):
        err_ch = errors if errors else ''
        char_set = self.get_sections(range(1, 94 + 1))
        count = 0
        lines = []
        lines.append(self.title)
        lines.append('=' * len(self.title))
        lines.append(self.description)
        lines += self.detail
        lines.append(self.wiki)
        lines.append(' ' * 3 + ' '.join(['%02d' % (x + 1) for x in range(94)]))
        for sec_set in char_set:
            count += 1
            lines.append('%02d ' % count + ' '.join(
                [ch if ch else err_ch for ch in sec_set]
            ))
        return '\n'.join(lines)

    def as_html(self, errors=None):
        err_ch = errors if errors else ''
        char_set = self.get_sections(range(1, 94 + 1))
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
        html.append('<p>%s</p>' % self.description)
        html.append('<ol>')
        html += ['<li>%s<li>' % item for item in self.detail]
        html.append('</ol>')
        html.append('<p>%s</p>' % self.wiki)
        html.append('<ul>')
        html.append('<li>s: section</li>')
        html.append('<li>p: position</li>')
        html.append('</ul>')
        html.append('<p><code>code = (0xA0 + sec) << 8 + (0xA0 + pos)</code></p>')
        html.append('<table>')
        html.append(
            '<tr>' +
            '<td>s\p</td>' +
            ''.join(['<td>%02d</td>' % (x + 1) for x in range(94)]) +
            '</tr>'
        )
        count = 0
        for sec_set in char_set:
            count += 1
            html.append(
                '<tr>' +
                '<td>%02d</td>' % count +
                ''.join(['<td>%s</td>' % ch if ch else '<td>%s</td>' % err_ch for ch in sec_set]) +
                '</tr>'
            )
        html.append('</table>')
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--output-html', action='store_true', help='output html table')
    parser.add_argument('--output-txt', action='store_true', help='output txt table')
    parser.add_argument('--output-table', action='store_true', help='output ascii table')
    parser.add_argument('--sp-search', help='section and position for gb2312 character')
    args = parser.parse_args()

    gb2312 = GB2312()
    if args.output_txt:
        text = gb2312.as_txt(errors=u'　')
        # output str
        print(text.encode(args.encoding))
    if args.output_html:
        html = gb2312.as_html()
        print(html.encode(args.encoding))
    if args.output_table:
        char_set = gb2312.get_sections(range(1, 94 + 1))
        from asciitable import AsciiTable
        a = AsciiTable(char_set, header=False, encoding='gb2312')
        print(a.table().encode(args.encoding))
    if args.sp_search:
        chars = args.sp_search.decode('utf-8')
        print('GB2312 section and position:')
        print(gb2312.sp_search(chars))
