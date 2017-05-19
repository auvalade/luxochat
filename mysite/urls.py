from django.conf.urls import url
from django.contrib import admin

import chatbox.views

urlpatterns = [
    url(r'^$', chatbox.views.index, name = 'index'),
    url(r'^admin/', admin.site.urls),
]
