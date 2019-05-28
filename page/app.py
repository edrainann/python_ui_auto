# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 11:13
# @Author  : Edrain
from page.BasePage import BasePage
from page.user_page.LoginUserPage import LoginUserPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        return LoginUserPage()
