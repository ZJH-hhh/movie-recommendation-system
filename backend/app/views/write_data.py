import ast
from datetime import datetime
import csv
from app.models import Movies, Details, NewUser
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


@require_http_methods(["GET", "POST"])
def data_clean(request):
    with open('app/views/merged_file.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for line in reader:
            print(line)
            img_url = line['cover_url']
            movie_id = line['id']
            movie_types_list = ast.literal_eval(line['types'])
            movie_regions_list = ast.literal_eval(line['regions'])
            movie_title = line['title']
            movie_url = line['url']
            movie_score = line['score']
            release_time_str = line['release_date']
            if release_time_str:
                try:
                    movie_release_time = datetime.strptime(release_time_str, "%Y-%m-%d").date()
                except ValueError:
                    movie_release_time = datetime.strptime(release_time_str, "%Y").date()
            else:
                movie_release_time = None
            actor_count = line['actor_count']
            vote_count = line['vote_count']
            actors_list = ast.literal_eval(line['actors'])
            if line['introduction']:
                introduction = line['introduction']
            else:
                introduction = None
            if line['trailer_url']:
                trailer_url = line['trailer_url']
            else:
                trailer_url = None
            if line['comment_list']:
                comment_list = ast.literal_eval(line['comment_list'])
            else:
                comment_list = None
            # print(img_url, movie_url, movie_title, movie_id, movie_regions_list, movie_types_list, movie_score, movie_release_time, actors_list, actor_count, vote_count)

            movie = Movies(
                img_url=img_url,
                movie_id=movie_id,
                movie_type_list=movie_types_list,
                movie_regions_list=movie_regions_list,
                movie_title=movie_title,
                movie_url=movie_url,
                movie_score=movie_score,
                release_time=movie_release_time,
                actor_count=actor_count,
                vote_count=vote_count,
                actor_list=actors_list,
                introduction=introduction,
                trailer_url=trailer_url,
                comment_list=comment_list
            )
            movie.save()


@require_http_methods(["GET", "POST"])
def write_detais(request):
    response = {}
    with open('app/views/res.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for line in reader:
            movie_title = line['title']
            introduction = line['introduction']
            trailer_url = line['trailer_url']
            comment_list = ast.literal_eval(line['comment_list'])
            
            details = Details(
                video_url=trailer_url,
                introduction=introduction,
                movie_title=movie_title,
                comment=comment_list
            )
            details.save()
            
    response['message'] = 'success'
    return JsonResponse(response)


@require_http_methods(["GET", "POST"])
def test_write_movies(request):
    response = {}
    user = NewUser.objects.get(id=int(1))
    if user.favor_movies is None:
        user.favor_movies = []
    movieid = 654321
    user.favor_movies.append(movieid)
    user.save()
    response['message'] = 'success'
    return JsonResponse(response)