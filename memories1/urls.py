# URLS.PY
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("category/<category>/", views.post_category, name="post_category"),
    path('post/', views.post, name='post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('profiles/', include('profiles.urls')),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)