from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Promote
import datetime

def index(request):
    return render(request, 'index.html')

def awebsites(request):
    return render(request, 'awebsites.html')

def apages(request):
    return render(request, 'apages.html')

def aothers(request):
    return render(request, 'aothers.html')

def promote(request):
    if request.method=="POST":
        fullname = request.POST.get('fullname', '')
        user_email = request.POST.get('user_email', '')
        user_phone = request.POST.get('user_phone', '')
        user_promote = request.POST.get('user_promote', '')
        user_link = request.POST.get('user_link', '')
        website_1 = request.POST.get('website_1', '')
        website_2 = request.POST.get('website_2', '')
        page_1 = request.POST.get('page_1', '')
        page_2 = request.POST.get('page_2', '')
        user_image = request.FILES['user_image']
        user_moretext = request.POST.get('user_moretext', '')
        user_add = request.POST.get('user_add', '')
        promote = Promote(fullname=fullname, user_email=user_email, user_phone=user_phone, user_promote=user_promote, user_link=user_link, website_1=website_1, website_2=website_2, page_1=page_1, page_2=page_2,user_image=user_image, user_moretext=user_moretext, user_add=user_add)
        promote.save()
        #for redirecting form
        thank = True
        return render(request, 'promote.html',{'thank':thank})
        #ends
    return render(request, 'promote.html')


def payment(request):
    return render(request, 'payment.html')

def finalpayment(request):
    return render(request, 'finalpayment.html')

def contactus(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contactus.html')