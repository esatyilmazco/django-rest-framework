from django.urls import path
from account.api.views import ProfileView, UpdatePassword, CreateUser

app_name = 'account'
urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
    path('change-password', UpdatePassword.as_view(), name='change-password'),
    path('register', CreateUser.as_view(), name='register'),

]
