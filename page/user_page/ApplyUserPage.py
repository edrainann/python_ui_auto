# -*- coding: utf-8 -*-
# @Time    : 2019/5/27
# @Author  : Edrain
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.user_page.BorrowerAuthPage import BorrowerAuthPage


class ApplyUserPage(BasePage):
    _apply_now_button = (By.XPATH, "//*[@text='马上申请']")

    def applyNow(self):
        """点击马上申请"""
        self.find_by_text("额度")
        self.find(self._apply_now_button)
        self.find(self._apply_now_button).click()
        return BorrowerAuthPage()
