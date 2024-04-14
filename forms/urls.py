
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("bookstore.urls")),
    path("auth/",include("authentication.urls"))
]
