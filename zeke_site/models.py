from django.db import models

# Create your models here.
class News(models.Model):
    news = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.news

class Videos(models.Model):
    video_title = models.CharField(max_length=512)
    embed_video_html = models.TextField()
    type = models.CharField(max_length=1, choices=( ('W', 'Work'), ('P', 'Play') ))
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Videos'

    def __unicode__(self):
        return self.video_title
