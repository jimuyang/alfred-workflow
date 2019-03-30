#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author:   Jimu Yang
Contact:  17621660286@163.com
这是一个python2脚本 import workflow以及调用 yd-translate来工作
'''

from workflow import Workflow, ICON_INFO
import sys
import subprocess
import json


def call_yd_translate(src):
    '''
    try use subprocess to invoke yd-translate.py
    '''
    obj = subprocess.Popen(['./yd-translate.py', src],
                           stdout=subprocess.PIPE)
    stdout = obj.stdout.read()
    obj.stdout.close()
    # print stdout
    return stdout


def main(wf):
    # 去掉参数两边的空格
    # param = (wf.args[0] if len(wf.args) else '').strip()
    # print wf.args[0]
    trans_results = call_yd_translate(wf.args[0])

    # trans_results = call_yd_translate('sex')
    # print type(trans_results)

    json_wrapper = ("{\"result\":" + trans_results + "}").replace("\'", "\"")
    jo = json.loads(json_wrapper)

    for result in jo['result']:
        # print result
        wf.add_item(title=result, subtitle='...', valid=True, icon=ICON_INFO)

    wf.send_feedback()


if __name__ == u'__main__':
    wf = Workflow()
    sys.exit(wf.run(main))

    # main(None)
