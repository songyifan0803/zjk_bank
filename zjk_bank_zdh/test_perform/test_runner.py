#!/usr/bin/env python
# -*- coding:utf-8 -*-
#====#====#====#====
#Author:
#CreatDate:
#Version:
#====#====#====#====

import unittest
from HTMLTestRunner_cn import HTMLTestRunner  # 用例执行器
import time
from tools.read_json import ReadJson


if __name__ == '__main__':
    ts = unittest.TestSuite()
    loader = unittest.TestLoader()
    # 通过设置执行设置文档获取相应的用例
    config = ReadJson.read_json("test_load_gui.conf")
    tests = loader.loadTestsFromNames(config["testLoadList"])
    # 形成测试套件
    ts.addTests(tests)
    unittest.TextTestRunner().run(ts)
    # 用时间戳来命名报告文件，避免文件名重复
    # now = time.strftime("%Y-%m-%d_%H%M%S")
    # filename = "../test_report/" + now + ".html"
    # # 以字节写入模式打开一个文件，用来接收执行结果
    # with open(filename, 'wb') as fp:
    # # 执行器配置
    #     runner = HTMLTestRunner(
    #         stream=fp,
    #         verbosity=2,
    #         title='张家口bank 测试报告',
    #         description="测试模块：路由",
    #         tester="张佳惺")
    #     # 执行器执行
    #     runner.run(ts)