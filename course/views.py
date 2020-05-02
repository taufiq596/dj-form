from django.shortcuts import render
from .models import Contact

# Create your views here.

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        desc = request.POST.get('desc','')
        contact= Contact(name=name, email=email, password=password, phone= phone, address= address, desc=desc)
        contact.save()

    return render(request, 'course/index.html')