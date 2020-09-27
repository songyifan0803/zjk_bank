from AC_frame.tools.common import Common

class ConnSql:
    # 调用日志模块，传入参数为本模块地址
    logger = Common.write_log()
    # 引入连接mysql的包
    import pymysql
    # 解析配置文件内容，与数据库建立连接，并创建游标
    data = Common.get_ini("../config/config_data.ini", 'mysql', 'db_data')
    conn = pymysql.connect(data[0], data[1], data[2], data[3], charset=data[4])
    cur = conn.cursor()

    @classmethod
    def query_one(cls,sql):
        """
            从数据库中查询单个结果
        :param sql:
            sql查询语句
        :return:
            查询结果
        """
        try:
            cls.cur.execute(sql)
            result = cls.cur.fetchone()
            cls.logger.info(f"{sql}语句执行正常")
        except:
            cls.logger.error(f"{sql}语句执行错误")
        finally:
            cls.cur.close()
            cls.conn.close()
            return result

    @classmethod
    def query_all(cls,sql):
        """
            从数据库中查询多个结果
        :param sql:
            sql查询语句
        :return:
            查询结果
        """
        try:
            cls.cur.execute(sql)
            result = cls.cur.fetchall()
            cls.logger.info(f"{sql}语句执行正常")
        except:
            cls.logger.error(f"{sql}语句执行错误")
        finally:
            cls.cur.close()
            cls.conn.close()
            return result

    @classmethod
    def updata(cls,sql):
        """
            增删改数据库中数据
        :param sql:
            sql操作语句
        :return:
            None
        """
        try:
            cls.cur.execute(sql)
            cls.conn.commit()
            cls.logger.info(f"{sql}语句执行正常")
        except:
            cls.logger.error(f"{sql}语句执行错误")
        finally:
            cls.cur.close()
            cls.conn.close()

