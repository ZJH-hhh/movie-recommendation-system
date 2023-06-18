from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movies, NewUser


class DeleteCommentView(APIView):
    def post(self, request):
        try:
            userid = request.POST.get('userid')
            movieid = request.POST.get('movieid')
            content = request.POST.get('content')

            user = NewUser.objects.get(id=userid)
            contents = user.contents
            contents.remove({movieid: content})
            user.contents = contents
            user.save()

            return Response({
                'result': 'success',
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })