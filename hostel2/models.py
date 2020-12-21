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

