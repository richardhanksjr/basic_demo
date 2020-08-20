from django.urls import path
from ui import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='ui/index.html'), name='index'),
    path('index2', TemplateView.as_view(template_name='ui/index2.html'), name='index2'),
    path('posts', views.CreatePost.as_view(), name='create-post'),
    path('random', views.RandomNumber.as_view(), name='random-number'),
]