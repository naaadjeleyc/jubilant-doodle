from django.db import models

# Create your models here

class Members(models.Model):
    members= models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
	