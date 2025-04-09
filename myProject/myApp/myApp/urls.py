from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addtask/', views.addtask, name='addtask'),
    path('journal/', views.journal, name='journal'),
    path('forgotpassword/', views.signup, name='forgotpassword'),
    # Add others accordingly
]