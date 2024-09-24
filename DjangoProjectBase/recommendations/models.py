from django.db import models

# Create your models here.
class Recommendation(models.Model): 
    description = models.CharField(max_length=1500) 

    def __str__(self): 
        return self.description