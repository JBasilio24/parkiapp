from django.db import models
from users.models import User

class Terminal(models.Model):
    number = models.IntegerField(default=0)
    address = models.TextField()

    def __str__(self):
        return '%s' % self.id

class Car(models.Model):
    FREE = 'FR'
    OCUPADE = 'OC'
    ALERT = 'AL'

    STATUS = (
        (FREE, 'Libre'),
        (OCUPADE, 'Ocupado'),
        (ALERT, 'Alerta'),
    )

    user = models.ForeignKey(User, default=1)
    terminal = models.ForeignKey(Terminal, default=1)
    date_start = models.DateTimeField(editable=True, auto_now=True, null=True)
    date_end = models.DateTimeField(editable=True, auto_now=True, null=True)
    hr = models.SmallIntegerField(null=True, default=0)
    minut = models.SmallIntegerField(null=True, default=0)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    plates = models.CharField(max_length=15)
    status = models.CharField(max_length=2, choices=STATUS, default='FR')

    def __str__(self):
        return '%s' % self.id

    def get_hr(self):
        return self.date_start.strftime('%H:%M')

class Zone(models.Model):
    street_start = models.CharField(max_length=15 ,null=True, default="")
    street_end = models.CharField(max_length=15 ,null=True, default="")


class Supervisor(models.Model):
     zone = models.ForeignKey(Zone, default=0)
     terminal = models.ForeignKey(Terminal, default=0)
     work_number = models.IntegerField(default=0)
     user = models.ForeignKey(User, default=0)
