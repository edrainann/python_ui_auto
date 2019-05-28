# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.user_page.BorrowerInfoPage import BorrowerInfoPage


class BorrowerAuthPage(BasePage):
    """身份认证"""
    _name_locator = (By.XPATH, "//*[@text='请输入姓名']")
    _idcard_locator = (By.XPATH, "//*[@text='请输入身份证号码']")
    _validity_period_id_locator = (By.XPATH, "//*[@text='格式为20181007-20381007']")

    def add_borrower_info(self, name, idcard):
        """添加用户姓名、身份证号"""
        self.find(self._name_locator).send_keys(name)
        self.find(self._idcard_locator).send_keys(idcard)
        self.find(self._validity_period_id_locator).send_keys("20110202-长期")
        return self

    def add_borrower_front(self):
        """上传身份证正面"""
        self.driver.tap([(300, 450)], 100)  # 身份证正面
        # touch = TouchAction(self.driver)
        # rect = self.driver.get_window_rect()
        # touch.press(x=rect['width']*0.3, y=rect['hegiht']*0.8)  # 身份证正面
        self.take_photo()
        return self

    def add_borrower_back(self):
        """上传身份证反面"""
        self.driver.tap([(800, 450)], 100)  # 身份证反面
        self.take_photo()
        return self

    def add_borrower_hold(self):
        """上传手持身份证"""
        self.driver.tap([(300, 800)], 100)  # 手持身份证
        self.take_photo()
        return self

    def add_borrower_person(self):
        """上传大头照"""
        self.driver.tap([(800, 800)], 100)  # 大头照
        self.find_by_text("直接拍照")
        self.find_by_text("直接拍照").click()
        self.take_photo()
        return self

    def gotoBorrowerInfo(self):
        """点击继续"""
        self.find_by_text("20110202-长期")
        self.find_by_text("继续").click()
        return BorrowerInfoPage()


