from django.db import models

class Aircraft(models.Model):
    aircraft_code = models.CharField(primary_key = True, max_length = 3)
    model = models.TextField()
    range = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'aircrafts'


class Airport(models.Model):
    airport_code = models.CharField(primary_key = True, max_length = 3)
    airport_name = models.TextField()
    city = models.TextField()
    #TODO: add custom field to map PointField to 
    #coordinates = models.PointField()  
    timezone = models.TextField() 
    class Meta:
        managed = False
        db_table = 'airports'