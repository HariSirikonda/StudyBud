from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

rooms = [
    {"id" : 1, "name" : "Hari Kiran"},
    {"id" : 2, "name" : "Hari Kiran"},
    {"id" : 3, "name" : "Hari Kiran"},
    {"id" : 4, "name" : "Hari Kiran"},
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def cerateRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)