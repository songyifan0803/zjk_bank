from tools.read_json import ReadJson
from tools.dirver import MyWebDriver

class UpperTools:
    @classmethod
    def input(cls, elementpath ,value):
        """
        此方法调用tools底层工具，用于对元素进行输入操作
        :param elementpath: 元素地址
        :param value: 要输入的文本
        :return:
        """
        ele = MyWebDriver.wait_element_present(elementpath)
        MyWebDriver.input(ele, value)

    @classmethod
    def select(cls,elementpath,value):
        """
        # 用于指定选择下拉框
        :param elementpath: 元素的路径
        :param value: 下拉框的文本或index下标
        :return:
        """
        ele = MyWebDriver.wait_element_present(elementpath)
        MyWebDriver.select(ele,value)