from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel
from administration.models import City, State

# Create your models here.

class Parcel(BaseModel):
    # Parcel model
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parcels')
    to_name = models.CharField(max_length=50, null=False, blank=False)
    to_phone = models.CharField(max_length=15, blank=False, null=False)
    to_email = models.EmailField(blank=True, null=True)
    to_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='parcels', blank=False, null=False)
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='parcels', blank=False, null=False)
    to_address = models.TextField(null=False, blank=False)
    to_zipcode = models.CharField(max_length=6, blank=False, null=False, default='00000')

    @property
    def from_state(self):
        return self.from_user.userprofile.state

    @property
    def from_city(self):
        return self.from_user.userprofile.city

    @property
    def from_address(self):
        return self.from_user.userprofile.address

    @property
    def from_zipcode(self):
        return self.from_user.userprofile.zipcode

    @property
    def from_phone(self):
        return self.from_user.userprofile.phone

    def __str__(self):
        text = f'parcel from {self.from_user.username} to {self.to_name}'
        return text
