from django.contrib import admin
from django.urls import path
from test_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', simple),
    path('json/', json),
]
