# -*- encoding: utf-8 -*-
import random
import time
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class Tool(object):

    def __init__(self, driver):
        self.driver = driver  # 这里不能再文件顶部导入webdriver，不然之后会有冲突
        # self.driver = None

    def up_swipe(self):
        """斜向上滑动
        """
        rect = self.driver.get_window_rect()
        touch = TouchAction(self.driver)
        touch.press(x=rect['width'] * 0.8, y=rect['height'] * 0.8).wait(200).\
            move_to(x=rect['width'] * 0.3, y=rect['height'] * 0.3).release().perform()  # 等待200ms
        sleep(0.5)

    def swipe_up_small(self):
        """底部方框的向上滑动"""
        sleep(0.5)
        rect = self.driver.get_window_rect()
        touch = TouchAction(self.driver)
        touch.press(x=rect['width'] * 0.8, y=rect['height'] * 0.8).wait(200).\
            move_to(x=rect['width'] * 0.3, y=rect['height'] * 0.3).release().perform()  # 等待200ms
        sleep(0.5)

    def swipe_down(self, site):
        driver = self.driver
        # driver.implicitly_wait(30)
        # button = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(site))
        # button.click()
        button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, site)))     # 等待XPATH元素可见
        # self.smart_wait(site)
        # button = driver.find_element_by_xpath(site)
        # sleep(2)
        """从button元素像下滑动200元素"""
        Action = TouchActions(driver)
        Action.scroll_from_element(button, 0, 34).perform()
        sleep(2)
        # print("success")

    def swipe_down02(self, site):
        """从button元素像下滑动68元素"""
        driver = self.driver
        # driver.implicitly_wait(30)
        # button = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(site))
        # button.click()
        button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, site)))     # 等待XPATH元素可见
        # self.smart_wait(site)
        # button = driver.find_element_by_xpath(site)
        # sleep(2)
        """从button元素像下滑动200元素"""
        Action = TouchActions(driver)
        Action.scroll_from_element(button, 0, 68).perform()
        sleep(2)
        # print("success")

    def dian_queding(self, element):
        """等待元素出现之后,点击确定"""
        queding = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(element))
        queding.click()
        sleep(1)

    def wait_click_queding(self, element):
        """等待元素出现之后,点击确定"""
        WebDriverWait(self.driver, 20, 0.3).until(lambda driver: driver.find_element_by_xpath(element))
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()

    def smart_tap(self):
        """等待元素出现之后,点击确定
        """
        sleep(0.5)
        self.driver.tap([(1000, 1400)], 400)
        # sleep(0.2)

    def take_photo(self):
        """打开相机，进行拍照"""
        driver = self.driver
        # sleep(0.8)
        WebDriverWait(driver, 60, 0.1).until(lambda x: x.find_element_by_xpath(
            "//GLButton[@text='快门']"))
        driver.tap([(550, 1750)], 200)  # 快门
        WebDriverWait(driver, 60, 0.1).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[@text='确定']"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        sleep(4)
        # WebDriverWait(driver, 60, 0.2).until(lambda x: x.find_element_by_xpath(
        #     "//android.widget.TextView[@text='采集照片']"))

    def smart_wait(self, element_xpath):  # 智能等待时间，60秒超时
        driver = self.driver
        for i in range(60):            # 循环60次，从0至59
            if i >= 59 :               # 当i大于等于59时，打印提示时间超时
                print("timeout")
                break
            try:                       # try代码块中出现找不到特定元素的异常会执行except中的代码
                # if driver.find_element_by_id(element_id): # 如果能查找到特定的元素id就提前退出循环
                if driver.find_element_by_xpath(element_xpath): # 如果能查找到特定的元素id就提前退出循环
                    print(i)
                    break
            except:                    # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
                print("wait for find element")
            sleep(1)

    def is_element_exist(self, identifyBy, c):
        # def main(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        # driver = self.driver
        # time.sleep(1)
        flag = None
        try:
            if identifyBy == "xpath":
                # self.driver.find_element_by_xpath(c)
                wait = WebDriverWait(self.driver, 3)
                wait.until(ec.presence_of_element_located((By.XPATH, c)))  # 等待该xpath元素最多10s，找到则返回元素，否则抛异常
                # WebDriverWait(self.driver, 5, 0.8).until(lambda x: x.find_element_by_xpath(c))  # 等待XPATH元素可见
                # self.driver.find_element_by_xpath(c).click()
            # elif identifyBy == "id":
            #     # self.driver.implicitly_wait(60)
            #     self.driver.find_element_by_id(c)
            #     self.driver.find_element_by_id(c).click()
            # elif identifyBy == "name":
            #     self.driver.find_element_by_name(c)
            #     self.driver.find_element_by_name(c).click()
            flag = True
            print("can find: ", c)
            # self.driver.find_element_by_name(c).click()
        # except NoSuchElementException as e:
        except TimeoutException as e:
            flag = False
            print("获取元素超时因为{}，无法找到{}元素", format(e, c))
            print("can't find: %s" % c)
        finally:
            return flag

    def phone_code_generator(self):
        """手机号码末尾随机四位数字"""
        # 倒数第一位数字
        first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        third = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        fourth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        # 拼接手机号
        return "1888888{}{}{}{}".format(fourth, third, second, first)
        # print("手机号码是：" + "1888888{}{}{}".format(fourth, third, second, first))

    def phone_generator(self):
        """随机生成手机号码"""
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)
        # print("手机号码是：" + "1{}{}{}".format(second, third, suffix))

    def idcard_generator(self):
        """ 随机生成新的18为身份证号码 """
        ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
        t = time.localtime()[0]
        x = '%02d%02d%02d%04d%02d%02d%03d' % (
        random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18),
        random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]
        IDCard = '%s%s' % (x, LAST[y % 11])
        # birthday = '%s-%s-%s 00:00:00' % (IDCard[6:14][0:4], IDCard[6:14][4: 6], IDCard[6:14][6:8])
        return IDCard
        # print("身份证号码：" + IDCard)

    def idcard_even_generator(self):
        """ 随机生成尾数为新的18为偶数的身份证号码 """
        for j in range(17):
            ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
            LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
            t = time.localtime()[0]
            x = '%02d%02d%02d%04d%02d%02d%03d' % (
                random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18),
                random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
            y = 0
            for i in range(17):
                y += int(x[i]) * ARR[i]
            end = LAST[y % 11]
            # print("末尾的数字是", end)
            IDCard = '%s%s' % (x, end)
            if LAST[y % 11] in ["0", "2", "4", "6", "8"]:
                return IDCard
            else:
                continue

    def idcard_odd_generator(self):
        """ 随机生成尾数为新的18为奇数身份证号码 """
        for j in range(17):
            ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
            LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
            t = time.localtime()[0]
            x = '%02d%02d%02d%04d%02d%02d%03d' % (
                random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18),
                random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
            y = 0
            for i in range(17):
                y += int(x[i]) * ARR[i]
            end = LAST[y % 11]
            print("末尾的数字是", end)
            IDCard = '%s%s' % (x, end)
            if LAST[y % 11] in ["1", "3", "5", "7", "9"]:
                print("身份证号码：" + IDCard)
                break
            else:
                continue

    def num_chinese(self, num):
        """阿拉伯数字转换为中文汉字"""
        dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七",
                "8": "八", "9": "九"}
        y = u""
        for x in u"" + str(num):
            y += dict[str(x)]
        return y

    def license_no(self):
        """随机生成15位营业执照号"""
        license_no = ""
        for i in range(15):
            num = random.randint(0, 9)
            license_no += str(num)
        return license_no

    def delete_text(self, element):
        """清空文本框"""
        ele = self.driver.find_element_by_xpath(element)
        ele.click()
        context = ele.get_attribute("text")
        self.driver.press_keycode(123)  # 将光标移动到末尾
        # for i in range(len(text.decode('utf-8'))):
        for i in range(len(context)):
            self.driver.press_keycode(67)   # 退格键

    # def up_swipe(self):
    #     """向上滑动
    #     """
    #     rect = self.driver.get_window_rect()
    #     touch = TouchAction(self.driver)
    #     touch.press(x=rect['width'] * 0.7, y=rect['height'] * 0.7).wait(200).\
    #         move_to(x=rect['width'] * 0.3, y=rect['height'] * 0.3).release().perform()  # 等待200ms
    #     sleep(0.5)
    #     print("已上滑")