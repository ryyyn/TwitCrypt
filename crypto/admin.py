from django.contrib import admin

from .models import Auth

# add database inspection/moderation functionality

admin.site.register(Auth)