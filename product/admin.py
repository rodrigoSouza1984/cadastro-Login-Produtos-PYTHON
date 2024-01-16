from django.contrib import admin

#Register your models here.
from django.contrib import admin	#add aki
from .models import UserProduct		#add aki

admin.site.register(UserProduct)		#add aki