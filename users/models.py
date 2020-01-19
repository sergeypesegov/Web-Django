# from audiofield.models import AudioFile
# from audiofield.widgets import CustomerAudioFileWidget
from django.db import models
from django.contrib.auth.models import User
from django.forms import FileField, ModelForm


class Playlist(models.Model):
    # playlist_name = models.CharField()
    track = models.FileField(upload_to='music')

class CurrentTracks(models.Model):
    tracks = models.ForeignKey(Playlist, on_delete=models.CASCADE)


class Profile(models.Model):
    # profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    music = models.ManyToManyField(Playlist, null=True)
    information = models.CharField(max_length=256, default='Расскажите о себе', name='Информация о пользователе')
    # information = models.TextField()
    # add personal information here

    def __str__(self):
        return f'Эта страничка принадлежит {self.user.username}'


































'''class AllTracks:
    track_id = models.AutoField(primary_key=True)
    track_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.track_id)


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # author_id =
    likes = models.IntegerField()
    dislikes = models.ImageField()
    # cur_tracks = models.ManyToManyField(AllTracks)


class CustomerAudioFileForm(ModelForm):
    audio_file = FileField(widget=CustomerAudioFileWidget)

    class Meta:
        model = AudioFile
        fields = ['name', 'audio_file']
        exclude = ('user',)
        '''
