from tools.dirver import MyWebDriver
from tools.read_json import ReadJson
from upper_tools.uppertools import UpperTools

class Login:

    driver = MyWebDriver.start()
    data = ReadJson.read_json('../test_element/element.json')

    @classmethod
    def login(cls):
        data = cls.data['login']
        UpperTools.input(data['username'],'test004')
        UpperTools.input(data['password'],'qw123456')
        MyWebDriver.wait_element_present(data['button']).click()


if __name__ == '__main__':
    test = Login()
    test.login()