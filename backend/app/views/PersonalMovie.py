from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movies, NewUser
import json
from django.core import serializers


class PersonalView(APIView):
    def get(self, request):
        try:
            userid = request.GET.get('userid')
            method = request.GET.get('method')
            if method == '我的收藏':
                movies_id = NewUser.objects.get(id=userid).favor_movies
                movies_data = Movies.objects.filter(movie_id__in=movies_id)
                data = json.loads(serializers.serialize("json", movies_data))
                return Response({
                    'result': 'success',
                    'data': data
                })
            elif method == '我的评论':
                movies_data = NewUser.objects.get(id=userid).contents
                data = []
                for item in movies_data:
                    movieid = list(item.keys())[0]
                    content = list(item.values())[0]
                    movie = Movies.objects.get(movie_id=movieid)
                    data.append({
                        'movieid': movie.movie_id,
                        'movie_title': movie.movie_title,
                        'movie_photo': movie.img_url,
                        'content': content
                    })
                # movies_data = Movies.objects.filter(movie_id__in=movies_id)
                # res = json.loads(serializers.serialize("json", data))
            return Response({
                'result': 'success',
                'data': data
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })