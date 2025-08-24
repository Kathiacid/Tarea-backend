from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('admin/', admin.site.urls),
]
