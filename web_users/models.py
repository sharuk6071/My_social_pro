from django.db import models
from django.contrib.auth.models import User

# here i had written code for profile pictures
#created a model profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #on_delete=models.CASCADE tells here if the user is deleted , delete profile of this user.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
