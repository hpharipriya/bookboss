from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .models import Borrow, Book
import json
def register(request,response):
    user = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    User = settings.AUTH_USER_MODEL.save()
    obj = User.objects.create(username=user, password=password, email=email)
    obj.save()
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user,password=password)
        login(request,user)
        token = Token.objects.get_or_create(user=user)
        token_val = token[0]
        res = {"action":"success","token":token_val}
        #data = serializers.serialize('json',res)
        return JsonResponse(res)
        #return HttpResponse(data, content_type="application/json")

@csrf_exempt
@permission_classes((IsAuthenticated,))
def borrow_book(request):
    if request.method == 'POST':
        book = request.POST['book']
        user = request.user
        bookObj = Book.objects.get(book_name= book)
        bookObj.count -= 1
        bookObj.save()
        borrow_val = Borrow.objects.create(book=bookObj,user=user)
        

@permission_classes((IsAuthenticated,))
def borrow_book(request):
    if request.method == 'POST':
        book = request.POST['book']
        user = request.user
        bookObj = Book.objects.get(book_name= book)
        bookObj.count -= 1
        bookObj.save()
        borrow_val = Borrow.objects.create(book=bookObj,user=user)


    