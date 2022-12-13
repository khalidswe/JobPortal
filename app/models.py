from datetime import date, datetime
from distutils.command.upload import upload
import email
from email.policy import default
from statistics import mode
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(default=datetime.today())
    is_updated = models.DateTimeField(default=datetime.today())


class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.DateField(max_length=50,blank=True,null=True)
    gender = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    maritual_status = models.CharField(max_length=20)
    portfolio = models.CharField(max_length=50)
    uni_college1 = models.CharField(max_length=100)
    major1 = models.CharField(max_length=100)
    degree1 = models.CharField(max_length=50)
    sgpa1 = models.CharField(max_length=20)
    uni_college2 = models.CharField(max_length=100)
    major2 = models.CharField(max_length=100)
    degree2 = models.CharField(max_length=50)
    sgpa2 = models.CharField(max_length=20)
    skill = models.CharField(max_length=500)
    additional_skill = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to="app/img/candidate")

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    website = models.CharField(max_length=100,blank=True,null=True)
    contact= models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=500,blank=True,null=True)
    about_us = models.CharField(max_length=1000,blank=True,null=True)
    services = models.CharField(max_length=1000,blank=True,null=True)
    logo = models.ImageField(upload_to="app/img/company")

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=300)
    job_position =models.CharField(max_length=300,blank=True,null=True)
    company_name= models.CharField(max_length=300)
    company_email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    company_website = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    job_context = models.TextField(max_length=1000)
    responsibilities = models.TextField(max_length=1000)
    qualification = models.CharField(max_length=1000)
    employement_status = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    vacancy = models.IntegerField()
    salary= models.CharField(max_length=100)
    apply_deadline = models.DateField(max_length=50) 
    job_logo = models.ImageField(upload_to="app/img/jobpostlogo")


class AppliedJob(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    jobname = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    portfolio = models.CharField(max_length=100)
    uni_name = models.CharField(max_length=500)
    major = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    sgpa = models.CharField(max_length=20)
    skill = models.CharField(max_length=500)
    additional_skill = models.CharField(max_length=500)
    cv = models.FileField(upload_to="app/cv")


#class AdminDB(models.Model):