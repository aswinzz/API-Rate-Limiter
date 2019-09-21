from django.shortcuts import render, redirect, reverse
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import RateLimits
import datetime
from django.utils import timezone

def RateLimitChecker(user,url,maxrate):
    ratelimitObj = RateLimits.objects.filter(user=user,url=url)
    count=1
    if(len(ratelimitObj)==0):
        ratelimitObj = RateLimits.objects.create(user=user,url=url,count=1,maxrate=maxrate)
    else:
        ratelimitObj=ratelimitObj[0]
        if(timezone.now() - ratelimitObj.lastupdated  < datetime.timedelta(days = 1)):
            if(ratelimitObj.count>=ratelimitObj.maxrate):
                response_data = {
                    "success":False,
                    "message":"Rate exceeded"
                }
                return response_data
            else:
                count=ratelimitObj.count+1
                ratelimitObj.count=count
                ratelimitObj.lastupdated=datetime.datetime.now()
                ratelimitObj.save()
        else:
            count=1
            ratelimitObj.count=1
            ratelimitObj.lastupdated=datetime.datetime.now()
            ratelimitObj.save()
    response_data={
        "success":True,
        "message":"Success",
        "count":count
    }
    return response_data

class ApiFirst(APIView):
    def post(self,request,format=None):
        maxrate=8
        url="1"
        response_data = RateLimitChecker(request.user,url,maxrate)
        return Response(response_data,status=status.HTTP_200_OK)

class ApiSecond(APIView):
    def post(self,request,format=None):
        maxrate=10
        url="2"
        response_data = RateLimitChecker(request.user,url,maxrate)
        return Response(response_data,status=status.HTTP_200_OK)