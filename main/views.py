from django.shortcuts import render, redirect
from django.http import HttpResponse
from djparser.parser import get_parsed_data
from djparser.celery import app
# Create your views here.


@app.task
def parse_task(url: str) -> str:
    return get_parsed_data(url)


def index(request):
    print(request.GET)
    context = {
        'status': request.GET.get('status'),
        'pid': request.GET.get('pid')
    }
    return render(request, 'index.html', context)


def parse(request):
    if request.method == 'POST':
        url = request.POST.get('lname')
        task = parse_task.delay(url)
        status = task.status
        pid = task.id
        return redirect(f'/?status={status}&pid={pid}')

    if request.method == 'GET':
        pid = request.GET.get('pid')
        result = app.AsyncResult(pid).result

        context = {
            'result': result,
            'pid': pid
        }
        return render(request, 'results.html', context)
