from django.db import models



# Create your models here.
class myform(models.Model):
    steam={
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('EE','EE'),
        ('ME','ME'),
        ('CE','CE'),
        ('FT','FT'),
        ('NONE','NONE'),
    }

    c_choice={
        ('B.Tech','B.Tech'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('Masters','Masters'),
    }

    name=models.CharField( max_length=50,null=True)
    Roll_No=models.CharField( max_length=50,null=True)
    Student_ID=models.CharField( max_length=50,null=True)
    dOB=models.DateField(null=True)
    Course=models.CharField( max_length=50,choices=c_choice,null=True)
    Stream=models.CharField( max_length=50,choices=steam,null=True)
    Mobile_No=models.IntegerField( null=True)
    Address=models.TextField(max_length=150,null=True)
    percentage_10th=models.IntegerField(null=True)
    percentage_12th=models.IntegerField(null=True)

    def __str__(self):
        return self.name



