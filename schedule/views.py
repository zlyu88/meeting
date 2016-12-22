from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import User, Room
from .forms import LogIn


def log_in(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(name=form.cleaned_data['name'],
                                        password=form.cleaned_data['password'])
                user.is_logged = True
                user.save()
                url = reverse('base', kwargs={'uid': user.id})
                return HttpResponseRedirect(url)
            except User.DoesNotExist:
                return HttpResponseRedirect('/schedule/log_in/')
    else:
        form = LogIn()
    return render(request, 'login.html', {'form': form})


def base(request, uid=None):
    users = User.objects.all()
    rooms = Room.objects.all()
    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        user = None
    context = {'user': user, 'users': users, 'rooms': rooms}
    return render(request, 'index.html', context)


def room_page(request, rid):
    room = Room.objects.get(id=rid)
    users = User.objects.all()
    context = {'users': users, 'room': room}
    return render(request, 'room_page.html', context)


def test(request, uid):
    return HttpResponse('link works with id: %s' % uid)
