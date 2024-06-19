from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel

# Create your models here.
class State(BaseModel):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class City(BaseModel):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities', blank=False, null=False)

    def __str__(self) -> str:
        return self.name

class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='addresses', blank=False, null=False)
    zipcode = models.CharField(max_length=6, blank=False, null=False, default='00000')

    @property
    def state(self):
        return self.city.state
    @property
    def zip_code(self):
        return self.city.zip_code

    def __str__(self):
        return self.address + ' - ' + self.city + ' - ' + self.state 

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    state = models.ForeignKey(State, related_name='users', on_delete=models.SET_DEFAULT, default=1)
    city = models.ForeignKey(City, related_name='users', on_delete=models.SET_DEFAULT, default=2)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)

    def __str__(self):
        return self.user.username + ' - ' + self.created_at.strftime('%Y-%m-%d %H:%M:%S')
