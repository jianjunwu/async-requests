#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/09/16 15:06:51
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
from async_requests import sessions
from async_requests.grequests import AsyncRequest, send, request
from async_requests.grequests import get, options, head
from async_requests.grequests import post, put, patch, delete
from async_requests.grequests import map, imap, collect_async_results
