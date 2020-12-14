from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import OrgData
from django.core.mail import send_mail
from math import ceil, floor
import requests

# Create your views here.
def handleregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('/')
        form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def handlelogin(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('/')
            '''
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'accounts/login.html', {'form': form})
            '''
    #else:
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('/')
   

def org_reg(request):
    allOrgObj = OrgData.objects.values('id' ,'name','email','contact','address','city','pincode', 'myfile','urgent','need_desc','bank_acc','bank_ifsc','upi_id')
    if request.method == 'POST':
        # id = worker_id()
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']
        urgent = request.POST['urgent_need']
        need_desc = request.POST['need_desc']
        myfile= request.FILES.get('myfile')
        bank_acc = request.POST['bank_acc']
        conf_bank_acc = request.POST['conf_bank_acc']
        bank_ifsc = request.POST['bank_ifsc']
        upi_id = request.POST['upi_id']
        filesystem = FileSystemStorage()
        filename = filesystem.save(myfile.name, myfile)
        uploaded_file_url = filesystem.url(filename)




        if OrgData.objects.filter(email=email).exists():
            messages.info(request,"You have already registered in our site as an Organisation, You can not have more than 1 account. ")
            return redirect('/')

        elif bank_acc != conf_bank_acc:
            messages.info(request,"Bank accounts not matching")

                   
        else:
            org_reg = OrgData(name=name, email=email, contact=contact,address=address, city=city, pincode=pincode,
             myfile=myfile,urgent=urgent,need_desc=need_desc,bank_acc=bank_acc,bank_ifsc=bank_ifsc,upi_id=upi_id)
            org_reg.save()
            print('Data Saved')
        # return render(request, 'org_reg.html', {'uploaded_file_url': uploaded_file_url})
            messages.info(request, "You have Successfully registered as Organisation in our site!")
            org_prev_registered = 1
            return redirect('/')
    return render(request, 'accounts/org_reg.html', {'allOrgObj':allOrgObj})


def food_new_search(request):

    search = request.POST.get('search')
    print(search)
    od = OrgData.objects.all().filter(pincode=search,urgent='Food')
    return render(request,'accounts/food.html',{'od':od})


def edu_new_search(request):

    search = request.POST.get('search')
    print(search)
    od = OrgData.objects.all().filter(pincode=search,urgent='Education')
    return render(request,'accounts/edu.html',{'od':od})


def cloth_new_search(request):

    search = request.POST.get('search')
    print(search)
    od = OrgData.objects.all().filter(pincode=search,urgent='Clothing')


    return render(request,'accounts/cloth.html',{'od':od})



