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
    # 添加行首，使得表格让人易懂
    datas = [["machine name", "Machine Status", "Machine Usage", "Last Usage Time", "10秒前cook数量", "当前cook数量"]]
    for i in results:
        datas.append(list(i[1:]))

    return datas
