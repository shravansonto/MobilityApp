# models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    adhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)
    assigned_mobile_number = models.CharField(max_length=10, unique=True)

class Plan(models.Model):
    PLAN_CHOICES = (
        ('Platinum365', 'Platinum365'),
        ('Gold180', 'Gold180'),
        ('Silver90', 'Silver90'),
    )
    plan_name = models.CharField(max_length=20, choices=PLAN_CHOICES)
    plan_cost = models.DecimalField(max_digits=6, decimal_places=2)
    validity_days = models.IntegerField()
    plan_status = models.CharField(max_length=10, choices=(('Active', 'Active'), ('Inactive', 'Inactive')))
    expiry_date = models.DateField(default=None, null=True) 


