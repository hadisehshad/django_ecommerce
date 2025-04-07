from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

app_name = 'account'

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT access and refresh tokens
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # Refresh the access token using the refresh token
    path('api/v1/send_code/', SendCodeView.as_view(), name='send_code'),  # Send a verification code
    path('api/v1/register_or_login/', RegisterView.as_view(), name='register_view'),
    # Register a new user or log in an existing user

    # START V2------------------------------------------------------------
    path('api/v2/person/', PersonView.as_view(), name='person_person'), # get create update profile



]
