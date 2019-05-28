# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 13:50
# @Author  : Edrain
from time import sleep

from page.app import App
from page.BasePage import BasePage


class TestLogin(BasePage):
    @classmethod
    def setup_class(cls):
        cls.loginUserPage = App.main()

    def setup_method(self):
        self.loginUserPage = App.main().login_user_page()

    def test_login_right(self):
        self.loginUserPage.loginUserByPassword("18888880569", "123456a")
        sleep(20)
