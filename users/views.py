# from audiofield.forms import CustomerAudioFileForm
# from audiofield.models import User
# from audiofield.widgets import CustomerAudioFileWidget
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PlaylistCreation

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан, {username}')
            print('Созданное имя пользователя :', username)
            return redirect('http://127.0.0.1:8000/profile/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваши изменения вступили в силу')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)

'''@login_required
def playlist(request):
   # form = CustomerAudioFileForm()

    # if request.method == 'POST':
    # form = CustomerAudioFileForm(request.POST, request.FILES)
     #   if form.is_valid():
      #      obj = form.save(commit=False)
       #     obj.user = User.objects.get(username=request.user)
        #    obj.save()
         #   return redirect('users/create_playlist.html')
#
 #       form.fields['audio_file'].widget = CustomerAudioFileWidget

    # audio = {'audio_form': form}


    return render(request, 'users/create_playlist.html')
    '''

@login_required
def create_playlist(request):
    current_tracks = []
    if request.method == 'POST':
        mus_form = PlaylistCreation(request.POST, request.FILES)

        if mus_form.is_valid() and str((request.FILES.get('track'))).endswith('.mp3'):
            buf = request.FILES.get('track')
            current_tracks.append(buf)
            mus_form.save()
            print(current_tracks)
            context = {'playlist': current_tracks}
            print(context)
            return render(request, 'users/create_playlist.html', context)
        elif not str((request.FILES.get('track'))).endswith('.mp3'):
            return 'Неподдерживаемый тип файла. Выберите файл формата .mp3'
    else:
         mus_form = PlaylistCreation()

    context = {'mus_form': mus_form}
    return render(request, 'users/create_playlist.html', context)

