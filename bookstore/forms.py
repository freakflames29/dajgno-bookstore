from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields="__all__"
        labels={
            "bname":"Book Name",
            "author":"Author",
            "desc":"Some description about the book",
            "price":"Price",
            "amazon_link":"Amazon link"
        }