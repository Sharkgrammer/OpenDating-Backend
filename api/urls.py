from django.urls import path

from api.views.function_views.feed import get_feed
from api.views.model_views.like import LikeView
from api.views.model_views.stat import StatView
from api.views.model_views.user import UserView
from api.views.model_views.interest import InterestView

app_name = "api"
urlpatterns = [
    # Data based views
    path('user', UserView.as_view(), name='user'),
    path('interest', InterestView.as_view(), name='interest'),
    path('like', LikeView.as_view(), name='like'),
    path('stat', StatView.as_view(), name='stat'),

    # Function based views
    path('feed', get_feed, name='feed'),
]
