from django.urls import path, include
from post.api.views import PostDetailAPIView, PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostCreateAPIView
from django.views.decorators.cache import cache_page

app_name = 'post'
urlpatterns = [
    path('list', cache_page(60*1)(PostListAPIView.as_view()), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('create/', PostCreateAPIView.as_view(), name='create'),


]
