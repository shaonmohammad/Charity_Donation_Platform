from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Feedback
from blog.models import BlogModel
from feedback.serializers import FeedbackSerializer
from django.contrib import messages
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

# Create your views here.


def feedback_form(request):
 
    print(request.POST)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        feedback_temp = Feedback(name=name, email = email,comment = comment)
        feedback_temp.save()
        print(name, email, comment)
        # messages.success(request, 'Thank you for Feedback')
        return redirect('Blog')
    return render(request, 'feedback.html')

# def feedback_show(request):
#     show_data = Feedback.objects.all()
#     print(show_data)
#     return render(request,'index.html', {'show_data' : show_data})

def feedback_show(request):
    show_data = Feedback.objects.all()
    return render(request, 'home', {'show_data' : show_data})


# def feedback_data(request):
#     print(request.post)
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         comment = request.POST['comment']
#         feedback_temp = Feedback(name=name, email = email,comment = comment)
#         feedback_temp.save()
#         print(name, email, comment)
#         # messages.success(request, 'Thank you for Feedback')
#         return redirect('Blog.html')
#     return render(request,'blog_detailed.html')

# @csrf_exempt
# def Feedback_list(request):
#     if request.method == 'GET':
#         api = Feedback.objects.all()
#         serializer = FeedbackSerializer(api, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = FeedbackSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)





class Feedback_list(ListAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer


class Create(CreateAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    
class Delete_item(DestroyAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    
class UpdateItem(UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer




        
    