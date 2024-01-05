from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField(default=6)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
