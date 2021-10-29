from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.address} , {self.name} .'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# so that we can map a location to multiple meetups as well

class Meetup(models.Model): # tableName
    title = models.CharField(max_length=200) # columns
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant,blank=True)

    def __str__(self):
        return f'{self.title}'