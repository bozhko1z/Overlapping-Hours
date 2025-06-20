from django.contrib import admin
from django.contrib.postgres.lookups import Overlap
from .models import Input

admin.site.register(Input)
