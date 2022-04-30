from django.shortcuts import render
from novel.models import Node
# Create your views here.

def index(request):
    node_list =Node.objects._mptt_filter(parent__isnull=True,in_work_space=False).order_by('-create_date')
    context = {'node_list':node_list}
    return render(request, 'novel/node_list.html',context)