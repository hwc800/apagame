from django.shortcuts import render

# Create your views here.
from app03.models import select_machine_info


def select_machine(requests):
    if requests.method == 'GET':
        datas = select_machine_info()
        if datas:
            return render(requests, 'db.html', {"data": datas})
        else:
            return render(requests, 'wait.html')
