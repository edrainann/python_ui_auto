# -*- coding: utf-8 -*-
# @Time    : 2019/5/28
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.user_page.BankInfoPage import BankInfoPage


class BorrowerInfoPage(BasePage):
    """个人资料"""
    _person_address = (By.XPATH, "//*[@text='请选择居住住址']")
    _detail_address = (By.XPATH, "//*[@text='请输入详细地址']")
    _emergency_contact_name = (By.XPATH, "//*[@text='请输入紧急联系人姓名']")
    _emergency_contact_relations = (By.XPATH, "//*[@text='请选择紧急联系人关系']")
    _emergency_contact_phone = (By.XPATH, "//*[@text='请输入紧急联系人手机号']")
    _previous_page = (By.XPATH, "//*[@text='上一页']")
    _next_page = (By.XPATH, "//*[@text='继续']")

    def add_borrower_info(self):
        """添加个人资料"""
        self.find(self._person_address).click()
        self.find_by_text("北京市").click()
        self.find_by_text("市辖区").click()
        self.find_by_text("朝阳区").click()
        self.find(self._detail_address)
        self.find(self._detail_address).send_keys("这是输入详细地址-个人资料")
        self.find(self._emergency_contact_name).send_keys("这是输入紧急联系人姓名")
        self.find(self._emergency_contact_relations).click()
        self.find_by_text("股东").click()
        self.find(self._emergency_contact_phone).send_keys("18866110110")
        return self

    def gotoBankInfo(self):
        """进入银行卡信息页"""
        self.find(self._next_page).click()
        return BankInfoPage()
