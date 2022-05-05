from django.shortcuts import render, get_object_or_404, redirect
from novel.models import Node
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    node_list =Node.objects.filter(parent__isnull=True,in_work_space=False).order_by('-create_date')
    context = {'node_list':node_list}
    return render(request, 'novel/node_list.html',context)

def detail(request,node_id):
    node=get_object_or_404(Node,pk=node_id)
    context={'node':node,'childlist':Node.objects.filter(parent=node,in_work_space=False)}
    return render(request,'novel/node_detail.html',context)

@login_required(login_url='account:login_view')
def vote(request,node_id):
    node=get_object_or_404(Node,pk=node_id)
    if request.user == node.author:
        messages.error(request,'자추는 불가능합니다.')
    else:
        node.voter.add(request.user)
    return redirect('novel:node_detail',node_id=node_id)