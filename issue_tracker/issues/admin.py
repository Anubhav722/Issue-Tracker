# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from issues.models import UserProfile, Issue
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Issue)
