from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movies
import json
from django.core import serializers


class RankView(APIView):
    def get(self, request):
        try:
            tag = request.GET.get('tag')
            print(tag)
            if tag != 'all':
                movies = Movies.objects.filter(movie_type_list__contains=tag)[:50]
                data = json.loads(serializers.serialize("json", movies))
                return Response({
                    'result': 'success',
                    'data': data,
                })
            else:
                movies = Movies.objects.all()[:50]
                data = json.loads(serializers.serialize("json", movies))
                return Response({
                    'result': 'success',
                    'data': data,
                })
        except Exception as e:
            return Response({
                'result': str(e)
            })