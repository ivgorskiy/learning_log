"""Определяет схемы URL для пользователей."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('register/', views.register, name='register'),
    # Страница пользователя
    path('<int:user_id>/profile/', views.profile, name='profile'),
    # Страница изменения пароля
    path('<int:user_id>/password/', views.change_password, name='password'),
    # Страница подтверждения удаления пользователя
    path('<int:user_id>/confirm_user_delete/', views.confirm_user_delete, name='confirm_user_delete'),
    # Удаление пользователя
    path('<int:user_id>/user_delete', views.user_delete, name='user_delete')
]
