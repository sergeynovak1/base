from django.urls import path
from users.views import user_list, user_card, edit_user, delete_user, create_user
from .views import logs_list, log_card

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_card, name='user_card'),
    path('users/<int:user_id>/edit/', edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),
    path('users/create/', create_user, name='create_user'),
    path('logs/', logs_list, name='log_list'),
    path('logs/<int:log_id>/', log_card, name='log_card'),
]