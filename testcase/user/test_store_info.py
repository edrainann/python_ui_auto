# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from page.app import App


class TestStoreInfoPage(object):
    @classmethod
    def setup_class(cls):
        cls.loginUserPage = App.main()

    def setup_method(self):
        # self.signUpPage = self.loginUserPage.gotoSignUp()
        # self.applyUserPage = self.signUpPage.singUp("18888880055", "123456a")
        self.applyUserPage = self.loginUserPage.loginUserByPassword("18888880055", "123456a")

    def test_bank_info(self):
        """填写门店信息"""
        self.borrowerAuthPage = self.applyUserPage.applyNow()
        self.borrowerInfoPage = self.borrowerAuthPage.gotoBorrowerInfo()
        self.bankInfoPage = self.borrowerInfoPage.gotoBankInfo()
        self.storeInfoPage = self.bankInfoPage.gotoStoreInfo()
        self.storeInfoPage.add_strore_info()
        self.storeInfoPage.add_business_photo()
        self.storeInfoPage.already_read()
        self.storeInfoPage.gotoWaitCreditPage()





