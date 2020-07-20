from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from spinfo.models import sinfo

def main(request):
    return render(request, "main/메인-1.html")

def main_search(request):
    return render(request, "main/검색.html")

def main_post(request):
    return render(request, "main/게시글.html")

def main_template(request):
    return render(request, "main/기본 템플릿.html")

def main_interest(request):
    return render(request, "main/관심분야.html")

def main_profile(request):
    return render(request, "main/내프로필.html")

def main_ranking(request):
    return render(request, "main/실시간온도순위.html")

def main_alrim(request):
    return render(request, "main/알림.html")

def main_friend(request):
    return render(request, "main/친구목록.html")