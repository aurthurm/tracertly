
from django.contrib import admin
from django.contrib.auth import views as viewz
from django.urls import path, include, re_path
# from .routers import router
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', viewz.login, name='login'),
    path('accounts/logout/', viewz.logout, name='logout', kwargs={'next_page': '/'}),
    re_path(r'^tinymce/', include('tinymce.urls')),
    # path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('users/', include('users.urls')),
    path('boards/', include('boards.urls')),
    path('divisions/', include('divisions.urls')),
]
