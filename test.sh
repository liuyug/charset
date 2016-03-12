#!/bin/bash


charset="python charset.py"

char_search2()
{
    python -m 'charset.gb2312' --code 我们
    python -m 'charset.gb2312' --char 4650,3539

    python -m 'charset.gbk' --code 我们
    python -m 'charset.gbk' --char CED2,C3C7

    python -m 'charset.gb18030' --code 我们
    python -m 'charset.gb18030' --char CED2,C3C7

    python -m 'charset.utf8' --code 我们
    python -m 'charset.utf8' --char E68891,E4BBAC

    python -m 'charset.unicode' --code 我们
    python -m 'charset.unicode' --char 6211,4EEC
}

char_search()
{

    $charset --encoding gb2312 --code 我们
    $charset --encoding gb2312 --char 4650,3539

    $charset --encoding gbk --code 我们
    $charset --encoding gbk --char CED2,C3C7

    $charset --encoding gb18030 --code 我们
    $charset --encoding gb18030 --char CED2,C3C7

    $charset --encoding utf8 --code 我们
    $charset --encoding utf8 --char E68891,E4BBAC

    $charset --encoding unicode --code 我们
    $charset --encoding unicode --char 6211,4EEC
}

char_gen()
{
    $charset --encoding gb2312 --panel 0  gb2312.html

    $charset --encoding gbk --panel 0,1  gbk.html

    $charset --encoding gb18030 --panel 0,1  gb18030-0.html
    $charset --encoding gb18030 --panel 2  gb18030-2.html

    $charset --encoding utf8 --panel 0,1  utf-1.html
    $charset --encoding utf8 --panel 2  utf-2.html
    $charset --encoding utf8 --panel 3  utf-3.html

    $charset --encoding unicode --panel 0  uni-0.html
    $charset --encoding unicode --panel 1  uni-1.html
    $charset --encoding unicode --panel 2  uni-2.html
    $charset --encoding unicode --panel 3  uni-3.html
    $charset --encoding unicode --panel 14  uni-14.html
    $charset --encoding unicode --panel 15  uni-15.html
    $charset --encoding unicode --panel 16  uni-16.html
}

char_$1

# vim: tabstop=4 shiftwidth=4 expandtab
