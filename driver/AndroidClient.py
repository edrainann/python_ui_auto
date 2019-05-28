# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:54
# @Author  : Edrain
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):

    driver: WebDriver
    @classmethod
    def install_app(cls) -> WebDriver:
        """安装App"""
        caps = {}
        # 如果有必要，进行第一次安装
        # caps["app"]=''
        caps["platformName"] = "android"
        caps["deviceName"] = "021602a231330203"
        caps["appPackage"] = "com.xydsupplychainydlloan"
        caps["appActivity"] = ".MainActivity"
        # 解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        """重新App"""
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "021602a231330203"
        caps['automationName'] = 'UIAutomator2'
        caps["appPackage"] = "com.xydsupplychainydlloan"
        caps["appActivity"] = ".MainActivity"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps['noReset'] = True
        caps['autoGrantPermissions'] = 'true'  # 自动处理权限弹框,解决第一次启动的问题
        # caps['chromedriverExecutableDir'] = "/Users/seveniruby/projects/chromedriver/2.20"
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        # caps["udid"]="emulator-5554"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
