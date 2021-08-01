"""simpleui_test URL Configuration

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
from django.urls import path, include
from django.views import static  ##新增
from django.conf import settings  ##新增
from django.conf.urls import url  ##新增
import debug_toolbar

urlpatterns = [
    path('', admin.site.urls),
    path('home/', include(('home.urls', 'home'), namespace='home')),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # path('__debug__/', include(debug_toolbar.urls))
]
#
from django.conf import settings
from django.conf.urls.static import static

#
# if settings.DEBUG==False:
#     urlpatterns.append(url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'))
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:
#     urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
# urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))