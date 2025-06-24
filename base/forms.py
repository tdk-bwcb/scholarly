from django.forms import ModelForm, TextInput
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        widgets = {
            'name': TextInput(attrs={
                'autocomplete': 'off',
                'class': 'input',  # optional: add your input class if styling is needed
            }),
        }
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
