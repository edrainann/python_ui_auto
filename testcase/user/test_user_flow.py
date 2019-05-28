# -*- coding: utf-8 -*-
# @Time    : 2019/5/28
# @Author  : Edrain
from page.app import App
from utils.tool import Tool


class TestUserFlow(object):
    # @classmethod
    # def setup_class(cls):
        # cls.loginUserPage = App.main()

    def setup_method(self):
        self.loginUserPage = App.main()

    def test_right_flow(self):
        tool = Tool(self)
        phone = tool.phone_code_generator()
        idcard = tool.idcard_even_generator()
        name = "雨点" + tool.num_chinese(phone[-4:])
        self.signUpPage = self.loginUserPage.gotoSignUp()
        self.signUpPage.signUp(phone, "123456a")
        self.applyUserPage = self.loginUserPage.loginUserByPassword(phone, "123456a")
        self.borrowerAuthPage = self.applyUserPage.applyNow()
        # 填写身份认证信息
        self.borrowerAuthPage.add_borrower_info(name, idcard)
        self.borrowerAuthPage.add_borrower_front()
        self.borrowerAuthPage.add_borrower_back()
        self.borrowerAuthPage.add_borrower_hold()
        self.borrowerAuthPage.add_borrower_person()
        # 填写个人信息
        self.borrowerInfoPage = self.borrowerAuthPage.gotoBorrowerInfo()
        self.borrowerInfoPage.add_borrower_info()
        # 填写银行卡信息
        self.bankInfoPage = self.borrowerInfoPage.gotoBankInfo()
        self.bankInfoPage.add_bank_info("6217002710000680031")
        # 填写门店信息
        self.storeInfoPage = self.bankInfoPage.gotoStoreInfo()
        self.storeInfoPage.add_strore_info()
        self.storeInfoPage.add_business_photo()
        self.storeInfoPage.already_read()
        self.storeInfoPage.gotoWaitCreditPage()
