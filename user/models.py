from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    pass  # Nenhuma modificação necessária, mantenha a classe vazia se não precisar de métodos personalizados


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):  
    username = models.CharField(max_length=150, null=True)  
    name = models.CharField(max_length=150) # nome - tipo string porem o charfield tem como configurar o tamanho
    email = models.EmailField(unique=True) # emai tipo de dados texto
    password = models.TextField() # password string
    age = models.IntegerField(default=None, null=True, blank=True) # idade inteiro
    ownerApp = models.BooleanField(default=False, null=True, blank=True) # dono do app boleano
    height = models.FloatField(default=None, null=True, blank=True) # altura float
    weight = models.FloatField(default=None, null=True, blank=True) # peso float     
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']
    
    def __str__(self):
        #return str(self)
        return f"User(username={self.name},,name={self.name}, email={self.email}, age={self.age}, ownerApp={self.ownerApp}, height={self.height}, weight={self.weight})"

# default=None: Isso define o valor padrão como None. 
    #Você pode ajustar isso para qualquer valor 
    #padrão desejado.

# null=True: Isso permite que o campo seja nulo no
    #banco de dados, tornando-o opcional.

# blank=True: Isso permite que o campo seja 
    #deixado em branco nos formulários.