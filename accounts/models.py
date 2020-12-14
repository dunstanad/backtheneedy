from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
fs = FileSystemStorage(location='/media/photos')
class OrgData(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    myfile = models.ImageField(upload_to='media', default="False")
    urgent = models.CharField(max_length=100)
    need_desc = models.CharField(max_length=150)
    bank_acc = models.CharField(max_length=20,default="0000")
    bank_ifsc = models.CharField(max_length=15,default="0000")
    upi_id = models.CharField(max_length=15,default="upi@upi.com")

   
    def __str__(self):
        return "Organisation Name: " + self.name
  


# Create your models here.
