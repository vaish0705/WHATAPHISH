from django.urls import path
from . import views
urlpatterns=[
    path('', views.enter, name='URL') ,
    path('home/',views.home, name='home'),
    path('signup/',views.login,name='signup'),
]