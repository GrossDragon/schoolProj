from django.contrib import admin
from matplotlib.pyplot import cla

# Register your models here.

from .models import Author, Book, Publisher, Pokupka


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #list_display = ("name", "author","publisher")
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    #list_display =("name",)
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
    #list_display=("name","last_name")


@admin.register(Pokupka)
class PokupkaAdmin(admin.ModelAdmin):
    pass
