from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_lenth=32)

class Country(models.Model):
    name = models.CharField(max_lenth=32)
    code = models.SmallIntger()


class School(models.Model):
    name = models.CharField(max_length=32)


