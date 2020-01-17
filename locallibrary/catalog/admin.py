from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language
#app 'catalog' has model.py file
#classes defined in model.py = Author, Genre, Book, BookInstance

#register these classes
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
