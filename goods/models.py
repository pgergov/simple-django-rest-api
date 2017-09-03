from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=255)
