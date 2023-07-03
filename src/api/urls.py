from django.urls import path
from .views import UserView, get_method, post_method

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:id>/', UserView.as_view(), name='user-detail'),
    path('get/', get_method, name='get'),
    path('post/', post_method, name='post'),

]