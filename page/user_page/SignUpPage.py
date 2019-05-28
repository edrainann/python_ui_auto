# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class SignUpPage(BasePage):
    _phone_locator = (By.XPATH, "//*[@text='请输入您的手机号']")
    _verification_code_locator = (By.XPATH, "//*[@text='请输入验证码']")
    _verification_button = (By.XPATH, "//*[@text='获取验证码']")
    _password_locator = (By.XPATH, "//*[@text='请输入不少于6位数字与字母组合的密码']")
    _password_again_locator = (By.XPATH, "//*[@text='请再次输入密码']")
    _read_locator = (By.XPATH, "//*[@text='我已阅读并同意']")
    _sign_up_button = (By.XPATH, "//*[@text='注册' and @index='0']")

    def signUp(self, phone, password):
        """新用户注册"""
        self.find(self._phone_locator).send_keys(phone)
        self.find_by_text("获取验证码").click()
        self.find(self._verification_code_locator).send_keys("123456")
        self.find(self._password_locator).send_keys(password)
        self.find(self._password_again_locator).send_keys(password)
        self.find(self._read_locator).click()
        self.find(self._sign_up_button).click()
        return self  # 这个地方不能用return LoginUserPage，否则会抛错

