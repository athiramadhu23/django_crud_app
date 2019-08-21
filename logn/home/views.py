from django.shortcuts import render, redirect
import datetime
from .models import Student, Emp, Sigh
from .forms import StudentForm, EmpForm, SignForm
from twilio.rest import Client
import random


# Create your views here.
def login(request):
    return render(request, "index.html")

def second(request):
    x = datetime.datetime.now()
    y = x.strftime('%X')
    return render(request, "next.html", {"day": y})

def add(request):
    c= " "
    if request.method =="POST":
        a = request.POST.get("num1")
        b = request.POST.get("num2")
        c = int(a)+int(b)
    return render(request, "add.html", {'out': c})

def add_stud(request):
    st_form = StudentForm(request.POST)
    if request.method == "POST":
        if st_form.is_valid():
            st_form.save()
        return redirect(view_stud)
    return render(request, "add_student.html", {'form': st_form})


def view_stud(request):
    ob = Student.objects.all()
    return render(request, "view_student.html", {'obj': ob})


def delete(request, id):
    ob = Student.objects.get(id=id)
    ob.delete()
    return redirect(view_stud)

def emp(request):
    st_form = EmpForm(request.POST)
    if request.method == "POST":
        if st_form.is_valid():
            st_form.save()
        return redirect(view_emp)
    return render(request, "add_emp.html", {'form': st_form})

def view_emp(request):
    ob = Emp.objects.all()
    return render(request, "view_emp.html", {'obj': ob})

def emp_delete(request, id):
    ob = Emp.objects.get(id=id)
    ob.delete()
    return redirect(view_emp)

def stu_edit(request, id):
    obj = Student.objects.get(id=id)
    st_form = StudentForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if st_form.is_valid():
            st_form.save()
        return redirect(view_stud)
    return render(request, "add_student.html", {'form': st_form})


def emp_edit(request, id):
    obj = Emp.objects.get(id=id)
    st_form = EmpForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if st_form.is_valid():
            st_form.save()
        return redirect(view_emp)
    return render(request, "add_emp.html", {'form': st_form})

def sign(request):
    st_form = SignForm(request.POST)
    if request.method == "POST":
        if st_form.is_valid():
            st_form.save()
            otpp = random.randint(1000, 9999)

            request.session['otp1'] = otpp

            a = "ACaef2b82556926724afffcb345d6267ab"
            b = "22160875d22158c9289e24d61e2b8c49"
            abc = Client(a, b)
            abc.messages.create(from_="(209) 270-5686", to="+917994544534",
                                body="Your verification code is - " + str(otpp))


        return redirect(otp)
    return render(request, "signup.html", {'form': st_form})

def log(request):
    msg=""
    if request.method == "POST":
        a = request.POST.get("userid")
        b = request.POST.get("pwd")
        try:
            abc = Sigh.objects.get(email=a, pwd=b)
            if abc is not None:
                return redirect(login)
        except:
            msg = "Invalid user details....Try signUp"
    return render(request, "root.html", {'msg': msg})

def otp(request):
    msg=""
    if request.method == "POST":
        otp_got = request.session['otp1']
        a = request.POST.get("pwd")
        if int(a) == otp_got:
            return redirect(login)
        else:
            msg = "Invalid OTP......Try Again"
    return render(request, "otp.html", {'msg': msg})



"""
        a = request.POST.get("rollno")
        b = request.POST.get("name")
        c = request.POST.get("place")
        d = request.POST.get("dept")
        qw = Student(roll_no=a, name=b, place=c, dept=d)
        qw.save()
        """

