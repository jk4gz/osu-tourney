from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField

# Create your models here.
class Mapdata(models.Model):
    map_id = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=150)
    star_rating = models.DecimalField(max_digits=3, decimal_places=2)
    bpm = models.IntegerField()
    length = models.CharField(max_length=4)
    circle_size = models.IntegerField()
    approach_rate = models.DecimalField(max_digits=2, decimal_places=1)
    overall_diff = models.DecimalField(max_digits=2, decimal_places=1)
    hp = models.DecimalField(max_digits=2, decimal_places=1)
    mapper = models.CharField(max_length=50)
