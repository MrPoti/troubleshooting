from django.contrib import admin

from .models.category import Category
from .models.issue import Issue
from .models.solution import Solution

admin.site.register(Category)
admin.site.register(Issue)
admin.site.register(Solution)
