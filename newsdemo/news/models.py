from django.db import models

# Create your models here.

class DemoNewsModel(models.Model):
    demonews = models.BigIntegerField(unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.id = self.demonews # replacing the id(primary key) as the demonews id
        super(DemoNewsModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.demonews)