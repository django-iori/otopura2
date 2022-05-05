from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import CreateView
import requests
import json
import http.client
import base64
import time
import hmac
import hashlib
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.middleware.csrf import get_token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import django_filters

@api_view(['POST'])
def signupview(request):
    if request.method=='POST':
        print(request.data)
        username_data=request.data["username"]
        print(username_data)
        password_data=request.data["password"]
        user=authenticate(request,username=username_data,password=password_data)
        if user is not None:
            return Response("userがすでに存在します")
        else:
            try:
                User.objects.create_user(username_data,'',password_data)
                user=authenticate(request,username=username_data,password=password_data)
                login(request,user)
                return Response("success")
                
            except:
                return Response("Something went wrong..")


@api_view(['POST'])
def loginview(request):
    if request.method=='POST':
        print(request.data)
        username_data=request.data["username"]
        print(username_data)
        password_data=request.data["password"]
        user=authenticate(request,username=username_data,password=password_data)
        if user is not None:
            login(request,user)
            print(request.user.username)
            return Response(data={'success':request.data})
            
        else:
            return Response(data={'error': 'エラーです'}, status=404)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        data = self.request.data
        print(data)
        username = data['username']
        password = data['password']

        try:
            user = authenticate(username=username, password=password)

            if username=="":
                print("first")
            elif user is not None:
                login(request, user)
                return Response({ 'success': 'User authenticated' })
            else:
                return Response({ 'error': 'Error Authenticating' })
        except:
            return Response({ 'error': 'Something went wrong when logging in' })


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            print(request.user)
            logout(request)
            return Response({ 'success': 'Loggout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        print('hello')
        return Response({ 'success': 'CSRF cookie set' })

@api_view(['GET'])
@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return Response({"details": "CSRF cookie set"})

"""@api_view(['GET'])
def CsrfView(request):
    return JsonResponse({'token': get_token(request)})
"""

@api_view(['GET'])
def CsrfView(request):
    response = HttpResponse()
    response.set_cookie('csrftoken', 'value')
    return response

@api_view(['GET'])
def HelloWorld(request):
    return Response({'message': 'hello world!'})


class MyPageView(APIView):
    def get(self, request, format=None):
        print(request.user)
        queryset = UserInfo.objects.filter(user=request.user)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class UploadListView(APIView):
    def get(self, request, format=None):
        print(request.user)
        queryset = BandModel.objects.filter(user=request.user)
        serializer = UploadListSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def authview(request):
    try:
        isAuthenticated = request.user.is_authenticated
        if isAuthenticated:
            return HttpResponse('success')
        else:
            return HttpResponse('failed')
    except:
        return HttpResponse('failed')

class CheckAuthenticatedView(APIView):
    def post(self, request, format=None):
        user = self.request.user
        print(user)
        try:
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                return Response('success')
            else:
                return Response('failed')
        except:
            return Response('failed')

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class Good_ListView(APIView):
    def get(self, request, format=None):
        queryset = GoodModel.objects.filter(user=request.user)
        serializer = GoodListSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def uploadview(request):
    if request.method=='POST':
        print(request.data)
        band = BandModel()
        band.user = request.user
        band.name = request.user.username
        band.age = request.data['age']
        print(request.data['part'])
        band.genre = request.data['genre']
        data = {
            'guitar': False,
            'base': False,
            'drum': False,
            'vocal': False,
            'keyboard': False
            }
        for key, value in json.loads(request.data['part']).items():
            if value:
                data[key]=value
        try:
            band.guitar = data['guitar']
            band.base = data['base']
            band.drum = data['drum']
            band.vocal = data['vocal']
            band.keyboard = data['keyboard']
        except:
            print('ok')
        band.image = request.data['image']
        band.save()
        return Response("success")

@api_view(['POST'])
def userinfoview(request):
    if request.method=='POST':
        print(request.data)
        user = UserInfo()
        user.user = request.user
        user.name = request.user.username
        user.age = int(request.data['age'])
        print(request.data['part'])
        user.genre = request.data['genre']
        user.address = request.data['address']
        user.artist = request.data['artist']
        part = ""
        for key, value in json.loads(request.data['part']).items():
            if value:
                part = part + key + " "
        print(part)
        user.part = part
        user.image = request.data['image']
        user.save()
        return Response("success")

@api_view(['POST'])
def goodview(request):
    #いいね数+1
    user = User.objects.get(pk=request.data['user'])
    band = BandModel.objects.get(user=user)
    band.good =band.good + 1
    band.save()

    model = UserInfo.objects.get(user=request.user)
    good = GoodModel()
    #いいねされた人,投稿
    good.user = user
    good.good_band = band
    #いいねした人
    good.good_user = request.user
    good.name = request.user.username
    good.age = model.age
    good.genre = model.genre
    good.address = model.address
    good.artist = model.artist
    good.part = model.part
    good.image = model.image
    good.save()
    return Response("Good!")

@api_view(['POST'])
def commentview(request):
    user = User.objects.get(pk=request.data['user'])
    band = BandModel.objects.get(user=user)
    cm = CommentModel()
    cm.cm_user = request.user
    cm.cm_band = band
    print(request.user.username)
    cm.cm_name = request.user.username
    cm.user = user
    cm.comment = request.data['comment']
    cm.save()
    return Response('comment!')

class Comment_ListView(APIView):
    def post(self, request, format=None):
        user = User.objects.get(pk=request.data['user'])
        queryset = CommentModel.objects.filter(user=user)
        serializer = CommentListSerializer(queryset, many=True)
        return Response(serializer.data)

class AccountView(APIView):
    def post(self, request, format=None):
        user = User.objects.get(pk=request.data['user'])
        queryset = UserInfo.objects.filter(user=user)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def edit_profile(request):
    try:
        print(request.data['part'])
        user = UserInfo.objects.get(pk=request.data['pk'])
        user.name = request.user.username
        user.age = request.data['age']
        user.genre = request.data['genre']
        user.address = request.data['address']
        user.artist = request.data['artist']
        user.part = request.data['part']
        user.image = request.data['image']
        user.save()
        return Response("Edit!")
    except:
        return Response("fail...")

class FilterBand(django_filters.FilterSet):
    guitar = django_filters.BooleanFilter(field_name='guitar')
    base = django_filters.BooleanFilter(field_name='base')
    drum = django_filters.BooleanFilter(field_name='drum')
    vocal = django_filters.BooleanFilter(field_name='vocal')
    keyboard = django_filters.BooleanFilter(field_name='keyboard')
    class Meta:
        model=BandModel
        fields = []

class BandView(APIView):
    def get(self, request):
        filterset = FilterBand(request.query_params, queryset=BandModel.objects.all())
        serializer = BandSerializer(instance=filterset.qs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def signoutview(request):
    print(request.user.pk)
    user = User.objects.get(pk=request.user.pk)
    user.delete()
    return Response("deleted!")

@api_view(['POST'])
def delete_upload(request):
    model = BandModel.objects.get(pk=request.data['id'])
    model.delete()
    return Response('deleted!')