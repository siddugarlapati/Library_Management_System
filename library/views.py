from django.shortcuts import render
from .models import Book, UserProfile

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def user_profile(request):
    profiles = UserProfile.objects.all()
    return render(request, 'library/user_profile.html', {'profiles': profiles}) 