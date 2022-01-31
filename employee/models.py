from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):        #name likhkr aayega jiske nam se database me entry kiho
        return self.name
    
class Employe(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    mobile=models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    city=models.CharField(max_length=50)
    salary=models.FloatField()

class Meta:
    db_table="empdata"
