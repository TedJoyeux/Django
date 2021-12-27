from django.contrib import admin
from .models import Project
from .models import Review
from .models import Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
