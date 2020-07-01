"""User model"""

from django.db import models
from django.contrib.auth.models import AbstractUser

from cride.utils.models import CRideModel
from .validators import phone_regex

class User(CRideModel, AbstractUser):
    """User model

    Extend from Django's Abstract User, change username
    field to email and add some extra fields.
    """

    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )
    is_client = models.BooleanField(
        'client_status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type or user.'
        )
    )
    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username
    
    def get_short_name(self):
        """Return username."""
        return self.username