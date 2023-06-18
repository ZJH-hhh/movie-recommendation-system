from django.urls import path
from app.views.test import test
from app.views.write_data import data_clean, write_detais
from app.views.All_Data2Frontend import data2frontend, data_filter_by_tags, data_filter_by_id
from app.views.StoreMovie import StoreMovie
from app.views.UnStoreMovie import UnStoreMovie
from app.views.Recommend import Recommend, RandomRecommend

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.views.getinfo import InfoView
from app.views.register import RegisterView
from app.views.getMovie import MovieView
from app.views.assess import AssessView
from app.views.rank import RankView
from app.views.PersonalMovie import PersonalView
from app.views.comment import CommentView
from app.views.deleteComment import DeleteCommentView

urlpatterns = [
    path('test/', test),
    path('write_data/', data_clean),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_all_data/', data2frontend),
    path('write_details/', write_detais),
    path('get_data_by_tags/', data_filter_by_tags),
    path('get_data_by_id/', data_filter_by_id),
    path('getinfo/', InfoView.as_view(), name='getinfo'),
    path('register/', RegisterView.as_view(), name='register'),
    path('storemovie/', StoreMovie),
    path('unstoremovie/', UnStoreMovie),
    path('getmovie/', MovieView.as_view(), name='getmovie'),
    path('assess/', AssessView.as_view(), name='assess'),
    path('rank/', RankView.as_view(), name='rank'),
    path('personalmovie/', PersonalView.as_view(), name='personal'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('recommend/', Recommend),
    path('randomrecommend/', RandomRecommend),
    path('deletecomment/', DeleteCommentView.as_view(), name='deletecomment'),
]