from .models import UserInformation
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import PaymentGatewaySettings
from django.views import View
from django.shortcuts import redirect, render
from django.db.models import Q


# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
def CheckoutSuccessView(request):
    return render(request, 'success.html')


@method_decorator(csrf_exempt, name='dispatch')
def CheckoutFailedView(request):
    return render(request, 'failed.html')


def register(request):
    user_registration = None
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        amount = request.POST['amount']
        user_registration = UserInformation(
            username=username, email=email, mobile=mobile, amount=amount)
        user_registration.save()
        return redirect(sslcommerz_payment_gateway(request, amount))
        # print(username, email, mobile, role)
        user_registration = UserInformation(
            username=username, email=email, mobile=mobile, role=role)
        user_registration.save()

        context = {
            'username': username,
            'email': email,
            'amount': amount,
            'Date': Date

        }
        return redirect('register')

        # print(username, email, mobile, role)
    return render(request, 'register.html')


def donation_report(request):
    donations = UserInformation.objects.all()
    for i in donations:
        print(i)
    return render(request, 'report_template.html', {'donations': donations})


def account(request):
    return render(request, 'account.html')


def history(request):

    if 'keyword' in request.GET:

        keyword = request.GET['keyword']

        if keyword:
            print(keyword)
            results_events = UserInformation.objects.filter(
                Q(email__icontains=keyword))

            # results_blogs = BlogModel.objects.filter(Q(title__icontains=keyword) | Q(body__icontains=keyword))
            print(results_events)
        if not keyword:

            return redirect('account')

    context = {

        'donations': results_events,

        # 'results_blogs':results_blogs

    }

    return render(request, 'report_template.html', context)
