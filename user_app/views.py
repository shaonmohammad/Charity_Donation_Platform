from django.shortcuts import render,redirect
from .models import UserInformation

# Create your views here.

def register(request):
    user_registration = None
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        user_registration = UserInformation(username=username,email = email,mobile = mobile, role = role)
        user_registration.save()
        return redirect('home')
        #print(username, email, mobile, role)
    return render(request, 'register.html')
