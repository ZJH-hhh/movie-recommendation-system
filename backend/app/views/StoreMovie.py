from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import JsonResponse
from app.models import Movies, Details, NewUser
from django.core import serializers
import json


@require_http_methods(["GET", "POST"])
def StoreMovie(request):
    response = {}
    movie_id = request.GET.get('movieid')
    user_id = request.GET.get('userid')
    if user_id:
        user = NewUser.objects.get(id=int(user_id))
        if user.favor_movies is None:
            user.favor_movies = []
        if movie_id in user.favor_movies:
            response['data'] = 'error'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        user.favor_movies.append(movie_id)
        user.save()
        response['data'] = 'success'
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    response['data'] = 'error'
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})