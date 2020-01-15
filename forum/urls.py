from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.post_list),  # func from views
    path('about/', views.about)
]