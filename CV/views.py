# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.conf.urls import include

def index(request):
	return HttpResponse("Hello World")
