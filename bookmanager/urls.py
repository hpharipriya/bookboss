from django.urls import path,include
from . import views

urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('book/borrow/id', views.register, name='register'),
]
