#urls.py
from django.urls import path
from . import views


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    path('', views.ytpList, name='ytpList'),



    ]
