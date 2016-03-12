#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from distutils.core import setup

from charset import version


setup(
    name="charset",
    version=version,
    description="charset for Unicode, UTF-8, GB18030, GBK, GB2312",
    url="https://github.com/liuyug/charset",
    license="BSD",
    author="Yugang LIU",
    author_email="liuyug@gmail.com",
    packages=[
        'charset',
    ],
    scripts=['charset.py', 'ascii.py']
)
