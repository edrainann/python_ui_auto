# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 17:47
# @Author  : Edrain
from page.app import App


class TestBorrowerAuthPage(object):
    @classmethod
    def setup_class(cls):
        cls.loginUserPage = App.main()

    def setup_method(self):
        # self.signUpPage = self.loginUserPage.gotoSignUp()
        # self.applyUserPage = self.signUpPage.singUp("18888880055", "123456a")
        self.applyUserPage = self.loginUserPage.loginUserByPassword("18888880055", "123456a")
        self.borrowerAuthPage = self.applyUserPage.applyNow()

    def test_borrower_auth(self):
        """填写身份认证信息"""
        self.borrowerAuthPage.add_borrower_info("哇哈哈", "610112198406239312")
        self.borrowerAuthPage.add_borrower_front()
        self.borrowerAuthPage.add_borrower_back()
        self.borrowerAuthPage.add_borrower_hold()
        self.borrowerAuthPage.add_borrower_person()
        self.borrowerAuthPage.gotoBorrowerInfo()

