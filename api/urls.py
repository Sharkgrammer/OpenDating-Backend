from django.urls import path
from api.views.model_views.user import UserView

app_name = "api"
urlpatterns = [
    # Data based views
    path('user', UserView.as_view(), name='user'),
]
