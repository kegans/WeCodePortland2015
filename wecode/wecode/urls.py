from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'wecode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('wecodeapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


### testing that it ignores the .pyc
