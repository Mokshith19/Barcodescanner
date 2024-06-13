from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True) # AutoField : will auto-increment
    name = models.CharField(max_length=255)
    rollno = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    email = models.EmailField(max_length = 225, default = 'default@example.com')
    econtact = models.CharField(max_length = 15)

    class Meta:
        db_table = "student"