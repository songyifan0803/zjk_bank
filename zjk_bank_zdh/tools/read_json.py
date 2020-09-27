import json5
class ReadJson:


    @classmethod
    def read_json(cls, path):
        """
        此方法用于读取test_element文件夹下的element.json文件内容
        :return: json文件内容
        """
        with open(path) as f:
            data = json5.load(f)
            return data


if __name__ == '__main__':

    test = ReadJson.read_json('../test_element/element.json')
    print(test)