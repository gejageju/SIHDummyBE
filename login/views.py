from django.shortcuts import render
from django.http import HttpResponse,request
from .models import User
from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import generics,status
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import serializers



# Create your views here.
def home(request):
    return render(request,'home.html')
class CreateUserview(APIView):
  
  def post(self,request,format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

def Viewdata(request):
    data = serializers.serialize('json',User.objects.all())
    return HttpResponse(data, content_type='application/json')  