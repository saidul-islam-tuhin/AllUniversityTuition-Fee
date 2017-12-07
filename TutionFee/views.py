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
    context = {
        'u_cost': Cost.objects.filter(subject=subject),
        'divisions_list': divisions_list,
        'subject': subject,
    }
    return render(request, 'TutionFee/tuition.html', context)

def division_wise(request, subject, division):
    obj = cost_tu()
    obj.cse()
    context = {
        'subject': subject,
        'divisions_list': divisions_list,
        'division': division,
        'u_cost': Cost.objects.filter(subject=subject),
    }

    return render(request, 'TutionFee/tuition.html', context)
