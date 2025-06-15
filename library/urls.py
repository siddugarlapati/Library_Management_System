from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('profiles/', views.user_profile, name='user_profile'),
] 