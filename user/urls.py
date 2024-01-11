# user/urls.py
from django.urls import path

from user.api.viewsets import createUser, getUsers, getUserById, updatePatchUserById, updatePutUserById, deleteUsersByIds, getUserByEmail


urlpatterns = [
    path("", createUser),
    path("get/", getUsers),
    path("get/<int:userId>", getUserById),
    path("getByEmail/<str:email>", getUserByEmail),
    path('updatePatch/<int:userId>/', updatePatchUserById),
    path('updatePut/<int:userId>/', updatePutUserById),
    path('deleteUsersByIds/<int:userId>/', deleteUsersByIds),
    # Adicione mais rotas conforme necessário
]