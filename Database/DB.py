import pymysql
from django.shortcuts import render

class DB():
    '''数据库相关操作'''
    def __init__(self):
        '''
        初始化数据库对象，数据库连接
        '''
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='root', port=3306, database='tripleskg')
            self.conected = True
            self.cursor = self.db.cursor()
            print('数据库连接成功')
        except pymysql.Error as e:
            print('数据库连接失败',e)

    def DropTable(self,table):
        '''
        删除一张数据表
        :param table: 需要删除的数据表名
        :return: 无
        '''
        sql = "drop table {};".format(table)
        self.cursor.execute(sql)
        print("数据库操作：",sql)

    def Clear(self,table):
        '''
        清除一张数据表所有内容
        :param table: 待清除数据表名
        :return:
        '''
        sql = 'truncate table {}'.format(table)
        print("数据库操作：", sql)
        self.cursor.execute(sql)

    def Insert(self,table,data):
        '''
        :param table: 待插入数据表名称
        :param data: 待插入数据
        :return: 无
        '''
        self.Clear(table)
        print('打开数据表:',table)
        index = 1
        for d in data[1:]:
            print(d)
            sql = "INSERT INTO {}(subject, predicate, object) values ('{}','{}','{}')".\
                format(table, d['head'], d['relation'], d['tail'])
            try:
                print("数据库操作：", sql)
                self.cursor.execute(sql)
                self.db.commit()
                print("插入成功")
            except pymysql.Error as e:
                print("插入失败", e)
                self.db.rollback()


    def SelectAll(self):
        sql = "SELECT * from main"
        try:
            print("数据库操作：", sql)
            self.cursor.execute(sql)
            self.db.commit()
            print('数据库操作：{}成功'.format(sql))
            data = list(self.cursor.fetchall())
            print(data[0][0])
        except pymysql.Error as e:
            print("{} 失败".format(sql))
            self.db.rollback()

    def Select(self, sql):
        try:
            print("数据库操作：", sql)
            self.cursor.execute(sql)
            self.db.commit()
            print("数据库操作成功：{}成功".format(sql))
            # print(self.cursor.fetchall())
            data = list(self.cursor.fetchall())
            print(data)
            return data
        except pymysql.Error as e:
            print("{}失败".format(sql))
            self.db.rollback()