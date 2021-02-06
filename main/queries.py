from django.db.models.query import QuerySet
from django.http.request import QueryDict
from .models import ResultIdModel, ResultRow


class PIDQuery:
    @staticmethod
    def create(pid: str) -> QueryDict:
        return ResultIdModel.objects.create(pid=pid)

    @staticmethod
    def get_all_pids() -> list:
        return [model.pid for model in ResultIdModel.objects.all()]

    @staticmethod
    def delete(pid: str) -> dict:
        return ResultIdModel.objects.filter(pid=pid).delete()


class ResultRowQuery:
    @staticmethod
    def create(pid: ResultIdModel, **rows) -> None:
        for k, v in rows.items():
            ResultRow.objects.create(parent_id=pid, name=k, value=v)

    @staticmethod
    def get_results_by_id(pid: str) -> QuerySet:
        return ResultIdModel.objects.get(pid=pid).resultrow_set.all()

    @staticmethod
    def delete(name: str) -> dict:
        return ResultRow.objects.filter(name=name).delete()
