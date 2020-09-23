#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tools.py
@Time    :   2020/09/23 14:02:21
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''

from functools import wraps
import time


def retry(exceptions, delay=0.001, max_retries=3):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            final_excep = None
            for counter in range(max_retries):
                if counter > 0:
                    time.sleep(delay)
                final_excep = None
                try:
                    value = func(*args, **kwargs)
                    return value
                except tuple(exceptions) as e:
                    print(f"Retry {counter + 1} cased by {e}")
                    final_excep = e
                    pass  # or log it
            if final_excep is not None:
                raise final_excep
        return inner_wrapper
    return outer_wrapper
