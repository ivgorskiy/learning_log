from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from users.forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from users.models import CustomUser
from learning_logs.models import Topic, Entry




# Create your views here.
def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = CustomUserCreationForm()

    else:
        # Обработка заполненной формы.
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнений входа и перенаправление на домашнюю страницу.
            login(request, new_user)

            return redirect('learning_logs:index')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def profile(request, user_id):
    """Страница профиля пользователя."""
    user = CustomUser.objects.get(id=user_id)

    if request.method != 'POST':
        form = CustomUserChangeForm(instance=user)
        context = {'form': form}
        return render(request, 'registration/profile.html', context)

    else:
        form = CustomUserChangeForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:index')


@login_required
def change_password(request, user_id):
    """Изменение пароля пользователя."""
    user = CustomUser.objects.get(id=user_id)

    if request.method != 'POST':
        form = CustomPasswordChangeForm(user=user)

    else:
        form = CustomPasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            user_save = form.save()
            # исключение аннулирования сеанса авторизации
            update_session_auth_hash(request, user_save)
            messages.success(request, 'You password was successfully updated!')
            return redirect('users:password', user_id=user.id)
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('users:password', user_id=user.id)

    context = {'form': form}
    return render(request, 'registration/change_password.html', context)


@login_required
def confirm_user_delete(request, user_id):
    """Страница подтверждения удаления аккаунта."""
    total_entries = 0               # всего заметок
    
    user = CustomUser.objects.get(id=user_id)
    topics = Topic.objects.filter(owner=request.user)
    total_topics = Topic.objects.filter(owner=request.user).count()
    
    for topic in topics:
        entries = Entry.objects.filter(topic=topic).count()
        total_entries += entries
    
    context = {
        'user': user,
        'total_entries': total_entries,
        'total_topics': total_topics
        }
    return render(request, 'confirm_user_delete.html', context)


@login_required
def user_delete(request, user_id):
    """Удаление аккаунта."""
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    
    return render(request, 'user_delete.html')
