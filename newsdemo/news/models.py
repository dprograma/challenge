from django.db import models

# Create your models here.


class DemoNewsModel(models.Model):
    newsid = models.BigIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    relatedids = models.TextField(blank=True, null=True)
    score = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    newstype = models.CharField(max_length=255, blank=True)
    descendants = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # replacing the id(primary key) as the demonews id
        self.id = self.newsid
        super(DemoNewsModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.newsid)
