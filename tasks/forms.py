from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={"placeholder": "ADD TASK"}))
    
    class Meta:
        model = Task
        fields = "__all__"
    
#the reason i used widget is because i wanted to display the placeholder
# when we use forms.CharField() directly, it has widget = forms.TextInput() by default in it which we dont need to mention, we can also use other widgets
# so its equivalent to writing title = forms.CharField(widget=forms.TextInput()), only specific to forms
