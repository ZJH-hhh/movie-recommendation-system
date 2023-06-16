from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movies


class AssessView(APIView):
    def post(self, request):
        try:
            movieid = request.POST.get('movieid')
            score = float(request.POST.get('score'))
            movie = Movies.objects.get(movie_id=movieid)

            cur = movie.score
            cnt = movie.assess_count
            cur += score
            cnt += 1

            movie.score = cur / cnt
            movie.assess_count = cnt
            movie.save()

            return Response({
                'result': 'success',
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })