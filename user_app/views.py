from .models import UserInformation
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import PaymentGatewaySettings
from django.views import View


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def CheckoutSuccessView(request):
    return render(request, 'success.html')
from django.shortcuts import redirect, render


@method_decorator(csrf_exempt, name='dispatch')
def CheckoutFailedView(request):
    return render(request, 'failed.html')

def register(request):
    user_registration = None
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        amount = request.POST['amount']
        user_registration = UserInformation(username=username,email = email,mobile = mobile, role = role, amount=amount)
        user_registration.save()
        return redirect(sslcommerz_payment_gateway(request, amount))
        #print(username, email, mobile, role)
        user_registration = UserInformation(
            username=username, email=email, mobile=mobile, role=role)
        user_registration.save()
        return redirect('register')
        # print(username, email, mobile, role)
    return render(request, 'register.html')
