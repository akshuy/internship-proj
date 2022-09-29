from django.http import HttpResponse
from django.shortcuts import render



def aboutUS(request):
    return HttpResponse("you are at about us")
def course(request):
    return HttpResponse("you are at course")
def coursedetail(request,courseid):
    return HttpResponse(courseid)
def homepage(request):
    data = {
        'title': 'HomepagNew',
        'bdata' :"welcome to our website",
        'clist' : ['php','java','django'],
        'numbers' : [10,20,30,40,50],
        'student_detail' : [
            {'name' : 'akshay' , 'phone' : 6378176772 },
            {'name' : 'ajay' , 'phone' : 9694684245}
        ]
    }
    return render(request,"index.html",data)