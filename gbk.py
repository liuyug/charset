#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import struct


class GBK(object):
    title = 'CODE TABLE OF GBK'
    description = u"GBK即汉字内码扩展规范，K为汉语拼音Kuo Zhan（扩展）中“扩”字的声母。英文全称Chinese Internal Code Specification。由于GB 2312-80只收录6763个汉字，有不少汉字，如部分在GB 2312-80推出以后才简化的汉字（如“啰”），部分人名用字（如中国前总理朱镕基的“镕”字），台湾及香港使用的繁体字，日语及朝鲜语汉字等，并未有收录在内。于是厂商微软利用GB 2312-80未使用的编码空间，收录GB 13000.1-93全部字符制定了GBK编码。GBK自身并非国家标准，只是曾由国家技术监督局标准化司、电子工业部科技与质量监督司公布为“技术规范指导性文件”。"
    detail = [
        u'字符有一字节和双字节编码，00–7F范围内是第一个字节，和ASCII保持一致，此范围内严格上说有96个文字和32个控制符号。之后的双字节中，前一字节是双字节的第一位。总体上说第一字节的范围是81–FE（也就是不含80和FF），第二字节的一部分领域在40–7E，其他领域在80–FE。',
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
        'gbk1': (0xa1, 0xa9, 0xa1, 0xfe),
        'gbk2': (0xb0, 0xf7, 0xa1, 0xfe),
        'gbk3_1': (0x81, 0xa0, 0x40, 0x7e),
        'gbk3_2': (0x81, 0xa0, 0x80, 0xfe),
        'gbk4_1': (0xaa, 0xfe, 0x40, 0x7e),
        'gbk4_2': (0xaa, 0xfe, 0x80, 0xa0),
        'gbk5_1': (0xa8, 0xa9, 0x40, 0x7e),
        'gbk5_2': (0xa8, 0xa9, 0x80, 0xa0),
        'user1': (0xaa, 0xaf, 0xa1, 0xfe),
        'user2': (0xf8, 0xfe, 0xa1, 0xfe),
        'user3_1': (0xa1, 0xa7, 0x40, 0x7e),
        'user3_2': (0xa1, 0xa7, 0x80, 0xa0),
    }
    color = {
        'gbk1': '#f79646',
        'gbk2': '#4bacc6',
        'gbk3_1': '#8064a2',
        'gbk3_2': '#8064a2',
        'gbk4_1': '#9bbb59',
        'gbk4_2': '#9bbb59',
        'gbk5_1': '#c0504d',
        'gbk5_2': '#c0504d',
        'user1': '#eeece1',
        'user2': '#ddd9c3',
        'user3_1': '#c4bd97',
        'user3_2': '#c4bd97',
    }

    def __init__(self, errors=None):
        self.charset = {}
        for r in self.define.values():
            self.charset.update(self.generate(*(r + (errors,))))

    def __repr__(self):
        return '<%s>' % self.title

    @classmethod
    def generate(cls, f1, f2, s1, s2, errors=None):
        charset = {}
        for x in range(f1, f2 + 1):
            for y in range(s1, s2 + 1):
                code = (x << 8) | y
                # bytes
                b_code = struct.pack('>1H', code)
                # unicode
                ch = b_code.decode(cls.encoding, errors='ignore')
                if not ch and errors:
                    ch = errors
                charset[code] = ch
        return charset

    @classmethod
    def get_area_name(cls, code):
        f = code >> 8
        s = code & 0xff
        for k, v in cls.define.items():
            if v[0] <= f <= v[1] and v[2] <= s <= v[3]:
                return k

    def sp_search(self, chars):
        """section and postion"""
        inverse_charset = dict(zip(self.charset.values(), self.charset.keys()))
        codes = []
        for ch in chars:
            code = inverse_charset.get(ch)
            codes.append('%04X' % code)
        return codes

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
        html.append('.gbk1 {background-color:%s;}' % self.color['gbk1'])
        html.append('.gbk2 {background-color:%s;}' % self.color['gbk2'])
        html.append('.gbk3_1 {background-color:%s;}' % self.color['gbk3_1'])
        html.append('.gbk3_2 {background-color:%s;}' % self.color['gbk3_2'])
        html.append('.gbk4_1 {background-color:%s;}' % self.color['gbk4_1'])
        html.append('.gbk4_2 {background-color:%s;}' % self.color['gbk4_2'])
        html.append('.gbk5_1 {background-color:%s;}' % self.color['gbk5_1'])
        html.append('.gbk5_2 {background-color:%s;}' % self.color['gbk5_2'])
        html.append('.user1 {background-color:%s;}' % self.color['user1'])
        html.append('.user2 {background-color:%s;}' % self.color['user2'])
        html.append('.user3_1 {background-color:%s;}' % self.color['user3_1'])
        html.append('.user3_2 {background-color:%s;}' % self.color['user3_2'])
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
        html.append(u'<p>不包含单字节编码 00-7F ，即 ASCII 范围。</p>')
        html.append('<p>')
        html.append('<span class="gbk1">GBK1</span>')
        html.append('<span class="gbk2">GBK2</span>')
        html.append('<span class="gbk3_1">GBK3</span>')
        html.append('<span class="gbk4_1">GBK4</span>')
        html.append('<span class="gbk5_1">GBK5</span>')
        html.append('<span class="user1">User1</span>')
        html.append('<span class="user2">User2</span>')
        html.append('<span class="user3_1">User3</span>')
        html.append('</p>')
        html.append('<table>')
        html.append(
            '<tr>' +
            '<td></td>' +
            ''.join(['<td>%02X</td>' % y for y in range(0x40, 0xff)]) +
            '</tr>'
        )
        for x in range(0x81, 0xff):
            row = []
            row.append('<td>%02X</td>' % x)
            for y in range(0x40, 0xff):
                code = (x << 8) | y
                name = self.get_area_name(code)
                row.append('<td class="%s">%s</td>' % (name, self.charset.get(code, err_ch)))
            html.append('<tr>' + ''.join(row) + '</tr>')
        html.append('</table>')
        html.append('</body>')
        html.append('</html>')
        return '\n'.join(html)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--encoding', default='utf-8', help='output encoding. default: utf-8')
    parser.add_argument('--output-html', action='store_true', help='output html table')
    parser.add_argument('--sp-search', help='section and position for gb2312 character')
    args = parser.parse_args()

    gbk = GBK()
    if args.output_html:
        html = gbk.as_html()
        print(html.encode(args.encoding))
    if args.sp_search:
        chars = args.sp_search.decode('utf-8')
        print('GBK section and position:')
        print(gbk.sp_search(chars))
