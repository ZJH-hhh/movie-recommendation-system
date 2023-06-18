import random

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import JsonResponse
from app.models import Movies, Details, NewUser
from django.core import serializers
import json
from collections import defaultdict
import math
import pandas as pd


def compute_similarity(user_tag_counts, tag_combinations):
    similarity_matrix = []
    for movie_tag in tag_combinations:
        similarity_score = sum(movie_tag) / math.sqrt(len(user_tag_counts)) + math.sqrt(len(movie_tag))
        similarity_matrix.append(similarity_score)
        # print(len(user_tag_counts), len(movie_tag), sum(movie_tag))
    return similarity_matrix


@require_http_methods(["GET", "POST"])
def Recommend(request):
    response = {}
    user_id = request.GET.get('userid')
    if user_id == '0':
        data = Movies.objects.order_by('?')[:12]
        response['data'] = json.loads(serializers.serialize("json", data))
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    else:
        user_favor = NewUser.objects.get(id=int(user_id)).favor_movies
        if not user_favor:
            data = Movies.objects.order_by('?')[:12]
            response['data'] = json.loads(serializers.serialize("json", data))
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        # user_favor = ['1292052', '1291546']
        movies_list = Movies.objects.values('id', 'movie_id', 'movie_type_list')
        i = 0
        movies = defaultdict()
        for movie in movies_list:
            if movie['movie_id'] in movies:
                continue
            else:
                i += 1
                key = movie['movie_id']
                value = movie['movie_type_list']
                movies[key] = value

        # print(movies)
        # 计算用户收藏的标签组合频次
        user_tag_counts = {}
        for movie in user_favor:
            tags = movies[movie]
            for tag in tags:
                user_tag_counts[tag] = user_tag_counts.get(tag, 0) + 1

        tag_combinations = []
        for movie, tags in movies.items():
            combination = [user_tag_counts.get(tag, 0) for tag in tags]
            tag_combinations.append(combination)

        similarity = compute_similarity(user_tag_counts, tag_combinations)
        max_index = list(pd.Series(similarity).sort_values(ascending=False).index[:100])
        similarity = list(pd.Series(similarity).sort_values(ascending=False))[:12]
        random_movies = random.sample(max_index, 12)
        # response['data'] = similarity
        # response['index'] = max_index
        # response['len'] = str(i)
        # response['len_movie'] = str(len(movies))

        max_index_movie_id = list()
        for i in random_movies:
            # print(movies_list[i])
            movie_id = movies_list[i]['id']
            max_index_movie_id.append(movie_id)

        # response['movie_id'] = max_index_movie_id

        recommend_movies = Movies.objects.filter(id__in=max_index_movie_id)
        response['data'] = json.loads(serializers.serialize("json", recommend_movies))
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})



@require_http_methods(["GET", "POST"])
def RandomRecommend(request):
    response = {}
    data = Movies.objects.order_by('?')[:12]
    response['data'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})