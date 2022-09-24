from django.http import HttpResponse
from django.shortcuts import render



def aboutUS(request):
    return HttpResponse("you are at about us")
def course(request):
    return HttpResponse("you are at course")
def coursedetail(request,courseid):
    return HttpResponse(courseid)
def homepage(request):
    return render(request,"index.html")