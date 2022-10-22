from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Firereport, Teams
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def new_request(request):
    if not request.user.is_authenticated:
        return redirect('dashboard')
    firereport = Firereport.objects.filter(Status__isnull=True)    
    return render(request,'admin/new_request.html',locals())

def reporting(request):
    error = ""
    if request.method == "POST":
        FullName = request.POST['FullName']
        MobileNumber = request.POST['MobileNumber']
        Location = request.POST['Location']
        Message = request.POST['Message']
        try:
            fire= Firereport.objects.create(FullName=FullName, MobileNumber=MobileNumber, Location=Location, Message=Message)
            fire.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'reporting.html', locals())

def delete_team(request,pid):
    if not request.user.is_authenticated:
        return redirect('index') 
    teams = Teams.objects.get(id=pid)
    teams.delete()           
    return redirect('manage-team')

def edit_team(request,pid):
    if not request.user.is_authenticated:
        return redirect('index') 
    teams = Teams.objects.get(id=pid) 

    error = '' 
    if request.method == 'POST':
        teamName = request.POST.get('teamName')
        teamLeaderName = request.POST.get('teamLeaderName')
        teamLeadMobno = request.POST.get('teamLeadMobno')
        teamMembers = request.POST.get('teamMembers')   

        teams.teamName = teamName
        teams.teamLeaderName = teamLeaderName
        teams.teamLeadMobno = teamLeadMobno
        teams.teamMembers = teamMembers

        try:
            teams.save()
            error = 'no'                                
        except:
            error = 'yes'              
    return render(request,'admin/edit_team.html',locals())

def manage_team(request):
    if not request.user.is_authenticated:
        return redirect('index') 
    teams = Teams.objects.all()           
    return render(request,'admin/manage_team.html',locals())

def add_team(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ''        
    if request.method == 'POST':
        teamName = request.POST.get('teamName')
        teamLeaderName = request.POST.get('teamLeaderName')
        teamLeadMobno = request.POST.get('teamLeadMobno')
        teamMembers = request.POST.get('teamMembers')   
        try:
            Teams.objects.create(teamName=teamName,teamLeaderName=teamLeaderName,
                                teamLeadMobno=teamLeadMobno,teamMembers=teamMembers)
            error = 'no'                                   
        except:
            error = 'yes'       
    return render(request,'admin/add_team.html',locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request,'admin/dashboard.html')

def admin_login(request):
    error = ''    
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                return redirect('dashboard')
                error = 'no'
        except:
            error = 'yes'

    return render(request,'admin_login.html')

def index(request):
    return render(request,'index.html')
