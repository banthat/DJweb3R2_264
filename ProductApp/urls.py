from django.urls import path
# from django.http import HttpResponse
from ProductApp import views

urlpatterns = [
    # path('', views.productapp_homepage, name='productapp_homepage'),
    path('testbt', views.testbt, name='testbt')
]