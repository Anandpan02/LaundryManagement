from random import randint
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from laundryapp.models import*

# Create your views here.
def index(request):
    data1 = About.objects.all()
    data = Price.objects.all()
    d = {'data': data}
    return render(request, "index.html", locals())

def user_dashboard(request):
    New = Laundry.objects.filter(status="New",user__user=request.user)
    Accept = Laundry.objects.filter(status="Accept",user__user=request.user)
    Inprocess = Laundry.objects.filter(status="Inprocess",user__user=request.user)
    Finish = Laundry.objects.filter(status="Finish",user__user=request.user)
    data = Price.objects.all()
    d = {'data': data}
    return render(request, "user_dashboard.html", locals())

def dashboard(request):
    New = Laundry.objects.filter(status="New")
    Accept = Laundry.objects.filter(status="Accept")
    Inprocess = Laundry.objects.filter(status="Inprocess")
    Finish = Laundry.objects.filter(status="Finish")
    data = Price.objects.all()
    d = {'data': data}
    return render(request, "dashboard.html", locals())

def user_signin(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(username=email, password=pwd)
        if user:
            if user.is_staff:
                messages.success(request, "Invalid User")
                return redirect('user_signin')
            else:
                login(request, user)
                messages.success(request, "User Login Successful")
                return redirect('user_dashboard')
        else:
            messages.success(request, "Invalid User")
            return redirect('user_signin')
    return render(request, "user_signin.html")

@login_required(login_url='/user_signin/')
def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('user_signin')

def user_signup(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        pwd = request.POST['password']

        user = User.objects.create_user(first_name=fullname, username=email, password=pwd)
        Register.objects.create(user=user, mobile=mobile)
        messages.success(request, "Register Successful")
        return redirect('user_signin')
    return render(request, "user_signup.html")

@login_required(login_url='/user_login/')
def user_profile(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']

        user = User.objects.filter(id=request.user.id).update(first_name=fullname, email=email)
        Register.objects.filter(user=request.user).update(mobile=mobile)
        messages.success(request, "Updation Successful")
        return redirect('user_profile')
    data = Register.objects.get(user=request.user)
    return render(request, "user_profile.html", locals())

@login_required(login_url='/user_login/')
def user_change_password(request):
    # user = User.objects.get(username=request.user.username)
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('user_change_password')
    return render(request,'user_change_password.html')

def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Admin Login Successful")
                return redirect('dashboard')
            else:
                messages.success(request, "Invalid User")
                return redirect('admin_login')
    return render(request, "admin_login.html")

@login_required(login_url='/admin_login/')
def change_password(request):
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('change_password')
    return render(request,'change_password.html')

@login_required(login_url='/admin_login/')
def admin_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('admin_login')

def laundry_request(request):
    if request.method == "POST":
        topwearqty = request.POST['topwearqty']
        bottomwearqty = request.POST['bottomwearqty']
        woolenclothqty = request.POST['woolenclothqty']
        other = request.POST['other']
        servicetype = request.POST['servicetype']
        pickupaddress = request.POST['pickupaddress']
        contactperson = request.POST['contactperson']
        description = request.POST['description']
        todate = request.POST['todate']

        user = Register.objects.get(user=request.user)
        Laundry.objects.create(topwearqty=topwearqty, bottomwearqty=bottomwearqty, user=user, woolenclothqty=woolenclothqty, other=other, servicetype=servicetype, pickupaddress=pickupaddress, contactperson=contactperson, description=description, todate=todate)
        messages.success(request, "Request Sent Successfully")
        return redirect('laundry_request')
    return render(request, "laundry_request.html", locals())

def requestlist(request):
    action = request.GET.get('action')
    data = Laundry.objects.filter()

    if request.user.is_staff:
        if action == "New":
            data = data.filter(status="New")
        elif action == "Accept":
            data = data.filter(status="Accept")
        elif action == "Inprocess":
            data = data.filter(status="Inprocess")
        elif action == "Finish":
            data = data.filter(status="Finish")
        return render(request, "view_request.html", locals())
    else:
        if action == "New":
            data = data.filter(status="New",user__user=request.user)
        elif action == "Accept":
            data = data.filter(status="Accept",user__user=request.user)
        elif action == "Inprocess":
            data = data.filter(status="Inprocess",user__user=request.user)
        elif action == "Finish":
            data = data.filter(status="Finish",user__user=request.user)
        return render(request, "user_view_request.html", locals())

def detail_request(request, pid):
    data = Laundry.objects.get(id=pid)
    price = Price.objects.filter().first()
    if request.method == "POST":
        status = request.POST['status']
        if data.status == "Inprocess":
            other_price = request.POST['other-price']
            total_price = request.POST['total_price']
            data.price = total_price
            data.other_price = other_price
        data.status = status
        data.save()
        messages.success(request, "Request Updated")
        return redirect('detail_request', pid)
    if request.user.is_staff:
        return render(request, "detail_request.html", locals())
    else:
        return render(request, "user_detail_request.html", locals())

@login_required(login_url='/admin_login/')
def view_reg_user(request):
    data = Register.objects.all()
    d = {'data': data}
    return render(request, "view_reg_user.html", locals())

@login_required(login_url='/admin_login/')
def view_laundry_price(request):
    data = Price.objects.all()
    d = {'data': data}
    return render(request, "view_laundry_price.html", locals())


@login_required(login_url='/admin_login/')
def delete_user_detail(request, pid):
    data = Register.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_reg_user')

@login_required(login_url='/admin_login/')
def delete_request(request, pid):
    data = Laundry.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('requestlist')

@login_required(login_url='/admin_login/')
def delete_laundry_price(request, pid):
    data = Price.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_laundry_price')

@login_required(login_url='/admin_login/')
def add_laundry_price(request):
    if request.method == "POST":
        topwearprice = request.POST['topwearprice']
        bottomwearprice = request.POST['bottomwearprice']
        woolenprice = request.POST['woolenprice']

        Price.objects.create(topwearprice=topwearprice, bottomwearprice=bottomwearprice, woolenprice=woolenprice,)
        messages.success(request, "Add Successful")
        return redirect('add_laundry_price')
    return render(request, "add_laundry_price.html", locals())

@login_required(login_url='/admin_login/')
def edit_laundry_price(request, pid):
    if request.method == "POST":
        topwearprice = request.POST['topwearprice']
        bottomwearprice = request.POST['bottomwearprice']
        woolenprice = request.POST['woolenprice']

        Price.objects.filter(id=pid).update(topwearprice=topwearprice, bottomwearprice=bottomwearprice, woolenprice=woolenprice)
        messages.success(request, "Updated Successful")
        return redirect('view_laundry_price')
    data = Price.objects.get(id=pid)
    return render(request, "edit_laundry_price.html", locals())

@login_required(login_url='/admin_login/')
def edit_about(request):
    if request.method == "POST":
        pagetitle = request.POST['pagetitle']
        description = request.POST['editor1']

        About.objects.filter(id=1).update(pagetitle=pagetitle, description=description)
        messages.success(request, "Updated Successful")
        return redirect('dashboard')
    data = About.objects.get(id=1)
    return render(request, "about.html", locals())

def between_dates(request):
    data = None
    fromdate = None
    todate = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        req = request.POST.get('reqtype')
        if req == "All":
            data = Laundry.objects.filter(todate__gte=fromdate, todate__lte=todate)
        else:
            data = Laundry.objects.filter(todate__gte=fromdate, todate__lte=todate, status=req)
        data2 = True
    return render(request, "between_dates.html",locals())

from django.db.models import Count
@login_required(login_url='/admin_login/')
def count_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        data = (Laundry.objects.filter(creationdate__date__gte=fromdate, creationdate__date__lte=todate).values('creationdate__date').annotate(dcount=Count('creationdate__date')).order_by())
        data2 = True
    return render(request, "count_report.html",locals())

