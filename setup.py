#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from distutils.core import setup


VERSION = "0.1.0"


setup(
    name="charset",
    version=VERSION,
    description="charset for Chinese GB2312",
    url="https://github.com/liuyug/charset",
    license="BSD",
    author="Yugang LIU",
    author_email="liuyug@gmail.com",
    scripts=['gb18030.py', 'utf8.py', 'gbk.py', 'gb2312.py', 'ascii.py']
)
