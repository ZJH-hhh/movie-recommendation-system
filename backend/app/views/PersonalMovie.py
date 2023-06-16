from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import JsonResponse
from app.models import Movies, Details, NewUser
from django.core import serializers
import json


@require_http_methods(["GET", "POST"])
def PersonalMovie(request):
    response = {}
    user_id = request.GET.get('userid')
    movies_id = NewUser.objects.get(id=user_id).favor_movies
    movies_data = Movies.objects.filter(movie_id__in=movies_id)
    response['data'] = json.loads(serializers.serialize("json", movies_data))
    # print(movies_id, type(movies_id), movies_data)
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})