#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import argparse
from collections import OrderedDict

from charset import version, Unicode, UTF8, GB18030, GBK, GB2312


CHARSET_CLASS = OrderedDict((
    ('gb2312', GB2312),
    ('gbk', GBK),
    ('gb18030', GB18030),
    ('utf8', UTF8),
    ('unicode', Unicode),
))


def main():
    parser = argparse.ArgumentParser(
        description='CHARSET v%s' % version,
        epilog='System encoding: %s' % sys.getfilesystemencoding(),
    )
    parser.add_argument(
        '--encoding',
        choices=CHARSET_CLASS.keys(),
        required=True,
        help='Use charset',
    )
    parser.add_argument(
        '--panel',
        help='charset panel'
    )
    parser.add_argument(
        '-P',
        action='store_true',
        help='list panel'
    )
    parser.add_argument(
        '--char',
        action='store_true',
        help='output character for Unicode code'
    )
    parser.add_argument(
        '--code',
        action='store_true',
        help='output Unicode code for character'
    )
    parser.add_argument(
        'target',
        nargs='?',
        help='input char or output file'
    )

    args = parser.parse_args()

    in_encoding = out_encoding = sys.getfilesystemencoding()

    charset = CHARSET_CLASS[args.encoding]()

    if args.P:
        for k, v in charset.define.items():
            p = k[5:]
            print('Panel %s: %s' % (p, ' - '.join(v['desc'])))
    elif args.panel:
        html = charset.as_html(panels=args.panel.split(','))
        if args.target:
            with open(args.target, 'w') as f:
                f.write(html.encode('utf-8'))
        else:
            print(html.encode(out_encoding))
    elif args.code:
        chars = args.target.decode(in_encoding)
        print('%s code:' % args.encoding.upper())
        print(charset.codes(chars))
    elif args.char:
        if '-' in args.target:
            codes = args.target.split('-')
        elif ',' in args.target:
            codes = args.target.split(',')
        else:
            codes = [args.target]
        print('%s char:' % args.encoding.upper())
        print(''.join(charset.chars(codes)))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
