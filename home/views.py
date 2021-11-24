from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse,HttpRequest
from home import models
from home import forms

class Home(View):
    def get(self,req):
        studentData=models.student.objects.all()
        return render(req,"index.html",{"data":studentData})

    def post(self,req):
        # name = req.POST['name']
        # email = req.POST['email']
        # phone = req.POST['phone']
        # batch = req.POST['batch']
        # sid = req.POST['sid']
        # stream = req.POST['stream']
        # models.student(name=name,email=email,phone=phone,batch=batch,sid=sid,stream=stream).save()
        studentData = forms.StudentForm(req.POST)
        if studentData.is_valid():
            studentData.save()
        return redirect("/")


class Search(View):
    def get(self,req):
        Ss=req.GET['s']
        # print(Ss)
        data=models.student.objects.filter(name__iexact=Ss)
        # if(data is not None):
        #     return render(req,"index.html",{"data":data,"val":1})
        return render(req,"index.html",{"data":data})