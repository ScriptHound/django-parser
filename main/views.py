from django.shortcuts import render, redirect
from django.http import HttpResponse
from djparser.parser import get_parsed_data
from djparser.celery import app
# Create your views here.

@app.task
def parse_task(url: str) -> str:
    return get_parsed_data(url)


def index(request, status=None):
    context = {
        'status': status
    }
    return render(request, 'index.html', context)


def parse(request):
    if request.method == 'POST':
        url = request.POST.get('lname')
        status = parse_task.delay(url).status
        return redirect('/index', status=status)
