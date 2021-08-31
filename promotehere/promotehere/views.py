from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')

# def awebsites(request):
#     return render(request, 'awebsites.html')

# def apages(request):
#     return render(request, 'apages.html')

# def aothers(request):
#     return render(request, 'aothers.html')

# def promote(request):
#     return render(request, 'promote.html')

# def contactus(request):
#     if request.method=="POST":
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         phone = request.POST.get('phone', '')
#         desc = request.POST.get('desc', '')
#         contact = Contact(name=name, email=email, phone=phone, desc=desc)
#         contact.save()
#     return render(request, 'contactus.html')