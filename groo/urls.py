from django.contrib import admin
from django.urls import path
from groo import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('formsignup',views.formsignup,name='formsignup'),
    path('formlogin',views.formlogin,name='formlogin'),
    path('question',views.question,name='question'),
    path('addquestion',views.addquestion,name='addquestion'),
    path('showanswers',views.showanswers,name='showanswers'),
    path('addans',views.addans,name='addans'),
    path('anssubmit',views.anssubmit,name='anssubmit'),
    path('home',views.home,name='home')
]
