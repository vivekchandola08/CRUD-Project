from django.shortcuts import render
from django.http import HttpResponse

def showtest(request):
    que="Father of c language"
    a="Denis ritchie"
    b="vivek"
    c="utkarsh"
    d="gaurav"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    s=render(request,'exam/test.html',data)
    return(s)
def showresult(request):
    s="<h1>This is your result</h1>"
    return HttpResponse(s)
