from django.urls import path

from login.api.viewsets import authLogin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)




urlpatterns = [
    path("", authLogin),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Adicione mais rotas conforme necessário
]