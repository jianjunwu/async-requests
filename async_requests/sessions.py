#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sessions.py
@Time    :   2020/09/16 15:07:19
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
from requests import Session
from requests.adapters import HTTPAdapter
from functools import partial
import traceback

TIMEOUT = 10
NUM_POOLS = 10
POOL_MAXSIZE = 10


class AsyncSession(Session):
    def __init__(self, keepalive=True, pool_connections=NUM_POOLS, pool_maxsize=POOL_MAXSIZE):
        super(AsyncSession, self).__init__()
        self.mount(
            "http://", HTTPAdapter(pool_connections, pool_maxsize))
        self.mount(
            "https://", HTTPAdapter(pool_connections, pool_maxsize))
        self.exception = None

    def request(self, method, url, **kwargs):
        resp = super(AsyncSession, self).request(method, url, **kwargs)
        return resp

