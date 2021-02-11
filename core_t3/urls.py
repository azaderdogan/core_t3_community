"""core_t3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/members/', include('users.api.urls')),
    path('api/utils/', include('utils.api.urls')),
    path('api/posts/', include('posts.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # browsable api sayfası için - daha önce yaptığımız gibi(api sayfaındaki login butonu)
    path('api/rest-auth/', include('rest_auth.urls')),  # django rest auth ile gelen endpointler için
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')), # buraya istek yapıp kullanıcı kaydı yapacağız
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
