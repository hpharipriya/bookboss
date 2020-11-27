from django.db import models
from django.conf import settings

class Book(models.Model):
    book_name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.book_name
    
class Borrow(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.book_name
