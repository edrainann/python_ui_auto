# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.user_page.SignUpPage import SignUpPage
from page.BasePage import BasePage
from page.user_page.ApplyUserPage import ApplyUserPage
# from page.user_page.SignUpPage import SignUpPage


class LoginUserPage(BasePage):
    _phone_locator = (By.XPATH, "//*[@text='请输入您的手机号']")
    _password_locator = (By.XPATH, "//*[@text='请输入密码']")
    _submit_locator = (By.XPATH, "//*[@text='提交']")
    _signup_button = (By.XPATH, "//*[@text='新用户注册']")

    def loginUserByPassword(self, phone, password):
        """用户输入手机号、密码登录"""
        self.delete_text("//android.widget.EditText[@index='1']")  # 清空手机号
        self.find(self._phone_locator).send_keys(phone)
        self.find(self._password_locator).send_keys(password)
        self.find_by_text("提交").click()
        # if self.find_by_text("马上申请"):
        #     return ApplyUserPage()
        # else:
        #     return HomeUserPage()
        return ApplyUserPage()

    def gotoSignUp(self):
        """跳转到新用户注册页面"""
        self.find(self._signup_button).click()
        return SignUpPage()
