from django.urls import path
from . import views

urlpatterns = [
    
path('home/',views.home),
path('login/',views.login_view,name='login'),
path(' petowner/',views.petowner),
path(' shopowner/',views.shopowner),
path('registration/', views.registration_view, name='registration'),
path('shop_dashboard/', views.shop_dashboard, name='shop_dashboard'),
path('pet_dashboard/', views.pet_dashboard, name='pet_dashboard'),

    
]
