from django.shortcuts import render
from novel.models import Node
from .forms import WorkForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='account:login_view')
def index(request):
    work_list=Node.objects._mptt_filter(author=request.user.id,in_work_space=True).order_by('-create_date')
    context={'work_list':work_list}
    return render(request,'workspace/work_list.html',context)

