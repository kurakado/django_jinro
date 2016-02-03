from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Villaage(models.Model):
    class Meta:
        db_table = "village_info"
    name=models.CharField(max_length=50)
    max_number_of_people=models.IntegerField()

class Participant(models.Model):
    class Meta:
        db_table = "participant_info"


class Role(models.Model):
    class Meta:
        db_table = "role_info"
