from __future__ import unicode_literals

from django.db import models
from django.db.models.deletion import CASCADE

class Conference(models.Model):
    title = models.CharField(max_length=1024)
    tagline = models.TextField(blank=True)
    begin_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.title

class Ticket(models.Model):
    """Ticket data imported from Entrio"""
    conference = models.ForeignKey(Conference, CASCADE)
    category = models.CharField(max_length=1024)
    code = models.CharField(max_length=1024)
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    country = models.CharField(max_length=2)
    company = models.CharField(max_length=1024, blank=True)
    promo_code = models.CharField(max_length=1024, blank=True)
    twitter = models.CharField(max_length=1024, blank=True)
    dietary_preferences = models.CharField(max_length=1024, blank=True)
    purchased_at = models.DateTimeField()

    class Meta:
        unique_together = ("conference", "code")

    def __unicode__(self):
        return "Ticket #%s (%s %s)" % (self.code, self.first_name, self.last_name)