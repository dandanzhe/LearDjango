"""myfirstweb URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import blog.views 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$',blog.views.hello),
    url(r'^datatime/$',blog.views.current_datatime),
    url(r'^time/(\d{1,2})/$',blog.views.hours_ahead),
    url(r'^sum/(\d{1,10})/$',blog.views.sum_n),
    url(r'^love/(\w+)/$',blog.views.love),
    url(r'^hhhh/$',blog.views.hhhh),
    #url(r'^search_form/$',blog.views.httprendertoresponse),
    url(r'^META/$',blog.views.request_META),
    url(r'^search/$',blog.views.search),
]
