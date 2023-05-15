def field(cursor, dbname, tablename):
    # 获取表结构
    sql = f"select table_name,column_name,column_comment from information_schema.columns where table_schema='{dbname}' and table_name='{tablename}';"
    try:
        cursor.execute(sql)
    except:
        raise ValueError(f"请确认{dbname},{tablename}是否存在")
    key = cursor.fetchall()
    return key


def select_f(cursor, sql, dbname, tablename):
    fi = field(cursor, dbname, tablename)
    fields = []
    # 得到所有的字段名
    for ih in fi:
        fields.append(ih[1])
    cursor.execute(sql)
    slet = cursor.fetchall()
    result = []
    # 给数据处理成键值对，然后返回
    for i in slet:
        dc = {}
        for j in range(len(i)):
            dc[fields[j]] = i[j]
        result.append(dc)

    if not result:
        return None

    return result


def select_new(cursor, sql, slet, f):
    fi = f
    fields = []
    # 得到所有的字段名
    for ih in fi:
        fields.append(ih)

    result = []
    # 给数据处理成键值对，然后返回
    for i in slet:
        dc = {}
        for j in range(len(i)):
            dc[fields[j]] = i[j]
        result.append(dc)

    if not result:
        return None

    return result
