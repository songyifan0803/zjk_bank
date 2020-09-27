import logging

class Common:
    logger = None
    @classmethod
    def ctime(cls):
        """
        获取ctime并转化为字符串
        :return: 当前时间ctime的字符串类型
        """
        import time
        return time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())

    @classmethod
    def write_log(cls):
        """
            在test_report文件下写入日志
        :param
            name:自定义的日志名称
        :return
            返回写入日志的工具
        """
        # 单例模式，防止在一次运行中写入多个文件
        if cls.logger ==None:
            # 获取对象
            cls.logger = logging.getLogger()
            # 设置信息等级，分为信息INFO,警告WARNING,错误ERROR等，等级越低可打印高等级信息，高等级不能打印低等级信息
            cls.logger.setLevel(level=logging.INFO)
            # 获得文件的句柄
            handler = logging.FileHandler('../test_report/'+cls.ctime()+'.log',encoding='utf8')
            # 定义写入格式
            formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
            # 给句柄定义写入格式
            handler.setFormatter(formatter)
            # 给对象添加句柄
            cls.logger.addHandler(handler)
            # 返回写入对象
            return cls.logger

    @classmethod
    def get_ini(cls, path, section, option):
        """
        从ini格式文件中读取内容
            :param
            path:ini文件路径
            section：节点的名称
            option：节点下的键名
        :return: 节点下键的对应值
        """
        import configparser
        #获取转化器对象
        cp = configparser.ConfigParser()
        # 读取ini文件内容
        cp.read(path,encoding='utf8')
        # 读取整个节点方法键列表
        sec = cp.options(section)
        # 获取节点下的键对应值,获取到的是字符串形式，可用eval转换为python中的格式
        data = cp.get(section,option)
        try:
            return eval(data)
        except:
            return data

    @classmethod
    def start_app(cls,cmd):
        """
        使用os命令启动程序
        :param cmd: cmd打开app命令
        :return:
        """
        import os,time
        os.system(f'start/b{cmd}')
        time.sleep(2)

if __name__ == '__main__':
    data = Common.get_ini('../config/config_data.ini','mysql','db_data')
    print(data)



