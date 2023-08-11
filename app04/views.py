from django.shortcuts import render

# Create your views here.
from app04.models import select_phone_info


def select_machine(requests):
    if requests.method == 'GET':
        datas = select_phone_info()
        if datas:
            return render(requests, 'newdb.html', {"data": datas})
        else:
            return render(requests, 'wait.html')
