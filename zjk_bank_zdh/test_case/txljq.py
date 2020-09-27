from test_case.login import Login
from tools.dirver import MyWebDriver
from tools.read_json import ReadJson
from upper_tools.uppertools import UpperTools
from parameterized import parameterized
import unittest,time

class Test_glq(unittest.TestCase):
    data = ReadJson.read_json('../test_element/element.json')["txljq"]
    driver = MyWebDriver.start()

    @classmethod
    def setUpClass(cls):
        Login.login()
        MyWebDriver.wait_element_present(cls.data["page"]).click()
        MyWebDriver.wait_element_present(cls.data["exploitpeople"]).click()
        MyWebDriver.wait_element_present(cls.data["txljq"]).click()

    def setUp(self):
        MyWebDriver.wait_element_present(self.data["page"]).click()

    @parameterized.expand([('describe', '2')])
    def test_1_add_ljq(self, describe, text):
        MyWebDriver.wait_element_present(self.data["addljq"]).click()
        MyWebDriver.wait_element_present(self.data["tcp"]).click()
        UpperTools.input(self.data["describe"], describe)
        MyWebDriver.wait_element_present(self.data["select"]).click()
        MyWebDriver.wait_element_present('/html/body/div[3]/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div/div[2]/ul[2]/li[%s]'%text).click()
        self.assertEqual(1, 1)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        MyWebDriver.start().close()