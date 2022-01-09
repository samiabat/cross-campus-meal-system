from django.db import models

# Create your models here.
class Student(models.Model):
    year = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
    )
    camp = (
        ("4killo","4killo"),
        ("5killo","5killo"),
        ("6killo","6killo"),
    )
    depart = (
        ("software engineer","software engineer"),
        ("electrical Engineer","electrical Engineer"),
        ("mechanical Engineer","mechanical Engineer"),
        ("biomedical Engineer","biomedical Engineer"),
        ("civil Engineer","civil Engineer"),
        ("chemical Engineer","chemical Engineer"),
    )
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50, choices = depart)
    id = models.CharField(max_length = 14, primary_key = True)
    bach = models.CharField(max_length = 50,choices = year)
    campus = models.CharField(max_length = 50, choices = camp )
    section = models.CharField(max_length =2)



class Schedule(models.Model):
    year = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
    )
    depart = (
        ("software engineer","software engineer"),
        ("electrical Engineer","electrical Engineer"),
        ("mechanical Engineer","mechanical Engineer"),
        ("biomedical Engineer","biomedical Engineer"),
        ("civil Engineer","civil Engineer"),
        ("chemical Engineer","chemical Engineer"),
    )
    camp = (
        ("4killo","4killo"),
        ("5killo","5killo"),
        ("6killo","6killo"),
    )
    d = (
        ('monday','monday'),
        ('tuesday','tuesday'),
        ('wednesday','wednesday'),
        ('thursday','thursday'),
        ('friday','friday'),
        ('saturday','saturday'),
        ('sunday','sunday')
        )
    bach = models.CharField(max_length = 50,choices = year)
    department = models.CharField(max_length = 30, choices = depart)
    section = models.CharField(max_length = 2)
    campus = models.CharField(max_length = 50, choices = camp)
    day = models.CharField(max_length = 20, choices = d)
    startTime = models.TimeField()
    endTime = models.TimeField()

    

class Admin(models.Model):
    name = models.CharField(max_length = 40)
    username = models.CharField(max_length = 20)

class User(models.Model):
    name = models.CharField(max_length = 40)
    username = models.CharField(max_length = 20)

class MealStatus(models.Model):
    s = (
        ('0', '0'),
        ('1', '1'),
    )
    student_id = models.CharField(max_length = 20, primary_key = True)
    breakfast = models.CharField(max_length  = 1, choices = s)
    lunch = models.CharField(max_length  = 1, choices = s)
    dinner = models.CharField(max_length  = 1, choices = s)
    