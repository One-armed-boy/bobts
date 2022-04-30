from django import forms
from account.models import User
from novel.models import Node

class WorkForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['memo']
        labels = {
            'memo':'메모'
        }