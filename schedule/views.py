from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import User, Room
from .forms import LogIn


#
