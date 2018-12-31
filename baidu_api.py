# -*- coding:utf-8 -*-

import urllib3
import json

import requests



class BaiduAI(object):
    def __init__(self):
        self.api_key = "mMrIsdXDSnQy3sW9BLVGgRyY"   # use your API Key
        self.secret_key = "myNtcTcO6wEskFaRlpTGIbYWGmSbpZrp"    # use your Sceret Key
        self.access_token = self.get_access_token(self.api_key, self.secret_key)

    def get_access_token(self, api_key, secret_key):
        '''获取token'''
        access_token_url = "https://aip.baidubce.com/oauth/2.0/token?" \
                           "grant_type=client_credentials&client_id={0}&client_secret={1}".format(api_key, secret_key)
        response = requests.post(access_token_url)
        return json.loads(response.content.decode("utf-8"))["access_token"]

    def test(self):
        '''文本测试'''
        pass

    def speech_recognition(self):
        '''语音识别'''
        pass

    def speech_synthesis(self):
        '''语音合成'''
        pass

    def sentiment_classify(self):
        '''词向量'''

        access_token = '24.e79954f09c8e26a5dfc2ff72eb0c6b56.2592000.1547788261.282335-15207272'
        http = urllib3.PoolManager()
        url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/topic' + '?access_token={0}'.format(access_token)
        params = {"title": "欧洲冠军联赛",
                  "content": "欧洲冠军联赛是欧洲足球协会联盟主办的年度足球比赛，代表欧洲俱乐部足球最高荣誉和水平，被认为是全世界最高素质、最具影响力以及最高水平的俱乐部赛事，亦是世界上奖金最高的足球赛事和体育赛事之一。"
                  }

        # 进行json转换的时候，encode编码格式不指定也不会出错
        encoded_data = json.dumps(params).encode('GBK')
        request = http.request('POST', url, body=encoded_data, headers={'Content-Type': 'application/json'})
        # 对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
        # 注意编码格式
        result = request.data.decode('GBK')
        print (result)

bd = BaiduAI()
bd.speech_recognition()

