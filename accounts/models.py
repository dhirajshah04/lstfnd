from django.db import models
from django.conf import settings

class Profile(models.Model):
    gender = (
        ('Male','Male'),
        ('Female','Female'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=10, null=False, choices=gender, default='Male')
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.BigIntegerField(default=0)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)