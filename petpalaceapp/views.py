from django.shortcuts import render,redirect
from. models import*
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.



def home(request):
    return render(request,'petpalace/home.html')

def petowner(request):
    return render(request,'petpalace/petowner.html')
    
def shopowner(request):
    return render(request,'petpalace/shopowner.html')

def shop_dashboard(request):
    return render(request,'petpalace/shop_dashboard.html')

def pet_dashboard(request):
    return render(request,'petpalace/pet_dashboard.html')


def registration_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        data=request.POST.copy()

        try:
            user=User.objects.create_user(email=email,username=username,password=password)
        except Exception as e:
            print(e)
            return render(request, 'petpalace/registration.html')

        form=RegistrationForm(data)
        if form.is_valid():
            registration_instance = form.save(commit=False) 
            registration_instance.user = user
            registration_instance.save()
            return redirect('login')  
        else:
            print(form.errors)  
            return render(request, 'petpalace/registration.html')
    return render(request, 'petpalace/registration.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        print('working')
        print(request.POST)
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        print(email,password,user)
        if user is not None:
            login(request, user)
            if user.roll=='petowner':
                return redirect('pet_dashboard')
            else:
                return redirect('shop_dashboard')

        else:
            return render(request, 'petpalace/login.html', { 'error': 'Invalid login credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'petpalace/login.html')
