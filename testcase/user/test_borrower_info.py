# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from page.app import App


class TestBorrowerInfoPage(object):
    @classmethod
    def setup_class(cls):
        cls.loginUserPage = App.main()

    def setup_method(self):
        # self.signUpPage = self.loginUserPage.gotoSignUp()
        # self.applyUserPage = self.signUpPage.singUp("18888880055", "123456a")
        self.applyUserPage = self.loginUserPage.loginUserByPassword("18888880055", "123456a")

    def test_borrower_info(self):
        """填写个人信息"""
        self.borrowerAuthPage = self.applyUserPage.applyNow()
        self.borrowerInfoPage = self.borrowerAuthPage.gotoBorrowerInfo()
        self.borrowerInfoPage.add_borrower_info()
        self.borrowerInfoPage.gotoBankInfo()


