from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
import json
from django.core import serializers
from home import models
from home import forms

class Search(View):
    def get(self,req):
        Ss = req.GET['s']
        # print(Ss)

        studentData = models.student.objects.filter(name__iexact=Ss)
        # data = serializers.serialize("json", studentData)
        data=[]
        for i in studentData:
           tempData={
                "name":i.name,
                "email":i.email,
                "phone":i.phone,
                "batch":i.batch,
                "sid":i.sid,
                "stream":i.stream
            }
           data.append(tempData)
        return JsonResponse(data,safe=False)