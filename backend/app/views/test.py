from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import JsonResponse


@require_http_methods(["GET", "POST"])
def test(request):
    response = {'msg': 1}
    return JsonResponse(response)