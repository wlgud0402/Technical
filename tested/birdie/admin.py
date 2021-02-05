from django.contrib import admin
from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = models.Post
    list_display = ('excerpt',)

    def excerpt(self, obj):
        return obj.get_excerpt(5)


admin.site.register(models.Post, PostAdmin)
