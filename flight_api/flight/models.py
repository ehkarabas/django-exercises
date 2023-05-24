from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# -----------------------------------------------------------
# --------------------- FixModel ----------------------------
# -----------------------------------------------------------
# Fix Model(daha sonra surekli olarak kullanilacak field'lari icerecek olan model)


class FixModel(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# -----------------------------------------------------------
# --------------------- Passenger ---------------------------
# -----------------------------------------------------------

class Passenger(FixModel):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('0', 'Prefer Not To Say')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDERS, default='0')
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# -----------------------------------------------------------
# --------------------- Flight ------------------------------
# -----------------------------------------------------------

class Flight(FixModel):
    AIRLINES = (
        ('THY', 'Turkish Airlines'),
        ('PEG', 'Pagasus Airlines'),
        ('HUS', 'Huseyin Airlines'),
    )

    CITIES = (
        (1, 'Adana'),
        (7, 'Antalya'),
        (34, 'Istanbul'),
        (35, 'Izmir'),
        (16, 'Bursa'),
        (10, 'Balikesir')
    )

    flight_number = models.CharField(max_length=64)
    airline = models.CharField(max_length=3, choices=AIRLINES)
    departure = models.PositiveSmallIntegerField(choices=CITIES)
    departure_date = models.DateField()
    arrival = models.PositiveSmallIntegerField(choices=CITIES)
    arrival_date = models.DateField()

    def __str__(self):
        return f'{self.flight_number} # {self.airline} / {self.departure} -> {self.arrival}'


# -----------------------------------------------------------
# --------------------- Reservation -------------------------
# -----------------------------------------------------------

class Reservation(FixModel):
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name='reservation_flight')
    passenger = models.ManyToManyField(
        Passenger, related_name='reservation_passenger')

    def __str__(self):
        return f'{self.flight} [{self.passenger.count()}]'

    # class Meta:
    #     verbose_name = _("Reservation")
    #     verbose_name_plural = _("Reservations")
