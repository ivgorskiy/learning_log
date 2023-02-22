"""Определяет схемы URL для learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Редактирование темы
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Удаление темы
    path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Удаление записи
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
