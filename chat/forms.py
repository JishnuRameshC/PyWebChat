from django.forms import ModelForm
from .models import Room, User, UserProfile

class CustomUserChangeForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']




