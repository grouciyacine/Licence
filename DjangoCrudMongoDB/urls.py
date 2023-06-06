"""DjangoCrudMongoDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from DjangoCrudApp import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts',views.PostsList.as_view()),
    path('api/',include('DjangoCrudApp.urls')),
    path('login/',views.login_api),
    path('getuser/',views.get_user_data),
    path('reg/',views.register_api),
    path('excel',views.JsonUploadView.as_view()),
    path('api/', include(router.urls)),
    path('npk',views.JsonUploadNPKView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
