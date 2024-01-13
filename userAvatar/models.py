from django.db import models
from user.models import User

# Create your models here.
class UserAvatar(models.Model):
    name = models.TextField() 
    url = models.TextField() # password string
    mimetype = models.TextField() # idade inteiro

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    #user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    
    user = models.OneToOneField(User, related_name='avatar', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"UserAvatar(name={self.name}, url={self.url}, mimetype={self.mimetype}, user={self.user})"