from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # information = models.TextField(default='Расскажите о себе', upload_to='')
    # add personal information here

    def __str__(self):
        return f'Эта страничка принадлежит {self.user.username}'