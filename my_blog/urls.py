from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from article import views

urlpatterns = [

#    url(r'^admin/', admin.site.urls),
#    url(r'^$', views.home),
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]
