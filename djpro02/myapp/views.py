from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("초기 요청 처리")

def helloFunc(request):
    msg = "장고 만세"
    ss = "<html><body>장고 프로젝트 구현 %s</body></html>"%msg
    return HttpResponse(ss)

def worldFunc(request):
    msg = "장고 처리 구조 이해"
    return render(request,'show.html',{'msg':msg}) # forward 방식이 기본