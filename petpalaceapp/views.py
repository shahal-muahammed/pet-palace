from django.shortcuts import render
from. models import*

# Create your views here.


def home(request):
    data=petowner_registration.objects.all()
    return render(request,'petpalace/index.html',context={"Data":data})
    