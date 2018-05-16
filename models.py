from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_lenth=32)


