from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Account(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    phone_number = PhoneNumberField(unique=True, region="IR")
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(age__gte=18), name="age_gte_18")
        ]

    class Meta:
        unique_together =[["full_name", "email"]]

    class Meta:
        indexes = [
            models.Index(fields=["full_name"])
        ]    
        


