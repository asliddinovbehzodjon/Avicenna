from django.shortcuts import render

# Create your views here.
from .models import FanTest,BlokTestlar
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serilizer import *
class FanTestView(APIView):
    def get(self,request,test_kodi,tel):
        result = FanTest.objects.filter(Q(test_kodi = test_kodi) & Q(tel=tel))
        serializer = FanTestSerializer(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class BlokTestlarView(APIView):
    def get(self, request, test_kodi, tel):
        result = BlokTestlar.objects.filter(Q(test_kodi=test_kodi) & Q(tel=tel))
        serializer = BlokTestlarSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CheckIt(APIView):
    def get(self,request,test_kodi):
        if FanTest.objects.filter(test_kodi = test_kodi).exists():
            return Response({"status":"OK"},status=status.HTTP_200_OK)
        else:
            return Response({"status": "BAD"}, status=status.HTTP_204_NO_CONTENT)
class CheckBlok(APIView):
    def get(self,request,test_kodi):
        if BlokTestlar.objects.filter(test_kodi = test_kodi).exists():
            return Response({"status":"OK"},status=status.HTTP_200_OK)
        else:
            return Response({"status": "BAD"}, status=status.HTTP_204_NO_CONTENT)




