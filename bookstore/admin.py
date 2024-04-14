from django.contrib import admin

# Register your models here.
from .models import Author,Book,Address

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Address)