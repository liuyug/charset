#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys


def ascii_set():
    char_begin = 32
    char_end = 128
    codes = range(char_begin, char_end)
    return codes


def txt(output=sys.stdout):
    codes = ascii_set()
    header = ' | DEC  HEX   HTML CH'
    ncol = 80 // len(header)
    nrow = len(codes) // ncol
    less = len(codes) % ncol
    for x in range(0, ncol):
        output.write(header)
    output.write(' |\n')
    for x in range(0, nrow):
        for y in range(0, ncol):
            code = codes[x + y * nrow]
            char_line = ' | %3d 0x%02x &#%03d; %02c' % (code, code, code, chr(code))
            output.write(char_line)
        output.write(' |\n')
    if less:
        for x in range(less, 0, -1):
            code = codes[-x]
            char_line = ' | %3d 0x%02x &#%03d; %02c' % (code, code, code, chr(code))
            output.write(char_line)
        output.write(' |\n')
    return


if __name__ == '__main__':
    txt()
