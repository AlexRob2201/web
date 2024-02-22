from django.shortcuts import render
import json
from bs4 import BeautifulSoup as bs
import requests
import datetime
from django.contrib.auth.decorators import login_required



# Create your views here.
#@login_required(login_url='user:login')
def cloudByKey(request):
    if request.method == "POST":
        xm = request.POST['xm']
        url = requests.post(
            f'https://tools.xmeye.net/deviceSuperPassword?text={xm}')
        html = bs(url.content, 'html.parser')
        dict = json.loads(html.get_text())
        return render(request, 'tools/cloud.html', {"dict":dict})

    return render(request, 'tools/cloud.html')

#@login_required(login_url='user:login')
def proByDate(request):
    day = datetime.datetime.now()
    return render(request, 'tools/pro.html', {"day":day})

def calculate_energy(voltage, current):
    """
    Розраховує кількість енергії в ватт-годинах (Wh)
    на основі значень напруги (вольтажу) та сили струму (амперажу).
    
    Параметри:
    voltage (float): Напруга (вольтах).
    current (float): Сила струму (амперах).
    
    Повертає:
    float: Кількість енергії в ватт-годинах (Wh).
    """
    energy = voltage * current
    return energy
