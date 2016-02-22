#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class GB2312(object):
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
                ch = b_code.decode('gbk', errors='ignore')
                if not ch and errors:
                    ch = errors
                self.charset[gb_code] = ch

    def __repr__(self):
        return '<GB2312>'

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
        html.append('<title>CODE TABLE of GB2312-80</title>')
        html.append('<style type="text/css">')
        html.append('table {border-collapse:collapse;border-spacing:0;}')
        html.append('td {border:1px solid green;padding:0.3em;text-align:center;}')
        html.append('hr {border:width:75%;}')
        html.append('</style>')
        html.append('</head>')
        html.append('<body>')
        html.append('<h1>CODE TABLE of GB2312-80</h1>')
        html.append('<p>Made by Yugang LIU</p>')
        html.append('<hr />')
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
    parser.add_argument('--output-html', action='store_true', help='output html table')
    parser.add_argument('--output-txt', action='store_true', help='output txt table')
    parser.add_argument('--output-table', action='store_true', help='output ascii table')
    parser.add_argument('--sp-search', help='section and position for gb2312 character')
    args = parser.parse_args()

    gb2312 = GB2312()
    if args.output_txt:
        print(gb2312.as_txt(errors=u'　').encode('utf-8'))
    if args.output_html:
        print(gb2312.as_html().encode('utf-8'))
    if args.output_table:
        char_set = gb2312.get_sections(range(1, 94 + 1))
        from asciitable import AsciiTable
        a = AsciiTable(char_set, header=False)
        print(a.table().encode('utf-8'))
    if args.sp_search:
        chars = args.sp_search.decode('utf-8')
        print('GB2312 section and position:')
        print(gb2312.sp_search(chars))
