from django.shortcuts import render, redirect
from .forms import UserForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

# 흐름: 초기 호출 시엔 GET method이므로 빈 form을 생성 후 render. 사용자가 빈 form을 채워서 POST method로 반환
# 이 때 form이 유효한 경우 db에 저장하고, 유효하지 않은 경우 해당 form을 그대로 render.
# 후자의 경우 form_errors.html에서 반환 받은 form의 에러를 확인 하고 에러 메세지 출력, 사용자는 유효하지 않은 form과 더불어 에러 메세지까지 보게 됨
# render: request, url, url에 전달할 변수 딕셔너리. 총 3개의 인자를 기반으로 html 파일에 템플릿 변수를 함께 넘겨주어 작동 시키는 역할
def signup_view(request):
    if request.method=='POST': # signup 초기 호출(get)에서 빈 form을 html로 넘겨준 뒤 입력을 받아(post) db에 사용자 등록
        form = UserForm(request.POST)
        #print(form)
        if form.is_valid():
            form.save()
            '''
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=raw_password)
            '''
            return redirect('account:login_view')
    else:
        form = UserForm()
    return render(request,'account/signup.html',{'form': form}) # view에서 넘겨준 변수를 가지고 templates(html) 내에서 다룰 수 있음, 템플릿 변수


def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('novel:index')

    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect('novel:index')