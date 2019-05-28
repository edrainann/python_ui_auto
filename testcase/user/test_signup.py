# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from time import sleep
from page.app import App


class TestSignUp(object):
    @classmethod
    def setup_class(cls):
        # cls.loginUserPage = App.main().gotoSignUp()
        cls.loginUserPage = App.main()

    def setup_method(self):
        # self.loginUserPage: LoginUserPage = TestLogin.loginUserPage
        self.signUpPage = self.loginUserPage.gotoSignUp()

    def test_signup(self):
        self.signUpPage.signUp("18888889780", "123456a")
        sleep(20)
