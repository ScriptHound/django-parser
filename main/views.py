from django.shortcuts import render, redirect
from django.http import HttpResponse
from djparser.celery import app

from .parser import get_parsed_data
from .queries import PIDQuery, ResultRowQuery
# Create your views here.


@app.task
def parse_task(url: str) -> str:
    return get_parsed_data(url)


def index(request):
    print(request.GET)
    context = {
        'status': request.GET.get('status'),
        'pid': request.GET.get('pid'),
        'saved_pids': PIDQuery.get_all_pids()
    }
    return render(request, 'index.html', context)


def parse(request):
    if request.method == 'POST':
        url = request.POST.get('lname')
        task = parse_task.delay(url)
        status = task.status
        pid = task.id
        PIDQuery.create(pid)
        return redirect(f'/?status={status}&pid={pid}')

    if request.method == 'GET':
        pid = request.GET.get('pid')
        result = app.AsyncResult(pid).result
        ResultRowQuery.create(result)

        context = {
            'result': result,
            'pid': pid
        }
        return render(request, 'results.html', context)
