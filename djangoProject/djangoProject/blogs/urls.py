from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('home/<int:post_id>/', views.home, name='home'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)