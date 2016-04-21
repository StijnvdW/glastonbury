from django.db import models

# Artist
class Artist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=50)
    record_label = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Festival models
class Festival(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    logo = models.ImageField(upload_to='uploads/',
    default='/uploads/leeg.png')
    performers = models.ManyToManyField(Artist, through='Performance')

    def __str__(self):
        return self.name

# Artist Performs on Fesitval
class Performance(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    festival = models.ForeignKey(to='Festival', on_delete=models.CASCADE)
    artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return "{} performs on {} at {}".format(self.artist.name,
        str(self.date), self.festival)
