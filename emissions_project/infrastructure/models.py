from django.db import models

class EmissionModel(models.Model):
    year = models.IntegerField()
    emissions = models.FloatField()
    emission_type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    class Meta:
        db_table = 'emissions'
        ordering = ['year']

    def __str__(self):
        return f"{self.country} - {self.year} ({self.emission_type})"
