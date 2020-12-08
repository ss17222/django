from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from mild.forms import *
from M2M3.settings import *
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from django.template.loader import render_to_string


class SignUp(View):
  
    def get(self, request):
        return render(request,"home.html")

    def post(self, request):
        params = request.POST
        print(params)
        form =SignUpForm(params)
        if form.is_valid():
            user = form.save()
            print("user: ", user.id)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = "http://"+str(current_site.domain) + \
                "/activate/"+str(user.id)
            print("message: ", message)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[user.email]
            )
            email.send() 
            user.set_password(params["password"])
            user.save()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return render(request, 'home.html', {'message': "User not created."})


class Activate(View):
    def get(self, request, uid):
        try:
            user =MyUser.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError,MyUser.DoesNotExist):
            user = None
        if user is not None and user.is_active == False:
            user.is_active = True
            user.is_staff = True
            user.save()
            return redirect("mild:login")
        else:
            return HttpResponse('Activation link is invalid!')


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        params = request.POST
        user = authenticate(email=params["email"], password=params["password"])
        if user is not None and user.is_active == True:
            login(request, user)
            return redirect("mild:dashboard")
        return render(request, "login.html", {"message": "user does not exists."})


class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            users =MyUser.objects.all()
            return render(request, 'dashboard.html', {"users": users})
        else:
            return redirect("mild:login")

 
class Delete(View):
    def get(self, request, uid):
        user =MyUser.objects.filter(id=uid).delete()
        return redirect("mild:dashboard")


class Edit(View):
    def get(self, request, uid):
        instance =MyUser.objects.get(id=uid)
        print(instance)
        return render(request, "edit.html", {"instance": instance,"uid":uid})

    def post(self, request, uid):
        instance =MyUser.objects.get(id=uid)
        print("instance: ", instance)
        print("request.POST: ", request.POST)
        form =EditForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            print("new data saved")
            return redirect("mild:dashboard")
        return redirect("mild:dashboard")


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, "login.html")

def forgot(request):
    para= request.POST
    print(para)
    form = ForgotForm(para) 
    if request.method=="POST":
        email = request.POST["email"]
        sumit=MyUser.objects.all()
        
        for i in sumit:
            if (email==i.email):
                abc = i.id
            
        print(abc)
        email=request.POST["email"]
        current_site= get_current_site(request)
        mail_subject='set your password'
        message = "http://"+str(current_site.domain) + "/forgoten/"+str(abc)
        print("message:", message)
        to_email =email
        email = EmailMessage(
                mail_subject, message, to=[email]
            )
        email.send()
        return HttpResponse('link has been sent to your mail to set password')
    else:
    
        return render(request,'forgot.html')


class Forgoten(View):
    def get(self, request, uid):
        try:
            user =MyUser.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError,MyUser.DoesNotExist):
            user = None
        if user is not None and user.is_active ==True:
            instance= MyUser.objects.get(id=uid)
            
            return render (request,"password.html",{"instance":instance,"uid":uid})
        else:
            return HttpResponse("Activation link is invalid")



            
    def POST(self, request, uid):
        instance=MyUser.objects.get(id=uid)
        password=request.POST["password"]
        instance.set_password(password)
        instance.save()
        return redirect("mild:login")

       




       
   
