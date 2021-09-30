"""DjongoTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


admin.site.site_header = 'Djongo Tutorial administration'
admin.site.site_title = 'Djongo Tutorial Admin'

schema_view = get_schema_view(
    openapi.Info(
        title="Djongo Tutorial API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('api/', include(("apps.api.urls", "apps.api"), namespace="api")),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    re_path(
        r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'
