
import xlrd  # 用来读取excel文件
# from AC_frame.tools.common import Common

class ReadExcel:

    def __init__(self):
        pass

    @classmethod
    def read_excel_gui(cls, filepath, sheet_name, rs, re, c_data=2, c_expect=3):
        """
            用于读取特定格式的excal文件：第一列必须有-符号，第三列必须有 = 符号。
        :param
            filepath: excal文件的地址
        :param
            sheet_name: excal文件中sheet名
        :param
            rs: 开始行数-1
        :param
            re: 结束行数
        :param
            c_data: 第三列数据，是个列表套字典格式
        :param
            c_expect: 第四列数据
        :return:
            整个sheet表的内容
        """
        book = xlrd.open_workbook(filepath)  # 获取book对象
        sheet = book.sheet_by_name(sheet_name)  # 获取sheet表对象
        testdata_dict = {}
        for i in range(rs, re):
            fuc_name = sheet.cell(i, 0).value.split("-")[0]
            if fuc_name not in testdata_dict.keys():
                testdata_dict[fuc_name] = []
            temp = {}
            data_dict = {}
            data_list = sheet.cell(i, c_data).value.split("\n")
            for j in data_list:
                data_dict[j.split("=")[0]] = j.split("=")[1]
            temp["data"] = data_dict
            temp["expect"] = sheet.cell(i, c_expect).value
            testdata_dict[fuc_name].append(temp)
        return testdata_dict

    @classmethod
    def read_excel_api(cls, filepath, sheet_name, rs, re, c_uri=2, c_headers=3, c_data=4, c_expect=5):
        book = xlrd.open_workbook(filepath)  # 获取book对象
        sheet = book.sheet_by_name(sheet_name)  # 获取sheet表对象
        testdata_dict = {}
        for i in range(rs, re):
            fuc_name = sheet.cell(i, 0).value.split("-")[0]
            if fuc_name not in testdata_dict.keys():
                testdata_dict[fuc_name] = []
            temp = {}
            headers_dict = {}
            headers_key = sheet.cell(i, c_headers).value.split("=")[0]
            headers_value = sheet.cell(i, c_headers).value.split("=")[1]
            headers_dict[headers_key] = headers_value
            data_dict = {}
            data_list = sheet.cell(i, c_data).value.split("\n")
            for j in data_list:
                data_dict[j.split("=")[0]] = j.split("=")[1]
            temp["uri"] = sheet.cell(i, c_uri).value
            temp["headers"] = headers_dict
            temp["data"] = data_dict
            temp["expect"] = sheet.cell(i, c_expect).value
            testdata_dict[fuc_name].append(temp)
        return testdata_dict


if __name__ == '__main__':
    sheet = ReadExcel.read_excel_gui('../test_data/test_login_gui.xlsx', 'login', 1, 5)
    print(sheet)
    # sheet2 = ReadExcel.read_excel_api('../test_data/test_login_api.xlsx', 'login', 1, 2)
    # print(sheet2)
