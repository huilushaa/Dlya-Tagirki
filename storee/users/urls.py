from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import (EmailVerificationView, ProfileUpdateView,
                         UserLoginView, UserRegistrationCreateView, logout)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(ProfileUpdateView.as_view()), name='profile'),
    path('logout', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name='email_verification'),
]
