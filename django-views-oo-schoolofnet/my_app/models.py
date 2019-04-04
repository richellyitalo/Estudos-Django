from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .choices import STATE_CHOICES


class Address(models.Model):
    address = models.CharField(max_length=255)
    address_complement = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, choices=STATE_CHOICES)
    country = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s/%s, %s' % (self.address, self.city, self.get_state_display(), self.country)

    @property
    def address_complement_normalized(self):
        return '' if self.address_complement is None else self.address_complement

    def get_absolute_url(self):
        return reverse('my_app:address-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Adresses'
