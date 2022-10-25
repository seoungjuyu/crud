from django.http import HttpResponse
from django.shortcuts import render
from .models import Article 

# Create your views here.

def index(request):
    return HttpResponse ("이거는 잘들어 올까요?")
    
    


def feed_create(request):
    if request.method == 'GET':
        return HttpResponse ("게시글 작성 페이지")