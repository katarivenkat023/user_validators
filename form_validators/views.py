from django.shortcuts import render
from django.http import HttpResponse
from form_validators.forms import  *
# Create your views here.

def validatros_form(request):
    object_form = Name_Form()
    d={'form':object_form}
    if request.method == 'POST':
        FD=Name_Form(request.POST)
        if FD.is_valid():
          return HttpResponse(str(FD.cleaned_data))
        
    return render(request,'form_validators.html',d)
            


