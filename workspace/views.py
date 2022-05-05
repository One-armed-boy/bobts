from django.shortcuts import render, get_object_or_404, redirect
from novel.models import Node
from .forms import StartForm,TailForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
# Create your views here.


@login_required(login_url='account:login_view')
def index(request):
    head_list = Node.objects.filter(author=request.user, in_work_space=True, parent__isnull=True).order_by('-create_date')
    tail_list = Node.objects.filter(author=request.user, in_work_space=True, parent__isnull=False).order_by('-create_date')
    context={
        'head_list':head_list,
        'tail_list':tail_list,
             }
    return render(request,'workspace/work_list.html',context)

@login_required(login_url='account:login_view')
def start_detail(request,node_id):
    start=get_object_or_404(Node, pk=node_id)
    context={'start':start}
    return render(request,'workspace/start_detail.html',context)

@login_required(login_url='account:login_view')
def start_write(request):
    if request.method=='POST':
        form=StartForm(request.POST)
        if form.is_valid():
            start=form.save(commit=False)
            start.author=request.user
            start.create_date=timezone.now()
            #start.parent=''
            start.in_work_space=True
            #start.memo=''
            start.save()
            return redirect('workspace:start_detail',node_id=start.id)
    else:
        form=StartForm()
        return render(request,'workspace/start_create.html',{'form':form})

@login_required(login_url='account:login_view')
def node_modify(request,node_id):
    node=get_object_or_404(Node,pk=node_id)
    if request.user!=node.author:
        messages.error(request,f'{request.user}!={node.author}')
        return redirect('workspace:start_detail',node_id=node.id)
    if request.method=='POST':
        form=StartForm(request.POST,instance=node)
        if form.is_valid():
            node=form.save(commit=False)
            node.modified_date=timezone.now()
            node.save()
            return redirect('workspace:start_detail',node_id=node.id)
    else:
        form=StartForm(instance=node)
    context={'form':form}
    return render(request,'workspace/start_create.html',context)

@login_required(login_url='account:login_view')
def node_delete(request,node_id):
    node=get_object_or_404(Node,pk=node_id)
    if request.user!=node.author:
        messages.error(request,'삭제권한이 없습니다.')
        return redirect('workspace:start_detail',node_id=node.id)
    node.delete()
    return redirect('workspace:index')

@login_required(login_url='account:login_view')
def node_eject(request,node_id):
    node = get_object_or_404(Node, pk=node_id)
    if request.user != node.author:
        messages.error(request, '내보낼 권한이 없습니다.')
        return redirect('workspace:start_detail', node_id=node.id)
    node.in_work_space=False
    node.create_date=timezone.now()
    node.save()
    return redirect('workspace:index')


@login_required(login_url='account:login_view')
def tail_write(request,node_id):
    if request.method=='POST':
        form=TailForm(request.POST)
        if form.is_valid():
            tail=form.save(commit=False)
            tail.author=request.user
            tail.parent=Node.objects.get(id=node_id)
            tail.create_date=timezone.now()
            tail.in_work_space=True
            tail.save()
            return redirect('novel:node_detail',node_id=node_id)
    else:
        form=TailForm()
    return render(request,'workspace/tail_write.html',{'form':form})

@login_required(login_url='account:login_view')
def tail_detail(request,node_id):
    tail=get_object_or_404(Node,pk=node_id)
    context = {'tail': tail}
    return render(request, 'workspace/tail_detail.html', context)