# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 11:04
# @Author  : Edrain
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = self.getDriver()
        rect = self.driver.get_window_rect()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)

    def find_by_text(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='{}']".format(text)))

    def delete_text(self, element):
        """清空文本框"""
        ele = self.driver.find_element_by_xpath(element)
        ele.click()
        context = ele.get_attribute("text")
        self.driver.press_keycode(123)  # 将光标移动到末尾
        for i in range(len(context)):
            self.driver.press_keycode(67)  # 退格键
        return self

    def take_photo(self):
        """打开相机，进行拍照"""
        # driver = self.driver
        WebDriverWait(self.driver, 60, 0.1).until(lambda x: x.find_element_by_xpath(
            "//GLButton[@text='快门']"))
        self.driver.tap([(550, 1750)], 200)  # 快门
        WebDriverWait(self.driver, 60, 0.1).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[@text='确定']"))
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        sleep(4)

    def up_swipe(self):
        """斜向上滑动"""
        rect = self.driver.get_window_rect()
        touch = TouchAction(self.driver)
        touch.press(x=rect['width'] * 0.7, y=rect['height'] * 0.7).wait(200).\
            move_to(x=rect['width'] * 0.2, y=rect['height'] * 0.2).release().perform()  # 等待200ms
        sleep(0.5)

    def swipe_up_small(self):
        """底部方框的向上滑动"""
        sleep(0.5)
        rect = self.driver.get_window_rect()
        touch = TouchAction(self.driver)
        touch.press(x=rect['width'] * 0.8, y=rect['height'] * 0.8).wait(200).\
            move_to(x=rect['width'] * 0.3, y=rect['height'] * 0.3).release().perform()  # 等待200ms
        sleep(0.5)
