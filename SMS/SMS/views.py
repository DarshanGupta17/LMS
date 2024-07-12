from django.shortcuts import redirect,render,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_typ = user.user_type
            if user_typ == '1':
                return redirect('hod_home')
            elif user_typ == '2':
                return redirect('staff_home')
            elif user_typ == '3':
                return redirect('Student_Home')
            else:
                messages.error(request,"Email and Password are Invalid !")
                return redirect('Login')
        else:
            messages.error(request,"Email and Password are Invalid !")
            return redirect('Login')
        
def doLogout(request):
    logout(request)
    return redirect('Login')

@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    cntxt = {
        "user":user,
    }
    return render(request,'profile.html',cntxt)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            if profile_pic != None and profile_pic != "":
               customuser.profile_pic = profile_pic

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request,"Your Profile Updated Successfully.")
            return redirect('profile')
        except:
            messages.error(request,"Failed to Update Your Profile.")
    return render(request,'profile.html')