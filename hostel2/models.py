from django.db import models

class Legend_Category(models.Model):
    name = models.CharField(max_length=150,primary_key=True)
    id = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Legends(models.Model):
    type = models.ForeignKey(Legend_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    year = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Council_Category(models.Model):
    name = models.CharField(max_length=150,primary_key=True)
    id = models.CharField(max_length=10)
    def __str__(self):
        return self.name



class Council(models.Model):
    category = models.ForeignKey(Council_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    rollno = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    conatctno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)



    def __str__(self):
        return self.name

