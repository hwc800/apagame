from django.shortcuts import render

# Create your views here.
from app03.models import select_machine_info


def select_machine(requests):
    # 机器状态查询
    if requests.method == 'GET':
        datas = select_machine_info()  # 把数据处理成对应格式
        if datas:
            return render(requests, 'machine_info.html', {"data": datas})  # 有数据时的正常页面
        else:
            return render(requests, 'wait.html')  # 没有数据时的页面
