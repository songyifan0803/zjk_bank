from selenium import webdriver
from tools.common import Common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException



# 定义返回单例模式中driver的类
class MyWebDriver:
    # 定义类的属性，在整个生命周期中将会保持地址的唯一性
    # 默认值定为none，为了判断里边是否有driver
    driver = None
    config = Common.get_ini("../config/config_data.ini",'test_url','dirver')
    print(config)

    def __init__(self):
        pass
    # 类方法装饰器，将普通方法转化为类方法，直接调用，无需实例化
    # 定义一个类方法，接收来自配置文件的参数，完整相关webdriver初始功能
    @classmethod
    def start(cls, browser=config[0]['browser'],
              url=config[1]['url']):
        """
        单例模式用于实例化driver
        :param browser: 打开浏览器类型，默认为配置文件中dirver分支下的配置
        :param url: 要打开的网址，默认为配置文件中dirver分支下的配置
        :return: driver实例化工具
        """
        if cls.driver is None:  # 判断webdriver是否存在，存在则直接返回，不存在就执行实例化driver的操作
            cls.driver = getattr(webdriver, browser)()
            # 和浏览器相关的操作实例化。
            cls.driver.maximize_window()  # 最大化
            cls.driver.implicitly_wait(5)  # 隐式等待
            cls.driver.get(url)  # 打开url（项目主页面）
        return cls.driver

    # 封装一个类方法，以显示等待的方式获取元素
    @classmethod
    def wait_element_present(cls, value, prop='xpath', freq=0.5, timeout=5):
        """
        寻显示等待找元素方法
        :param prop: 寻找元素方法，默认为xpath
        :param value: 元素的路径
        :param freq: 搜索间隔默认为0.5
        :param timeout:显示等待时间默认5秒
        :return: 元素对象或None
        """
        try:
            element = WebDriverWait(cls.driver, timeout, freq).until(ec.presence_of_element_located((prop, value)))
            return element
        except TimeoutException:
            return None

    # 封装一个类，用于返回元素查找的结果
    @classmethod
    def is_element_present(cls, value, prop='xpath', freq=0.5, timeout=5):
        """
        判断元素是否存在
        :param prop: 寻找元素方法，默认为xpath
        :param value: 元素的路径
        :param freq: 搜索间隔默认为0.5
        :param timeout: 显示等待时间默认5秒
        :return: login-pass 或 login-fail
        """
        element = cls.wait_element_present(prop, value, freq, timeout)
        if element is not None:
            return "login-pass"
        return "login-fail"

    @classmethod
    def input(cls,ele, value):
        """
        对输入框元素进行输入
        :param ele: 元素对象
        :param value: 要输入内容
        :return:
        """
        ele.click()
        ele.clear()
        ele.send_keys(value)

    @classmethod
    def select(cls,ele, text):
        """
        选择制定下拉框选项
        :param ele: 下拉框元素对象
        :param text: 下拉框的text内容
        :return:
        """
        from selenium.webdriver.support.select import Select
        try:
            Select(ele).select_by_visible_text(text)
        except:
            Select(ele).select_by_index(text)
            raise

    @classmethod
    def select_rand(cls, ele):
        """
        随机选择下拉框选项方法
        :param ele: 下拉框元素
        :return:
        """
        from selenium.webdriver.support.select import Select
        s1 = Select(ele)
        import random
        s1.select_by_index(random.randint(0, len(s1.options)-1))

    @classmethod
    def lots_paras(cls, data):
        temp = []
        for i in data.keys():
            for j in data[i]:
                temp_list = []
                temp_list.append(j)
                temp_tuple = tuple(temp_list)
                temp.append(temp_tuple)
        return temp


if __name__ == '__main__':
    test = MyWebDriver()
    test.start()