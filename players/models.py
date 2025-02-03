import django.utils.timezone
from django.db import models
import datetime


class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=None)
    photo = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    date_of_insert = datetime.date.today()

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def __str__(self):
        return self.surname + ' ' + self.name


class Review(models.Model):
    RATING_CHOICES = ((1, '1 - Bad'), (2, '2 - Sufficient'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent'))

    title = models.CharField(max_length=50)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    rating = models.IntegerField(choices=RATING_CHOICES)
    pub_date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title


class Concert(models.Model):
    place = models.CharField(max_length=100)
    concert_time = models.DateTimeField(default=None)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.place + ', ' + str(self.concert_time)
