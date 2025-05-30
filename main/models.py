from django.db import models

class Prestation(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    icon = models.FileField(upload_to='prestation_icon', blank=True, null=True)

    def __str__(self):
        return self.name
