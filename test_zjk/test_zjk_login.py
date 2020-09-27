#!/usr/bin/env python
# -*- coding:utf-8

import pytest_selenium
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Test_login():


    def test_login(self):

        global brower
        browser = webdriver.Chrome(
            executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

        browser.create_options()
        # V76以及以上版本
        # browser.
        # option.add_experimental_option('useAutomationExtension', False)
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # # 不自动关闭浏览器
        # option.add_experimental_option("detach", True)
        browser.get("http://10.150.2.50:31545/open-inmanage/index.html#/login")
        browser.maximize_window()
        time.sleep(3)
        #输入参数
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/form/div[1]/div/div/input").send_keys('ali')
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/form/div[2]/div/div/input").send_keys("qw123456")
        time.sleep(2)
        # browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/form/div[4]/button').click()
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/form/div[4]/button').send_keys(Keys.ENTER)

    if __name__ == '__main__':

        test_login()
