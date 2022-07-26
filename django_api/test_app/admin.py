from django.contrib import admin
from .models import *


admin.site.register((TestModel, ModelX, ModelY))