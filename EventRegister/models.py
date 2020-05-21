from django.db import models
import uuid
# Create your models here.


class Register(models.Model):
    reg_id = models.CharField(primary_key=True, max_length=8, editable=False)
    fullname = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    identification = models.ImageField(upload_to='ids')
    reg_type = models.CharField(max_length=20)
    no_ticket = models.IntegerField()
    reg_date = models.DateField(auto_now=True)


