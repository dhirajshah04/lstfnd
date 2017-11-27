from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    lost_or_found = (
        ('','Select'),
        ('LOST', 'Lost' ),
        ('FOUND', 'Found'),
    )

    zone = (
        ('', 'Select Zone'),
        ('koshi', 'koshi'),
        ('sagarmatha', 'sagarmatha'),
        ('Mechi', 'Mechi'),
        ('Janakpur', 'Janakpur'),
        ('Bagmati', 'Bagmati'),
        ('Narayani', 'Narayani'),
        ('Gandaki', 'Gandaki'),
        ('Dhawalagiri', 'Dhawalagiri'),
        ('Lumbini', 'Lumbini'),
        ('Rapti', 'Rapti'),
        ('Bheri', 'Bheri'),
        ('Karnali', 'Karnali'),
        ('Seti', 'Seti'),
        ('Mahakali', 'Mahakali'),
    )

    author = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(null=False, blank=False)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=False, null=False)
    updated_date = models.DateTimeField(auto_now=True)
    lost_or_found = models.CharField(max_length=10, null=False, choices=lost_or_found)
    zone = models.CharField(max_length=25, null=False, choices=zone)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
