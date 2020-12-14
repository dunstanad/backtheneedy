from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib import messages
from main.models import Contact



# Create your views here.
def index(request):
    return render(request,'base.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        sugg = request.POST.get("sugg")
        contact = Contact(name= name,email= email,phone= phone,sugg=sugg,date= datetime.today())        
        contact.save()
        messages.success(request, 'Your details are recorded. Thank-you')  
        return redirect('/')   
    return render(request,'main/contact.html')

def about(request):
    return render(request,'main/about.html')
