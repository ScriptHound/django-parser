from django.db.models.query import QuerySet
from django.http.request import QueryDict
from .models import ResultIdModel, ResultRow


def save_pid(pid: str) -> QueryDict:
    return ResultIdModel.objects.create(pid=pid)


def save_parsing_results(pid: ResultIdModel, **rows) -> None:
    for k, v in rows.items():
        ResultRow.objects.create(parent_id=pid, name=k, value=v)


def get_all_pids():
    return [model.pid for model in ResultIdModel.objects.all()]


def get_results_by_id(pid: str) -> QuerySet:
    return ResultIdModel.objects.filter(pid=pid)[0].resultrow_set.all()