from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from spinfo.models import sinfo

def loginmain(request):
    return render(request, "login/비로그인(최종).html")

def loginprocess(request):
    input_ID = request.POST["loginID"]
    input_PW = request.POST["loginPW"]
    users = sinfo.objects.all()
    for i in users:
        if i.get_id == input_ID:
            if i.PASSWORD == input_PW:
                return HttpResponse('login 성공')
            else :
                return HttpResponse('password error')
    return HttpResponse('일치하는 아이디가 없습니다.')