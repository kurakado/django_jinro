from django.db import models

# Create your models here.
class Village(models.Model):
    class Meta:
        db_table = "village_info"
    # id
    name=models.CharField(max_length=32)
    max_people=models.IntegerField(default=17)

class Role(models.Model):
    class Meta:
        db_table = "role_info"
    #id
    role_name=models.CharField(max_length=16,unique=True)

class HN(models.Model):
    class Meta:
        db_table = "handle_name_info"
    #id
    name=models.CharField(max_length=16)
    password=models.CharField(max_length=16)

class Participant(models.Model):
    class Meta:
        db_table = "participant_info"
    # id
    HN=models.ForeignKey(HN)
    CN=models.CharField(max_length=16)
    role=models.ForeignKey(Role,null=True)
    village=models.ForeignKey(Village)
    alive_flag=models.BooleanField(default=True)
    IPaddr=models.CharField(max_length=15)

class Comment(models.Model):
    class Meta:
        db_table = "comment_info"
    #id
    village=models.ForeignKey(Village)
    person=models.ForeignKey(Participant)
    time=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=1000)
