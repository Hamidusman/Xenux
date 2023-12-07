from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Education(models.Model):
    certification = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.certification

class Experience(models.Model):
    position = models.CharField(max_length=20)
    organization = models.CharField(max_length=30)
    duration = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.position

class Skill(models.Model):
    skill1 = models.CharField(max_length=30, default='')
    skill2 = models.CharField(max_length=30, default='')
    skill3 = models.CharField(max_length=30, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Skillsets'