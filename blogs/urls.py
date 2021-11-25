from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include('post.api.urls'), name='post'),
    path('api/comment/', include('comment.api.urls'), name='comment'),
    path('api/favourite/', include('favourite.api.urls'), name='favourite')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
