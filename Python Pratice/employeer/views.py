from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .forms import EmployeerForm
def employeer(request):
    if request.method == 'POST':
        form = EmployeerForm(request.POST)
        print(form.is_valid())
        data = form.cleaned_data
        print(data['email'])
    form = EmployeerForm()
    context = {
        'form':form
    }

    return render(request,'employeer/employeer.html',context)


