from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'callsign')


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ('Old_password', 'new_password1', 'new_password2')
