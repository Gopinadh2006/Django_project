from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book  # this brings in your Book model

admin.site.register(Book)  # this tells Django to show it in the admin

