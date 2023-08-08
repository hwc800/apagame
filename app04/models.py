from django.db import models
import pymysql as mysql


# Create your models here.
def select_phone_info():
    # 创建数据库连接对象。
    db = mysql.connect("9.135.94.3", "root", "123456789", "mysql", port=3306, charset='utf8')
    # 使用 cursor() 方法创建一个游标对象cursor
    cursor = db.cursor()
    # SQL语句
    sql = 'select * from web.phone_info;'
    cursor.execute(sql)
    results = cursor.fetchall()
    datas = [["phone", "资产编码", "设备归属者", "借用人", "借用日期", "是否归还", "归还日期", "借出人", "备注"]]
    for i in results:
        datas.append(list(i[1:]))

    return datas
