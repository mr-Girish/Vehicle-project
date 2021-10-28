from django.db import models

# Create your models here.

class vehicle(models.Model):
    vehicle_id=models.AutoField
    vehicle_name=models.CharField(max_length=50)
    des =models.CharField(max_length=200)
    rent_date=models.DateField('')
    image=models.ImageField(upload_to="vehicleservice/images",default="" )


class users(models.Model):
    user_id=models.AutoField
    user_name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)

    def __str__(self):
        return self.vehicle_name