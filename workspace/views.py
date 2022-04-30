from django.shortcuts import render
from novel.models import Node
from .forms import WorkForm
# Create your views here.



def index(request):
    work_list=Node.objects._mptt_filter(author=request.user.nickname,in_work_space=True).order_by('-create_date')
    context={'work_list':work_list}
    return render(request,'workspace/work_list.html',context)

