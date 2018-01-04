from django.shortcuts import render
from django.http import HttpResponse
from .scrapy import cost_tu
from .models import Cost,Information
from django.db.models import Q

divisions_list = ['Dhaka', 'Chittagong', 'Rajshahi', 'Barisal', 'Khulna',
                     'Mymensingh', 'Rangpur', 'Sylhet']
def home(request):
    subject_list = ['CSE', 'LLB', 'BBA', 'EEE', 'ENGLISH',]
    context = {
        'subject_list': subject_list,
        'All': 'All',
    }
    return render(request, 'TutionFee/home.html', context)

def subject_wise(request,subject):
    if request.GET.get('high'):
        u_cost = Cost.objects.filter(subject=subject).order_by("-cost")
        active="h"
    elif request.GET.get('low'):
        u_cost = Cost.objects.filter(subject=subject).order_by("cost")
        active="l"
    elif request.GET.get('normal'):
        u_cost = Cost.objects.filter(subject=subject)
        active="n"
    else:
        u_cost = Cost.objects.filter(subject=subject)
        active="none"
    context = {
        'u_cost': u_cost,
        'divisions_list': divisions_list,
        'subject': subject,
        'active': active,
    }
    return render(request, 'TutionFee/tuition.html', context)
def max_min(self,sub):
     if request.GET.get('high'):
         u_cost = Cost.objects.filter(subject=subject).order_by("-cost")
         active="h"
     elif request.GET.get('low'):
         u_cost = Cost.objects.filter(subject=subject).order_by("cost")
         active="l"
     elif request.GET.get('normal'):
         u_cost = Cost.objects.filter(subject=subject)
         active="n"
     else:
         u_cost = Cost.objects.filter(subject=subject)
         active="none"
     return self.u_cost
     return self.active

def division_wise(request, subject, division):
    obj = cost_tu()
    obj.cse()
    min_price = request.GET.get("lower")
    max_price = request.GET.get("higher")
    print("hb h",min_price)

    if request.GET.get('high'):
        u_cost = Cost.objects.filter(subject=subject).order_by("-cost")
        active="h"
    elif request.GET.get('low'):
        u_cost = Cost.objects.filter(subject=subject).order_by("cost")
        active="l"
    elif request.GET.get('normal'):
        u_cost = Cost.objects.filter(subject=subject)
        active="n"
    else:
        u_cost = Cost.objects.filter(subject=subject)
        active="none"
    if min_price or max_price:
        u_cost = Cost.objects.filter(subject=subject,cost__range=(int(min_price),int(max_price)))

    context = {
        'subject': subject,
        'divisions_list': divisions_list,
        'division': division,
        #'u_cost': Cost.objects.filter(subject=subject),
        'u_cost': u_cost,
        'active': active,
    }

    return render(request, 'TutionFee/tuition.html', context)

# max_min = Cost.objects.filter(subject=subject,cost__range=(min_price,max_price))
