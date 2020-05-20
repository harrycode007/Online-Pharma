from django.db import models

# The following are the models listed and used in the project.

GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('rather', 'Non binary'),
)

CELLPHONE_CHOICE = (
    ('91', '+91'),
    ('92', '+92'),
    ('93', '+93'),
    ('94', '+94'),
    ('95', '+95'),
    ('96', '+96'),
)

LOOKING_CHOICE = (
    ('Just Information', 'Just Information'),
    ('Treatment Details', 'Treatment Details'),
)
class Registration(models.Model):
    mes_id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email = models.EmailField(default="null")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='male')
    selphone=models.CharField(max_length=10, choices=CELLPHONE_CHOICE, default='91')
    contactnumber = models.CharField(max_length=10, default="")
    password=models.CharField(max_length=20,default="")
    cpassword = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=20, default="")


    def __str__(self):
        return self.fname


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200,default="null")
    message = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class MedicineOrdered(models.Model):
    Combiflam = models.IntegerField(default=0)
    Paracetamol = models.IntegerField(default=0)
    Cofsils = models.IntegerField(default=0)
    DigeneTablet = models.IntegerField(default=0)
    DigeneGel = models.IntegerField(default=0)
    Hajmola = models.IntegerField(default=0)
    Seacod = models.IntegerField(default=0)
    Shelcal = models.IntegerField(default=0)
    Crocin = models.IntegerField(default=0)
    Lubrifresh = models.IntegerField(default=0)
    Dettol = models.IntegerField(default=0)
    Ashwagandha = models.IntegerField(default=0)
    Moov = models.IntegerField(default=0)
    Zandu = models.IntegerField(default=0)
    Vicks = models.IntegerField(default=0)
    Chyawanprash = models.IntegerField(default=0)
    totalSum = models.IntegerField(default=0)
    storeemail = models.EmailField(default="null")
    def __str__(self):
        return self.storeemail

class Contactlogin(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200, default="null")
    message = models.CharField(max_length=2000, default="")

    def __str__(self):
            return self.name