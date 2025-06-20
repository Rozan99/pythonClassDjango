from django import forms
from .models import Todo

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'email', 'age', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
