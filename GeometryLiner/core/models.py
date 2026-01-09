from django.db import models


class GeometryFormat(models.Model):
    nome = models.CharField(max_length=50)
    geometry = models.JSONField()
