from django.db import models
# from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.


class Topic(models.Model):
    """Тема, которую изучает пользователь."""
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 30:
            string = self.text
        else:
            string = f"{self.text[:30]}..."

        return string


class Entry(models.Model):
    """Информация, изученная пользователем по теме."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 50:
            string = self.text
        else:
            string = f"{self.text[:50]}..."

        return string
