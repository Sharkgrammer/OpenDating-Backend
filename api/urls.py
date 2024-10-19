from django.urls import path
from api.views.model_views.user import UserView
from api.views.model_views.interest import InterestView

app_name = "api"
urlpatterns = [
    # Data based views
    path('user', UserView.as_view(), name='user'),
    path('interest', InterestView.as_view(), name='interest'),
]
