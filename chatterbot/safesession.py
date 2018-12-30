# -*- coding:utf-8 -*-

import traceback

import requests


class SafeSession(requests.Session):
    def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):
        for i in range(3):
            try:
                return super(SafeSession, self).request(method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
            except Exception as e:
                print (e.message, traceback.format_exc())
                continue

        # 重试3次以后再加一次，抛出异常
        try:
            return super(SafeSession, self).request(method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
        except Exception as e:
            raise e
