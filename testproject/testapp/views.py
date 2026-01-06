from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password,check_password
from .models import *
# Create your views here.
def home(request):
    sall=Student.objects.all()
    total_students=sall.count()
    total_cities=sall.values("city").distinct().count()
    context={
        "sall":sall,
        "total_students":total_students,
        "total_cities":total_cities,
    }
    return render(request,"testapp/index.html",context)
    # return render(request,"testapp/index.html")

def register(request):
    if request.POST:
        p_name=request.POST['name']
        p_email=request.POST['email']
        p_passsword=request.POST['password']
        p_subject=request.POST['subject']
        p_city=request.POST['city']
        student=Student.objects.filter(email=p_email).first()
        if student:
            return render(request,"testapp/registratioin.html",{"error":"email id already exists"})
        else:
            sid=Student.objects.create(
                name=p_name,
                email=p_email,
                password=make_password(p_passsword),
                subject=p_subject,
                city=p_city

            )
            send_mail(
                    subject="Registration Successfully",
                    message="congratulations your registration successfully compleated",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[p_email],
                    fail_silently=False

                )
                
        if sid:
            sall=Student.objects.all()
            total_students=sall.count()
            total_cities=sall.values("city").distinct().count()
            context={
                "sall":sall,
                "total_students":total_students,
                "total_cities":total_cities,

            }
            
            return render(request,"testapp/index.html",context)
        else:
            return render(request,"testapp/registratioin.html")
    else:
        return render(request,"testapp/registratioin.html")

def login(request):

    if request.POST:
        l_email=request.POST['email']
        l_password=request.POST['password'] 
        try:
            student=Student.objects.get(email=l_email)
            if student:
                if check_password(l_password,student.password) or student.password==l_password:
                    return redirect(student.subject)
                
                else:
                    return render(request,"testapp/login.html",{
                        "error":"Password Is Wrong"
                    })
        except:
            return render(request,"testapp/login.html",{
                "error":"email id is not registred please do registration"
            })
        
        
    
    return render(request,"testapp/login.html")

def forgot(request):
    if request.POST:
        f_email=request.POST['email']
        try:
            student=Student.objects.get(email=f_email)
            if student:
                return render(request,"testapp/change_pssword.html",{"email":f_email,"student":student})
        except:
            return render(request,"testapp/forgot.html",{"error":"Please Check Email Id "})
    return render(request,"testapp/forgot.html")


def change_password(request):
    if request.POST:
        new_password=request.POST['new_password']
        con_password=request.POST['confirm_password']
        c_email=request.POST['email']
        if new_password!=con_password:
            return render(request,"testapp/change_pssword.html",{"error":"Password Do Not Match","email":c_email})
        else:
            student=Student.objects.filter(email=c_email).first()
            student.password=make_password(new_password)
            student.save()
            return render(request,"testapp/change_pssword.html",{"msg":"Password Changed Successfully.. !Please Login Again"})


    return render(request,"testapp/change_pssword.html",{"email":"test@gmail.com"})

def delete(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        student=Student.objects.filter(email=email).first()
        if check_password(password,student.password):
            student.delete()
            return redirect('home')
        else:
            return render(request,"testapp/delete.html",{"error":"password not match"})
    return render(request,"testapp/delete.html")

def edit(request):
    if request.POST:
        email=request.POST['email']

        student=Student.objects.filter(email=email).first()
        if student:
            return render(request,"testapp/change_detail.html",{"email":email,"student":student})
        else:
            return render(request,"testapp/edit.html",{"error":"Email Is Not registered"})
        
    return render(request,"testapp/edit.html")

def change_detail(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        city=request.POST['city']
        subject=request.POST['subject']
        student=Student.objects.filter(email=email).first()
        if student:
            student.name = name
            student.city = city
            student.subject = subject
            student.save()

            return render(
                request,
                "testapp/change_detail.html",
                {
                    'email': email,
                    'student': student,
                    'msg': "Details changed successfully "
                }
            )
        else:
            return render(
                request,
                "testapp/change_detail.html",
                {
                    'error': "Student not found"
                }
            )
    
    return render(request,"testapp/change_detail.html")
def python(request):
    return render(request,"testapp/python.html")

def c(request):
    return render(request,"testapp/c.html")


def javascript(request):
    return render(request,"testapp/javascript.html")
def java(request):
    return render(request,"testapp/java.html")


def cpp(request):
    return render(request,"testapp/cpp.html")
def react(request):
    return render(request,"testapp/react.html")

def node(request):
    return render(request,"testapp/node.html")

def php(request):
    return render(request,"testapp/php.html")
def kotlin(request):
    return render(request,"testapp/kotlin.html")
def flutter(request):
    return render(request,"testapp/flutter.html")

