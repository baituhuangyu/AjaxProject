from django.db import models

# Create your models here.
from django.db import models

class Ajaxdb(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=255, blank=True)
    itemcontent = models.CharField(max_length=255, blank=True)
    itemurl = models.CharField(max_length=255, blank=True)

