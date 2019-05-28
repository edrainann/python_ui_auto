# -*- coding: utf-8 -*-
# @Time    : 2019/5/28
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.user_page.WaitCreditPage import WaitCreditPage
from utils.tool import Tool


class StoreInfoPage(BasePage):
    _business_type = (By.XPATH, "//*[@text='选择类型']")
    _business_number = (By.XPATH, "//*[@text='营业执照号或统一社会信用代码']")
    _enterprise_name = (By.XPATH, "//*[@text='与营业执照保持一致']")
    _legal_representative = (By.XPATH, "//*[@text='与营业执照保持一致']")
    _person_with_legal_representative = (By.XPATH, "//*[@text='选择关系']")
    _business_address = (By.XPATH, "//*[@text='请选择实际经营地址']")
    _detail_business_address = (By.XPATH, "//*[@text='请输入实际经营街道地址']")

    def add_strore_info(self):
        """添加门店信息"""
        tool = Tool(self.driver)
        self.find(self._business_type).click()
        self.find_by_text("个体工商户").click()
        self.find(self._business_number).send_keys(tool.license_no())
        self.find(self._enterprise_name).send_keys("这是企业名称")
        self.find(self._legal_representative).send_keys("这是法定代表人")
        self.find(self._person_with_legal_representative).click()
        self.find_by_text("合伙经营人").click()
        self.find(self._business_address).click()
        self.find_by_text("北京市").click()
        self.find_by_text("市辖区").click()
        self.find_by_text("朝阳区").click()
        self.find(self._detail_business_address).send_keys("北京市朝阳区望京soho中心")
        return self

    def add_business_photo(self):
        """上传营业执照照片"""
        self.driver.tap([(300, 1650)], 100)  # 上传营业执照照片
        self.take_photo()
        return self

    def already_read(self):
        self.up_swipe()
        self.find_by_text("我已阅读并同意如下协议").click()
        return self

    def gotoWaitCreditPage(self):
        """提交额度申请"""
        self.find_by_text("提交额度申请").click()
        return WaitCreditPage()


