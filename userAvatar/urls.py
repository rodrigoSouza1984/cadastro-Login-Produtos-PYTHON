from django.urls import path

from userAvatar.api.viewsets import addAndUpdateAvatar, deleteAvatar


urlpatterns = [
    path("<int:userId>/", addAndUpdateAvatar),
    path("<int:userId>/<int:avatarId>", deleteAvatar),     
    # Adicione mais rotas conforme necessário
]
