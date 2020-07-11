from . import views
from django.urls import path



app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('image/<int:post_id>/', views.image, name='image'),
    path('new_imege/', views.new_imege, name='new_imege'),

]
