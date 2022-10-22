from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Firereport, firereport
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def admin_login(request):
    error = ''    
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                return HttpResponse('dashboard')
                error = 'no'
        except:
            error = 'yes'

    return render(request,'admin_login.html')


def index(request):
    return render(request,'index.html')
