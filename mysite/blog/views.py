from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Msg
from .forms import MsgForm

# Create your views here.

def post_list(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', { 'post' : post })

def base(request):
    return render(request, 'base.html')

def inbox(request):
    msg = Msg.objects.all()
    return render(request, 'inbox_lst.html', { 'msgs' : msg })

def new(request):
    if request.method == 'GET':
        form = MsgForm()
        return render(request, 'msg_new.html', { 'form' : form })
    elif request.method == 'POST':
        form = MsgForm(request.POST)
        #falta salvar os dados no banco.

def show(request):
    msgs = Msg.objects.get(to=request.user)
    return HttpResponse('/inbox/')
