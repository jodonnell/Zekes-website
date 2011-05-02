from zeke.zeke_site.models import News, Videos
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news', 'created_on')
    ordering = ('-created_on',)

class VideosAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'created_on')
    ordering = ('-created_on',)

admin.site.register(News, NewsAdmin)
admin.site.register(Videos, VideosAdmin)
