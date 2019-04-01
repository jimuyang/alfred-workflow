#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author:   Jimu Yang
Contact:  17621660286@163.com
这是一个python2脚本 import workflow以及调用 yd-translate来工作
1. ascii cannot decote byte... 将默认编码设置为utf-8
2. 不要瞎写print alfred读取的就是sys.stdout
'''

from workflow import Workflow, ICON_INFO
import sys
import subprocess
import json

reload(sys)
sys.setdefaultencoding('utf-8')


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
    # trans_results = call_yd_translate('找零')

    # print type(trans_results)
    # print trans_results
    arr = trans_results.strip()[1:-1].split(',')
    # print arr

    # json_wrapper = ("{\"result\":" + trans_results + "}").replace("\'", "\"")
    # jo = json.loads(json_wrapper)

    for result in arr:
        result = result.strip()[1:-1]
        wf.add_item(title=result,
                    subtitle='...', valid=True, icon=ICON_INFO)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))

    # main(None)
