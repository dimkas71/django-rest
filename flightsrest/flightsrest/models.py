from django.db import models

class Aircraft(models.Model):
    aircraft_code = models.CharField(primary_key = True, max_length = 3)
    model = models.TextField()
    range = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'aircrafts'