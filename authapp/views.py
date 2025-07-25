from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import logging


logger = logging.getLogger(__name__)

def login_page(request):
    return render(request, 'login.html')
