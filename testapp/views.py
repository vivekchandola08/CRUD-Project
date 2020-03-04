from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def Employee_data(request):
    employee=Employee.objects.all()
    res=render(request,'testapp/employee.html',{'employee':employee})
    return res
def greeting(request):
    s="<h1> this is greeting page </h1><p> This is landing page</p>"
    return HttpResponse(s)
def about(request):
    s='this is about page'
    return render(request,'testapp/about.html',{'s':s})
def showcontact(request):
    s="<h1>mobil-98888888888</h1>"
    s+="<h1>address-ims</h1>"
    return HttpResponse(s)
