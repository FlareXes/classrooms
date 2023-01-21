from django.shortcuts import render

from iod.models import Room


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, template_name="iod/home.html", context=context)


def classroom(request, pk):
    room = Room.objects.get(pk=pk)
    context = {'room': room}
    return render(request, template_name="iod/classroom.html", context=context)
