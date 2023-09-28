from django.shortcuts import render
from django.views.generic import ListView
from . models import EventsModel
# Create your views here.

class Manage_Event(ListView):
    model = EventsModel
    template_name = 'home.html'