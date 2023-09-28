from django.shortcuts import render
from django.views.generic import ListView
from . models import Event_Model
# Create your views here.

class Manage_Event(ListView):
    model = Event_Model
    template_name = 'events.html'