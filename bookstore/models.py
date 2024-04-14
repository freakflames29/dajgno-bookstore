from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Address(models.Model):
    add=models.CharField(max_length=20)
    author=models.OneToOneField(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.add


class Countries(models.Model):
    published=models.CharField(max_length=20)


class Book(models.Model):
    bname=models.CharField(max_length=20)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    desc =  models.TextField(max_length=100)
    price = models.IntegerField(default=0)
    amazon_link = models.CharField(max_length=150)
    published_countries=models.ManyToManyField(Countries,related_name='books')

