"""ee_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.routers import DefaultRouter


# Django REST framework API routing
router = DefaultRouter()

# API endpoints


# Construct URLs
urlpatterns = [
    # API registration
    url(r'^api/', include(router.urls)),

    # Django admin views
    url(r'^api-admin/', admin.site.urls),
]


# DEBUG mode only URLs
if settings.DEBUG:
    urlpatterns += [
        # REST framework browsable API login/logout views
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

        # API documentation
        # url(r'^api-docs/', include('rest_framework_swagger.urls')),
    ]

    # Media files URL
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

