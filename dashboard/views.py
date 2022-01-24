from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from authapp.models import MCProfile, User
from grievance_data.models import Grievance
from dashboard.models import Desk
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core import serializers
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def colorDemo(request):
    desk = Desk.objects.all()
    grievance = Grievance.objects.all()
    return render(request,'muncipalDashboard.html',{'grievances':grievance})

def workSpace(request):
    return render(request,"WorkspaceDashboard.html")

def muncipalDashboard(request):
    grievance = Grievance.objects.all()
    return render(request,'muncipalDashboard.html',{'grievances':grievance})


def searchDemo(request):
    return render(request,'search-results.html')

def getDeskInfo(request):
    desk = Desk.objects.all()
    data = serializers.serialize('json',desk)
    return HttpResponse(data, content_type='application/json')

def loadDesk(request):
    mc_profile = MCProfile.objects.get(mc_user=request.user)
    desk_id = int(request.GET.get('desk_id').split("_")[1])
    desk = Desk.objects.get(id=desk_id)
    template = render_to_string('insideDesk.html', {'desk_single': desk})
    return JsonResponse({'data':template})

def grievance(request):
    return render(request,'grievance-detail.html')

def signin(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        # user = authenticate(username= email, password= password)
        user = auth.authenticate(email = mail, password = password)
        if user is not None:
            login(request, user)
            return redirect("dashboard:acdetail")
            
        else:
            return redirect("dashboard:register")
    return render(request,'sign-in.html')



def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('mail')
        username = request.POST.get('mail')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect("dashboard:search")
    
    return render(request,'sign-up.html')

def accountDetail(request):
    return render(request,'account-detail.html')

def accountSetting(request):
    return render(request,'account-setting.html')
    