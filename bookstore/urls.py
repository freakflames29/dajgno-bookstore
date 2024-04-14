from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="root"),
    path("new/",views.new,name='new'),
    path("create/",views.create,name='create'),
    path("book/<int:id>/",views.view_edit_delete,name='show'),
    path("book/<int:id>/delete/",views.delete,name='delete'),
    path("book/<int:id>/edit/",views.edit_and_update,name='edit'),


]