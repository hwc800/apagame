import pymysql

from functiong.db_functiong import select_f, select_new


# 剔除build_version表中不要的字段
build_version_blank = [
    "id", "TopTwo", "TopThree", "third", "fourth", "tag", "CommitId"
]


def select_new_database(version):
    version = version.replace("\'", "")
    version = version.replace("\"", "")
    db = pymysql.connect("9.135.94.3", "root", "123456789", "version_num", port=3306, charset='utf8')
    cursor = db.cursor()
    sql = "select * from build_version where version=\"%s\";" % version
    select_result = select_f(cursor=cursor, dbname="version_num", tablename="build_version", sql=sql)

    db.close()

    return select_result


def new_select_arges(version):
    # 联合查询
    import ast

    version = version.replace("\'", "")
    version = version.replace("\"", "")
    db = pymysql.connect("9.135.94.3", "root", "123456789", "version_num", port=3306, charset='utf8')
    cursor = db.cursor()
    need_key = ["pipeline","arges","version","tag","appversion","BuildClass","CommitId","build_mode","UpdaterChannelID","PufferChannelId","ASANENABLE",]
    # 联合查询两个表，只获取上面的字段
    sql = f"select bb.pipeline,aa.arges,bb.version,bb.tag,bb.appversion,bb.BuildClass,bb.CommitId,bb.build_mode,bb.UpdaterChannelID," \
          f"bb.PufferChannelId,bb.ASANENABLE from (SELECT * FROM version_num.build_arges where version='%s') as aa, " \
          f"(SELECT * FROM version_num.build_version where version='%s') as bb where aa.pipeline=bb.pipeline;" % (version, version)
    cursor.execute(sql)
    slet = cursor.fetchall()
    select_result = select_new(cursor=cursor, slet=slet, sql=sql, f=need_key)
    db.close()

    if select_result:
        for i in select_result:
            d = i["arges"]
            d = ast.literal_eval(d)
            i["arges"] = d
            commit = i["CommitId"]
            branch = i["tag"]
            commit_list = commit.split("_")
            branch_list = branch.split("+")
            i["engine_commit"] = commit_list[0] + "(SVN)"
            i["client_commit"] = commit_list[1] + "(SVN)"
            i["content_commit"] = commit_list[2] + "(P4)"
            i["engine_branch"] = branch_list[0]
            i["client_branch"] = branch_list[1]
            i["content_branch"] = branch_list[2]
            i.pop("CommitId")
            i.pop("tag")
    else:
        select_result = {}
    return select_result


def select_commit(version):
    version = version.replace("\'", "")
    version = version.replace("\"", "")
    db = pymysql.connect("9.135.94.3", "root", "123456789", "version_num", port=3306, charset='utf8')
    cursor = db.cursor()
    sql = "select * from build_version where version=\"%s\";" % version
    select_result = select_f(cursor=cursor, dbname="version_num", tablename="build_version", sql=sql)

    db.close()

    if not select_result:
        return {}

    # 可能查到多个相同版本号
    result = {}
    p = 0
    for i in select_result:
        page = {}

        commit = i["CommitId"]
        branch = i["tag"]
        commit_list = commit.split("_")
        branch_list = branch.split("+")
        page["engine_commit"] = commit_list[0]
        page["client_commit"] = commit_list[1]
        page["content_commit"] = commit_list[2]
        page["engine_branch"] = branch_list[0]
        page["client_branch"] = branch_list[1]
        page["content_branch"] = branch_list[2]
        result[p] = page
        p += 1
    p = 0
    for i in select_result:
        for key, value in i.items():
            if key not in build_version_blank:
                result[p][key] = value
        p += 1
    return result


# 需要显示在查询界面的参数可在此列表中添加参数名
ARGES_LIST = []
