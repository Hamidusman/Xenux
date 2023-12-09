from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=150)
    occupation = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=20)
    about = models.TextField(max_length=150)

    def __str__(self):
        return self.owner.username
    


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