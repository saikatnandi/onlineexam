from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ....qa...... index.")




def detail(request):
    return HttpResponse("Hello, world. You're at the qa..........details.... index.")