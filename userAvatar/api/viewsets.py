from rest_framework.viewsets import ModelViewSet
from userAvatar.models import UserAvatar
from .serializers import UserAvatarSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

class UserAvatarViewSet(ModelViewSet):
    queryset = UserAvatar.objects.all()
    serializer_class = UserAvatarSerializer 
    

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def addAndUpdateAvatar(request, userId):
    if request.method == 'POST':        
        serializer = UserAvatarSerializer(data=request.data)
        if serializer.is_valid():            
            serializer.addAndUpdateAvatar(serializer.validated_data, userId)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteAvatar(request, userId, avatarId):
    if request.method == 'DELETE':
        serializer = UserAvatarSerializer()       
                
        serializer.deleteAvatar(userId, avatarId)

        return Response(status=status.HTTP_200_OK)