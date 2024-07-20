from .views import *
from django.contrib import admin
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap


admin.autodiscover()
app_name = 'frontend'




urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'about-me/$',AboutMe,name="about_me"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


