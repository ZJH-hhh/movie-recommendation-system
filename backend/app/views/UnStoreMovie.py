from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import JsonResponse
from app.models import Movies, Details, NewUser
from django.core import serializers
import json


@require_http_methods(["GET", "POST"])
def UnStoreMovie(request):
    response = {}
    movie_id = request.GET.get('movieid')
    user_id = request.GET.get('userid')
    if user_id:
        user = NewUser.objects.get(id=int(user_id))
        movie_index = user.favor_movies.index(movie_id)
        # print(user.favor_movies[movie_index])
        user.favor_movies.pop(movie_index)
        user.save()
        response['data'] = 'success'
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    response['data'] = 'error'
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})