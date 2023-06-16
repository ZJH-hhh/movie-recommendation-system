from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import JsonResponse
from app.models import Movies, Details, NewUser
from django.core import serializers
import json


@require_http_methods(["GET", "POST"])
def data2frontend(request):
    response = {}
    data = Movies.objects.all()[:36]
    response['data'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET", "POST"])
def data_filter_by_tags(request):
    response = {}
    data = Movies.objects.filter(movie_type_list__contains='历史')[:180]
    response['data'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET", "POST"])
def data_filter_by_id(request):
    response = {}
    movie_id = request.GET.get('id')
    data = Movies.objects.filter(movie_id=movie_id)
    response['data'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


