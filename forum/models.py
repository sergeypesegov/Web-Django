from django.db import models

# Create your models here.
class Post(models.Model):  # playlist ~ post
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # вывод информации об объекте - переопределенный
        return '{}'.format(self.title)
