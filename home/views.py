from django.shortcuts import render
from events.models import Event_Model
from feedback.models import Feedback
# Create your views here.


def home(request):
    finished_events = Event_Model.objects.filter(is_finished=False)
    news = Event_Model.objects.filter(is_finished=True)
    data=Feedback.objects.all()
    return render(request, 'home/index.html', {'events': finished_events, 'all_news': news, 'data':data})
