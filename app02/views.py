import ast
import json
import pymysql as mysql
import re, time
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from app02 import tests

# Create your views here.
from django.template import loader

from functiong import new_database_select


def select(requests):
    return render(requests, "select_version_info.html")


def arges_mesg(requests):
    return render(requests, "arges_mesg.html")


def version(requests):
    if requests.method == "GET":
        version = requests.GET.get("version")
        versions = version.split(".")
        datas = {}
        if not version or len(versions) != 4:
            return JsonResponse({"data": "no"})
        new_datas = new_database_select.new_select_arges(version)
        page = 0  # 用作版本号重复时，作为一个自增的key，用来区别同版本号的包并标记顺序
        if new_datas:
            for new_data in new_datas:
                new_data["混淆开关"] =  "开启" if new_data["ASANENABLE"] == "True" else "关闭"
                new_data.pop("ASANENABLE")
                datas[page] = new_data
                page += 1

            data = {
                "code": 0,
                "msg": "数据正常",
                "data_dict": datas
            }
            return JsonResponse(data)

        return JsonResponse({"data": {"code": 1, "msg": "版本异常或不存在"}})


def build_arges(requests):
    # 详细参数接口
    if requests.method == "GET":
        version = requests.GET.get("version")
        page = int(requests.GET.get("page"))

        versions = version.split(".")
        if not version or len(versions) != 4:
            return JsonResponse({"data": "no"})
        new_datas = new_database_select.new_select_arges(version)
        if new_datas:
            datas = new_datas[page]["arges"]
            datas["pipeline"] = new_datas[page]["pipeline"]
            data = {
                "arges": datas
            }
            return render(requests, "arges_mesg.html", data)

        return JsonResponse({"data": "no"})
