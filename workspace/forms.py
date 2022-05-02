from django import forms
from account.models import User
from novel.models import Node

class TailForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['memo']
        labels = {
            'memo':'메모'
        }

class StartForm(forms.ModelForm):
    class Meta:
        model = Node
        fields=['subject','content']
        labels = {
            'subject':'제목',
            'content':'내용',
        }