from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,default='')
    email = models.CharField(max_length=40, default='')
    password = models.CharField(max_length=100, default='')
    phone = models.IntegerField(max_length=40, default='')
    address = models.TextField(max_length=300, default='')
    desc = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.name
