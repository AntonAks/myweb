from django.db import models

# TODO: need to read about models.Model module

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = model.CharField(max_length=200)
