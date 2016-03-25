from django.db import models

# Festival models
class Festival(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    logo = models.ImageField(upload_to='uploads/', default='/uploads/leeg.png')

    def __str__(self):
        return self.name

# Artist
class Artist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=50)
    record_label = models.CharField(max_length=50)

    def __str__(self):
        return self.name
