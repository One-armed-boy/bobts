from django.db import models
from account.models import User
from mptt.models import TreeForeignKey,MPTTModel

# Create your models here.

class Node(MPTTModel):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='node_author')
    parent = TreeForeignKey('self',null=True,blank=True, db_index=True, on_delete=models.CASCADE,related_name='node_parent')
    subject = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='node_voter')
    in_work_space = models.BooleanField(default=True)
    memo = models.CharField(max_length=20, null=True, blank=True)
