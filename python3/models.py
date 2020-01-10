# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'



class Student(models.Model):
    stu_name = models.CharField(max_length=10)
    stu_age = models.IntegerField()
    stu_sex = models.BooleanField(default=1)
    stu_birth = models.DateField()


class Meta:
    db_table = 'cd_student'
