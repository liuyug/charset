#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct

from .utils import get_colors


class CharsetBase(object):
    title = 'CODE OF TABLE'
    description = []
    detail = []
    wiki = ''
    encoding = 'ascii'
    define = {
        'panel': {
            'desc': [],
            'range': (0x00, 0xff),
        },
    }
    category = {}

    def __init__(self, errors=None):
        pass

    def __repr__(self):
        return '<%s>' % self.title

    def get_category(self, b_code):
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
            codes.append(code.strip('0'))
        return codes

    def as_html(self, panels=None, errors=None):
        if panels is None:
            panels = ['0']
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
        for p in panels:
            category = self.category.get('panel' + p)
            if not category:
                continue
            colors = get_colors(len(category))
            for x in range(len(category)):
                html.append('.%s {background-color:%s;}' % (category[x]['name'], colors[x]))
        html.append('</style>')
        html.append('</head>')
        html.append('<body>')
        html.append('<h1>%s</h1>' % self.title)
        html.append('<p>Made by Yugang LIU</p>')
        html.append('<hr />')
        html.append('<h2>Description</h2>')
        for desc in self.description:
            html.append('<p>%s</p>' % desc)
        html.append('<ul>')
        html += ['<li>%s</li>' % item for item in self.detail]
        html.append('</ul>')
        html.append('<h2>Reference</h2>')
        html.append('<ul>')
        html.append('<li>wiki: <a href="%s" target="_blank">%s</a></li>' % (self.wiki, self.wiki))
        html.append('</ul>')
        html.append('<h2>Code Table</h2>')
        for p in panels:
            html += self.panel_as_html(p, err_ch)
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)

    def panel_as_html(self, panel, err_ch):
        define = self.define.get('panel' + panel)
        html = []
        html.append('<h3>%s</h3>' % ' - '.join(define['desc']))
        category = self.category.get('panel' + panel)
        if category:
            html.append('<table>')
            for c in category:
                html.append('<tr>')
                html.append('<td class="%s">%s</td>' % (
                    c['name'],
                    '%s - %s' % (c['desc'], c['name'].replace('_', ' ')),
                ))
                html.append('</tr>')
            html.append('</table>')
            html.append('<p></p>')
        html += self.do_panel_as_html(define, err_ch)
        return html

    def do_panel_as_html(self, define, err_ch):
        return []
