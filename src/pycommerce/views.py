from django.db import connection
from django.http import JsonResponse


def healthz(_request):
    connection.ensure_connection()
    return JsonResponse({"status": "ok"})
