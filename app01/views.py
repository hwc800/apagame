from django.shortcuts import render

# Create your views here.
import os

from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from app01.models import select_machine_info
from functiong.new_database_select import select_new_database


def ind(requests):
    return JsonResponse({"error": "fialed no file"})


def down_loads(requests):
    if requests.method == 'GET':
        path = 'static/'
        files = os.listdir(path)
        context = {
            'fielname': files,
        }
        return render(requests, 'downloads.html', context)


def download_template(request):
    file = open('static/comp.csv', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response["filename"] = "comp.csv"
    response['Content-Disposition'] = 'static/comp.csv"'
    content_dis = 'attachment;filename="' + 'comp.csv' + '"'
    response['Content-Disposition'] = content_dis
    return response


def down(request):
    name = request.GET.get("name")
    file = open(f'static/{name}', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response["filename"] = f"{name}"
    response['Content-Disposition'] = f'static/{name}"'
    content_dis = 'attachment;filename="' + f'static/{name}' + '"'
    response['Content-Disposition'] = content_dis
    return response


def connect(requests):
    if requests.method == 'GET':
        datas = select_machine_info()
        if datas:
            return render(requests, 'db.html', {"data": datas})
        else:
            return render(requests, 'wait.html')


def main(requests):
    return render(requests, 'main.html')


# 提供的下载对应版本符号表接口
def url(requests):
    """
            REFRESH_TOKEN = "OWlXdvWgLtpRan1QQZTcreUzoPEAxe"
        COOKIES = ""
        bk_tickets = "w52Qf1j0rcg1hx9_F1ScoQPqAuMZ_ERn_SZt7_Wf8yo"
        app_code = "apgame-build"
        app_secret = "mrDz5d4Q6d5quRPbtq2LqEZ3IzLjsoZ0FPq2HVha9vjUGGyDfQ"
        bk_uid = "booleyu"
        env_name = "prod"
    :param requests:
    :return:
    """
    if requests.method == "GET":
        import pymysql as mysql

        version = requests.GET.get("version")
        db = mysql.connect("9.135.94.3", "root", "123456789", "aclient", port=3306, charset='utf8')
        cursor = db.cursor()
        sql = f'select * from qa_select where version={version};'

        cursor.execute(sql)
        results = cursor.fetchall()

        import json
        pipline_id, build_id = None, None
        # todo: 这里需要注意，token需要关注是否过期，项目id是否切换
        ACCESS_TOKEN = "83ueVqukO3Es3enAYqMVZjMrYYE1Lo"
        project_id = "afgame"
        if not results:
            # 新数据库中查询一次
            select_result = select_new_database(version)
            if not select_result:
                return JsonResponse({"error": "The version is not file"})
            select_result = select_result[-1]
            piplineUrl = select_result["pipeline"]

            if select_result["BuildClass"] in ["ipa", "ios_pak"]:
                if select_result["build_mode"] == "Shipping":
                    so_file = "AClient-IOS-Shipping.dSYM"
                elif select_result["build_mode"] == 'Development':
                    so_file = "AClient.dSYM"
                elif select_result["build_mode"] == "Test":
                    so_file = "AClient-IOS-Test.dSYM"
                else:
                    return JsonResponse({"error": "The version is not file"})
            else:
                so_file = "libUE4.so"
            artifactoryType = "PIPELINE"
            url = "error to get url"
            url_infos = piplineUrl.split("/")
            for info in url_infos:
                if info.startswith("p-"):
                    pipline_id = info
                    continue
                if info.startswith("b-"):
                    build_id = info
            if pipline_id and build_id:
                path = "%2f" + pipline_id + "%2f" + build_id + "%2f" + so_file
                url = 'http://devops.apigw.o.oa.com/prod/v2/apigw-user/artifactories/projects/%s/thirdPartyDownloadUrl?access_token=%s&amp;artifactoryType=%s&amp;path=%s' % (
                    project_id, ACCESS_TOKEN, artifactoryType, path)
                import requests as req
                response = req.get(url, headers={"Content-Type": "application/json", "accept": "application/json"})
                # url = "None URL, please check your piplineId and buildId, file name"
                if response.status_code == 200:
                    response_data = json.loads(response.text)
                    if not response_data["data"]:
                        return JsonResponse({"error": "The version is not file"})
                    url = response_data["data"][0]
            if not url:
                return JsonResponse({"error": "The version is not file"})
            else:
                return JsonResponse({"successful": url})
        data = {"pipline": results[0][4]}
        input_json = data
        piplineUrl = input_json["pipline"]
        if results[0][8] == "IOS" and results[0][7] == "app":
            if results[0][6] == "Shipping":
                so_file = "AClient-IOS-Shipping.dSYM"
            elif results[0][5] =='Development':
                so_file = "AClient.dSYM"
            elif results[0][5] == "Test":
                so_file = "AClient-IOS-Test.dSYM"
            else:
                return JsonResponse({"error": "The version is not file"})
        else:
            so_file = "libUE4.so"

        artifactoryType = "PIPELINE"
        url = "error to get url"
        url_infos = piplineUrl.split("/")
        for info in url_infos:
            if info.startswith("p-"):
                pipline_id = info
                continue
            if info.startswith("b-"):
                build_id = info
        if pipline_id and build_id:
            path = "%2f" + pipline_id + "%2f" + build_id + "%2f" + so_file
            url = 'http://devops.apigw.o.oa.com/prod/v2/apigw-user/artifactories/projects/%s/thirdPartyDownloadUrl?access_token=%s&amp;artifactoryType=%s&amp;path=%s' % (project_id, ACCESS_TOKEN, artifactoryType, path)
            import requests as req
            response = req.get(url, headers={"Content-Type": "application/json", "accept": "application/json"})
            # url = "None URL, please check your piplineId and buildId, file name"
            if response.status_code == 200:
                response_data = json.loads(response.text)
                if not response_data["data"]:
                    return JsonResponse({"error": "The version is not file"})
                url = response_data["data"][0]

        if not url:
            return JsonResponse({"error": "The version is not file"})
        else:
            return JsonResponse({"successful": url})


