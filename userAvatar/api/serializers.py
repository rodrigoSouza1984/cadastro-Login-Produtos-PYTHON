from rest_framework.serializers import ModelSerializer, ValidationError
from userAvatar.models import UserAvatar
from user.models import User
from rest_framework import status

class UserAvatarSerializer(ModelSerializer):    
    class Meta:
        model = UserAvatar
        fields = '__all__'
        
    def addAndUpdateAvatar(self, body, userId):           

            userExists = User.objects.filter(id=userId).first()            
            
            if userExists == None:                
                 raise ValidationError("User Not Found", code=status.HTTP_404_NOT_FOUND)              

            avatarExists = UserAvatar.objects.filter(user_id=userId).first()

            if avatarExists:
                avatarExists.delete()                   
            
            body['user'] = userExists            

            avatarCreated = UserAvatar.objects.create(**body)                               

            return avatarCreated 


       
    def deleteAvatar(self, userId, avatarId):           

            userExists = User.objects.filter(id=userId).first()            
            
            if userExists == None:                
                 raise ValidationError("User Not Found", code=status.HTTP_404_NOT_FOUND)              

            avatarExists = UserAvatar.objects.filter(id=avatarId).first()            

            if avatarExists.user.id == userExists.id:                
                avatarExists.delete() 

                return True                  
            else:
                raise ValidationError("User not owner Avatar", code=status.HTTP_400_BAD_REQUEST)                             
        

            
                 

            
            