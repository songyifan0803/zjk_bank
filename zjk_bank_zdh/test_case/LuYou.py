from test_case.login import Login
from tools.dirver import MyWebDriver
from tools.read_json import ReadJson
from parameterized import parameterized
import unittest,time

class Test_LuYou(unittest.TestCase):
    data = ReadJson.read_json('../test_element/element.json')["luyou"]
    driver = MyWebDriver.start()

    @classmethod
    def setUpClass(cls):
        Login.login()

    def setUp(self):
        MyWebDriver.wait_element_present(self.data["page"]).click()

    # @parameterized.expand()
    def test_1_add_luyou(self):
        MyWebDriver.wait_element_present(self.data["page"]).click()
        self.assertEqual(1,1)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

