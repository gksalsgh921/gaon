from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import sinfo

def spinfo(request):
    return render(request, "spinfo/개인정보.html")

def register(request):
    user_input_ID= request.POST["my_id"]
    user_input_NAME=request.POST["my_name"]
    user_input_PW=request.POST["my_pw"]
    user_input_EMAIL=request.POST["email"]
    new_IDPW = sinfo(get_id =user_input_ID ,NAME =user_input_NAME, PASSWORD=user_input_PW, EMAIL=user_input_EMAIL,  )
    new_IDPW.save()
    context = {
        'put_id' : user_input_ID
    }
    return render(request, "spinfo/회원상세정보.html", context)

def register_complete(request):
    input_user_id =request.POST['user_id']
    input_job=request.POST['job']
    input_school = request.POST['a_b']
    input_local = request.POST['home']
    input_status = request.POST['marige']
    input_intro = request.POST['self_intro']
    input_checkbox =request.POST['interest']
    input_check=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(input_checkbox)):
        if input_checkbox[i]!='NULL':
            input_check[i]=50
    user = sinfo.objects.get(get_id = input_user_id)
    user.JOB=input_job
    user.SCHOOL = input_school
    user.LOCATION = input_local
    user.STATUS = input_status 
    user.INTRO = input_intro
    user.ENT=input_check[0]
    user.SPT=input_check[1]
    user.CAR=input_check[2]
    user.TEC=input_check[3]
    user.ECN=input_check[4]
    user.FOOD=input_check[5]
    user.TRIP=input_check[6]
    user.HTH=input_check[7]
    user.BIS=input_check[8]
    user.FNB=input_check[9]
    user.ANP=input_check[10]
    user.GROW=input_check[11]
    user.HUMOR=input_check[12]
    user.CNM=input_check[13]
    user.save()
    return redirect('http://127.0.0.1:8000')