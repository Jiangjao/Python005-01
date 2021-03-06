from django.db import models

class Moviebang(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    n_start = models.IntegerField(blank=True, null=True)
    short = models.CharField(max_length=10000, blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField()
    movietitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moviebang'

    def __str__(self):
        return self.name



