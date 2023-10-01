from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer


# Create your views here.


def feedback(request):
    return render(request, 'feedback.html')

@csrf_exempt
def Feedback_list(request):
    if request.method == 'GET':
        api = Feedback.objects.all()
        serializer = FeedbackSerializer(api, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




        
    