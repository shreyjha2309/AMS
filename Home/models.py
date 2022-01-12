from django.db import models
from . widgets import DateInput
import datetime
from .manager import UserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser,PermissionsMixin
# Create your models here.

#Date Validator
def date_valid(value):
    today=datetime.date.today()
    # print(value.day)
    # print(today.day)
    # print(value.month)
    # print(today.month)
    # print(value.year)
    # print(today.year)
    if value.year != today.year or value.month != today.month or value.day != today.day:
        raise ValidationError("Attendance can only be for today's date!")
    # else:
    #     print("passed")
class NewCustomUser(AbstractUser,PermissionsMixin):
    username= None
    email=models.EmailField(unique=True)
    contactno=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    forget_password=models.CharField(max_length=50,null=True,blank=True)

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]




class student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()

    def __str__(self):
        return f"{self.name} and {self.roll}"

    class Meta:
        ordering = ['roll']


class subject(models.Model):
    sub = models.CharField(max_length=64)
    def __str__(self):
        return self.sub

class time(models.Model):
    sub = models.ForeignKey(subject,on_delete=models.CASCADE)
    time = models.CharField(max_length=64)
    def __str__(self):
        return self.time


class attendance(models.Model):
    name = models.CharField(max_length=64,blank=False)
    roll = models.IntegerField(blank=False)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=False,validators=[date_valid])
    sub = models.ForeignKey(subject,on_delete=models.SET_NULL,blank=True,null=True)
    # time = models.ForeignKey(time,on_delete=models.SET_NULL,blank=True,null=True)
    """ def save(self, *args, **kwargs):
        if self.date is not datetime.date.today():
            raise ValidationError("The date has to be today!")
        super(Event, self).save(*args, **kwargs) """

    class Meta:
        ordering = ["-date","roll"]


class attendanceclass(models.Model):
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    status=models.IntegerField(default=0)

    #class Meta:
        #unique_together = ('date','status')
