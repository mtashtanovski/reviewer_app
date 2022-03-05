from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import (
                            RegisterView,
                            UserProfileView,
                            UsersProfilesListView,
                            UpdateUserView,
                            UserPasswordChangeView,
                            )

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('profiles/', UsersProfilesListView.as_view(), name='users_profiles_list'),
    path("update/", UpdateUserView.as_view(), name="update_user"),
    path("change_password/", UserPasswordChangeView.as_view(), name="change_password"),
]
