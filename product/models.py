from django.db import models
from user.models import User

# Create your models here.
class UserProduct(models.Model): 
    id = models.AutoField(primary_key=True)     
    title = models.TextField() 
    url = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    

    def __str__(self):
        return f"UserProduct(id={self.id},title={self.title}, url={self.url}, price={self.price},quantity={self.quantity}, user={self.user})"
# Create your models here.
