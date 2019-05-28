# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 17:47
# @Author  : Edrain
from page.app import App


class TestBankInfoPage(object):
    @classmethod
    def setup_class(cls):
        cls.loginUserPage = App.main()

    def setup_method(self):
        # self.signUpPage = self.loginUserPage.gotoSignUp()
        # self.applyUserPage = self.signUpPage.singUp("18888880055", "123456a")
        self.applyUserPage = self.loginUserPage.loginUserByPassword("18888880055", "123456a")

    def test_bank_info(self):
        """填写银行卡信息"""
        self.borrowerAuthPage = self.applyUserPage.applyNow()
        self.borrowerInfoPage = self.borrowerAuthPage.gotoBorrowerInfo()
        self.bankInfoPage = self.borrowerInfoPage.gotoBankInfo()
        self.bankInfoPage.add_bank_info("6217002710000680031")
        self.bankInfoPage.gotoStoreInfo()




