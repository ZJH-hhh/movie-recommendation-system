from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movies
from django.core import serializers
import json


class MovieView(APIView):
    def get(self, request):
        try:
            title = request.GET.get('title')
            movie = Movies.objects.filter(movie_title=title)
            data = json.loads(serializers.serialize("json", movie))
            return Response({
                'result': 'success',
                'data': data,
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })