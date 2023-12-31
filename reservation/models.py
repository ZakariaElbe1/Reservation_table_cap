from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.SmallIntegerField(db_index=True)
    bookingDate = models.DateField(db_index=True)

    def __str__(self):
        return self.name 


class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField(db_index=True)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
