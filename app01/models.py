import pymysql as mysql


# Create your models here.
def select_machine_info():
    # 创建数据库连接对象。
    db = mysql.connect("9.135.94.3", "root", "123456789", "mysql", port=3306, charset='utf8')
    # 使用 cursor() 方法创建一个游标对象cursor
    cursor = db.cursor()
    # SQL语句
    sql = 'select * from web.machine_info;'
    cursor.execute(sql)
    results = cursor.fetchall()
    datas = []
    for i in results:
        datas.append(list(i[1:]))
    top = ["机器", "状态", "占用情况", "最近使用时间"]
    datas.insert(0, top)
    return datas



