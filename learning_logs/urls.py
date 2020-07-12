from . import views
from django.urls import path



app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('image/<int:post_id>/', views.image, name='image'),
    path('new_post/', views.new_post, name='new_post'),

]


