# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from .models import Photo


def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'photos': photos})

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.photo_set.all().order_by('-created_at')
    return render(request, 'app/users_detail.html', {'user': user, 'photos': photos})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # 入力された値からUserインスタンスを作成
        if form.is_valid():
            new_user = form.save()  # ユーザーインスタンスを保存
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})
