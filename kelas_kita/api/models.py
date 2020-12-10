from django.db import models

# Create your models here.

class PageView(models.Model):
    page_id = models.IntegerField(null=False, unique=True)
    page_views = models.IntegerField(null=False, default=0)