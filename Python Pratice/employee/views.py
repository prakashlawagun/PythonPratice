from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return render(request, "base.html")

def employee(request):
    if request.method=='POST':
        data =request.POST
        email = data['email']
        password = data['password']
        context = {
       'name':email,
       'address':password
        }
    else:
        context = {
            'name':"Dinesh",
            'address':"Bagar"
        }
    return render(request,'employee.html',context)



