from .models import UserInformation
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import PaymentGatewaySettings
from django.views import View


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def CheckoutSuccessView(request):
    return render(request, 'success.html')
>>>>>>> 933caffa1d92f86830ebe2d729eac2fdbe085094
from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserInformationSerializer,UserLoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

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

class DetailsUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer


'''class UserLoginView(APIView):
    def post(self, request, *args,**kwargs):
        seriallizer = UserLoginSerializer(data = request.data)

        if seriallizer.is_valid():
            username = seriallizer.validated_data['username']
            password = seriallizer.validated_data['password']

            user = authenticate(request,username = username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                 return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Invalid data
            return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)'''

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password) #, password=password
        if user is not None:
            login(request, user)  # Authenticate user and create session
            serializer =  UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogout(APIView):
    def post(self, request):
        logout(request)  # Logout user and destroy session
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    
class UserRegister(APIView):

    def post(self, request):
        data = request.data
        hashed_password = make_password(data['password'])
        new_object = User(username=data['username'], email = data['email'],password=hashed_password )
        new_object.save()
        return Response({'message': 'Object created successfully'}, status=status.HTTP_201_CREATED)
        

'''class UserLogout(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        request.user.auth_token.delete()  # Delete the user's token
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)'''
        


#curl -X POST -H "Authorization: Token YOUR_AUTH_TOKEN" http://localhost:8000/api/logout/