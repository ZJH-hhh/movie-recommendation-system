from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movies, NewUser
import json
from django.core import serializers


class CommentView(APIView):
    def post(self, request):
        try:
            movieid = request.POST.get('movieid')
            userid = request.POST.get('userid')
            content = request.POST.get('content')
            user = NewUser.objects.get(id=userid)

            contents = user.contents
            contents.append({movieid: content})
            user.contents = contents
            user.save()
            
            return Response({
                'result': 'success',
                'data': user.contents,
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })