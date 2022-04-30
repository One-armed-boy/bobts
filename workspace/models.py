'''
from django.db import models
from novel.models import Node
from account.models import User
# Create your models here.

class Work(models):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='work_author')
    parent = models.ForeignKey('self', null=True, blank=True, db_index=True, on_delete=models.CASCADE,
                            related_name='work_parent')
    content=
'''