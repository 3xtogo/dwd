#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: 3xtogo
    Status: Development
    Description: contains helpful functions...
"""

import datetime


def printSQL(query, result):
    print('===========')
    print('Query:', query, '\nResult:', result)
    print('===========')


def timeStamp():
    return '[{}]'.format(datetime.datetime.now())


def cTime():
    date = '{}'.format(datetime.datetime.now().ctime())
    return date
