
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import loggin,logginNEW,otppass
from .forms import logginform,logginNEWform,otpvalidform
from .models import predictdata
from .forms import predictform
from .one import emailsent
import math, random

def compare(ss):
    import csv
    with open('covid.csv', 'r') as file:
        reader = csv.reader(file)
        a=[]
        for j,row in enumerate(reader):
            if j==0:
                continue
            s=''
            for i in row:
                if i=="YES":
                    s+='1'
                else:
                    s+='0'
            a.append(s)
        if ss in a:
            return True
        else:
            return False








def generateOTP():
    d="0123456789"
    otp=''
    
    for i in range(4):
        otp+=d[math.floor(random.random()*10)]
    return int(otp)

    

def loginpage(request):
    form = logginform()
    
    
    if request.method == "POST":
        form = logginform(request.POST)
        if form.is_valid():
            a=form.cleaned_data.get("usname")
            b=form.cleaned_data.get("pasword")
            try:
                aa=loggin.objects.get(usname=a)
                if aa.usname==a and aa.pasword==b:
                    
                    return HttpResponseRedirect("/predisplay")
                else:
                    raise IndentationError
            except:
                form = logginform()
                return render(request, 'demoapp1/insert.html', context={'form': form,'mes':'invalid user and password'})

    return render(request, 'demoapp1/index.html', context={'form': form})

def newpage(request):
    form=logginNEWform()
    if request.method == "POST":
        form = logginNEWform(request.POST)
        if form.is_valid():
            b=form.cleaned_data.get("primaryemail")
            global oo
            oo=generateOTP()
            emailsent(oo,b)
            return HttpResponseRedirect('/enterotp')
    return render(request, 'demoapp1/index1.html', context={'form': form})

def enterotp(request):
    form=otpvalidform
    if request.method == "POST":
        form = otpvalidform(request.POST)
        if form.is_valid():
            ae=form.cleaned_data.get("username")
            b=form.cleaned_data.get("password")
            c=form.cleaned_data.get("newpassword")
            d=int(form.cleaned_data.get("otp"))
            if b==c and d==oo:
                print("done")
                p=loggin(usname=ae,pasword=b)
                p.save()
            else:
                return render(request, 'demoapp1/input1.html', context={'form': form,'mes':'please enter the details properly'})

            
            return HttpResponseRedirect('/login')
    return render(request, 'demoapp1/input1.html', context={'form': form})





def predisplay(request):
    form = predictform()
    mes=''
    if request.method == "POST":
        form = predictform(request.POST)
        if form.is_valid():
            a0=form.cleaned_data.get("fever")
            a1=form.cleaned_data.get("breatheproblem")
            a2=form.cleaned_data.get("drycough")
            a3=form.cleaned_data.get("sorethroat")
            a4=form.cleaned_data.get("hypertension")
            a5=form.cleaned_data.get("abroadtravel")
            a6=form.cleaned_data.get("contact")
            a7=form.cleaned_data.get("publicplaceexposed")
            a8=form.cleaned_data.get("headache")
            a9=form.cleaned_data.get("lungspain")
            a10=form.cleaned_data.get("vaccine")
            a11=form.cleaned_data.get("boosterdose")
            ss=a0+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11
            q=compare(ss)
            n=ss.count("1")
            print(n)
            if q or n>=5:
                mes="u having covid please visit doctor"
            elif n<=3:
                mes='not having you are healthy'
            else:
                mes='not having you are healthy'
            

    return render(request, 'demoapp1/insert11.html', context={'form': form,'mes':mes})





