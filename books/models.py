from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length = 100, default = '*')
    author = models.CharField(max_length = 40, default = '*')
    release_date = models.IntegerField(default = 0 )
    number_of_pages = models.IntegerField(default = 0)
    short_description = models.TextField()
    published_at = models.DateTimeField()
    def __str__(self):
        return self.title
   # def __str__(self):
       # return self.author
