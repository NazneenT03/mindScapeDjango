from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:id>/',views.retrieve_update_acc),
    path('login/',views.login),
    path('signup/',views.signup),
    
]

