from django.db.models.query import QuerySet
from django.http.request import QueryDict
from .models import ResultIdModel, ResultRow


class PIDQuery:
    @staticmethod
    def create(pid: str) -> QueryDict:
        return ResultIdModel.objects.create(pid=pid)

    @staticmethod
    def get_all_pids() -> list:
        return ResultIdModel.objects.values_list('id', flat=True)

    @staticmethod
    def get_db_pid_by_id(id: str) -> str:
        return ResultIdModel.objects.get(id=id).pid

    @staticmethod
    def delete(pid: str) -> dict:
        return ResultIdModel.objects.filter(id=pid).delete()


class ResultRowQuery:
    @staticmethod
    def create(pid: ResultIdModel, **rows) -> None:
        results: list = []
        for k, v in rows.items():
            results.append(ResultRow(parent_id=pid, name=k, value=v))
        ResultRow.objects.bulk_create(results)

    @staticmethod
    def get_results_by_id(pid: str) -> QuerySet:
        return ResultIdModel.objects.get(id=pid).parent.all()

    @staticmethod
    def delete(name: str) -> dict:
        return ResultRow.objects.filter(name=name).delete()
