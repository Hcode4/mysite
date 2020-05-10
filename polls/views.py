# Create your views here.
from django.http import HttpResponse

import polls.connectRequest


def index(request):
    return HttpResponse(nice(request))


def nice(request):
    return HttpResponse("Hello world")


def webTest(request):
    # print(polls.connectRequest.getBaiduTest().text)
    return HttpResponse(polls.connectRequest.getBaiduTest().text)


def apiTest(request):
    return HttpResponse(polls.connectRequest.getHelloApi())

