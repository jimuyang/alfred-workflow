#!/usr/local/bin/python3

'''
Author:   Jimu Yang
Contact:  17621660286@163.com
这是一个python3脚本 使用youdao api来进行翻译工作
'''

import requests
import time
import random
import hashlib
from string import Template
import json
import sys

url = "http://fanyi.youdao.com/translate_o"
querystring = {"smartresult": ["dict", "rule"]}


def generatePayload(source):
    ts = str(int(time.time() * 1000))
    salt = ts + str(random.randint(1, 10))
    sign = hashlib.md5(('fanyideskweb' + source + salt +
                        'Nw(nmmbP%A-r6U3EUn]Aj').encode('utf-8')).hexdigest()
    return {"ts": ts, "salt": salt, "sign": sign, "src": source}


def translate(src):
    # payload = "i=hi&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=15534143179236&sign=55acfecd86f0cdccda828250bd50bc6a&ts=1553414317923&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTlME&typoResult=false"
    payload_template = Template("i=${src}&salt=${salt}&sign=${sign}&ts=${ts}&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&doctype=json&version=2.1&keyfrom=fanyi.web")

    headers = {
        'Cookie': "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=271625424@111.225.144.245; JSESSIONID=abcELnvDkDjsqfk7m6ydx; OUTFOX_SEARCH_USER_ID_NCOO=276591875.4945921; _ntes_nnid=1e16a9cdf3a3f052deb2aa4ad4f4847c,1584187160477; ___rl__test__cookies=1584187201937",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Referer': "http://fanyi.youdao.com/",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    # src = input('input:')
    payload = payload_template.substitute(**(generatePayload(src)))
    # print(payload.encode('utf-8'))

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers, params=querystring)
    data = json.loads(response.text)
    # print(data)

    result = []
    if ('translateResult' in data):
        result.append(data['translateResult'][0][0]['tgt'])
    if ('smartResult' in data):
        for o in data['smartResult']['entries']:
            if o.strip() != '':
                result.append(o.replace('\r\n', ''))
    # print(result)
    return result


if __name__ == u"__main__":
    # print(sys.argv)
    print(translate(sys.argv[1]))
