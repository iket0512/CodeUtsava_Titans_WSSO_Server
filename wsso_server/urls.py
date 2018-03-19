
"""wsso_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings            
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin

from data.views import populate
from posts.views import pointers, test, test_map, trigger_post,get_posts, get_post_id, get_habitation,get_mobileposts, hardcoded

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^home/', test),
    url(r'^map/', test_map),
    # url(r'^populate/', populate),
    url(r'^pointers/', pointers),
    # url(r'^trigger_post/', trigger_post),
    url(r'^home/', get_posts),
    url(r'^notify/', hardcoded),

    url(r'^post/(?P<id>\w+)/', get_post_id),
    url(r'^habitation/(?P<id>\w+)/', get_habitation),
    url(r'^get_mobileposts/', get_mobileposts)

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
