from django.urls import path
from AutoCalApp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('top/', views.formView, name='formView'),
    path('top/', views.topView, name='topView'),
    path('result/', views.resultView, name='resultView'),
]
