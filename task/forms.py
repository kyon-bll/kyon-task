from django import forms

from .models import Task

forms.DateInput.input_type = "date"
forms.DateTimeInput.input_type = "datetime-local" 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date',)
