# -*- coding: utf-8 -*-
# @Time    : 2019/5/28
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.user_page.StoreInfoPage import StoreInfoPage


class BankInfoPage(BasePage):
    _bank_card_number = (By.XPATH, "//*[@text='请输入银行卡号']")
    _bank_name = (By.XPATH, "//*[@text='自动识别银行名称']")
    _bank_branch = (By.XPATH, "//*[@text='请输入开户支行']")
    _bank_phone = (By.XPATH, "//*[@text='请输入预留手机号']")

    def add_bank_info(self, bankcard):
        """添加银行卡信息"""
        self.find(self._bank_card_number).send_keys(bankcard)
        self.find_by_text(bankcard)
        self.find_by_text(bankcard).click()
        self.find(self._bank_name).click()
        self.find(self._bank_branch).send_keys("这是银行卡的开户支行")
        self.find(self._bank_phone).send_keys("13288569831")
        return self

    def gotoStoreInfo(self):
        """进入"""
        self.find_by_text("继续").click()
        return StoreInfoPage()