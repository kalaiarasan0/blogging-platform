from django.urls import path
from .views import UserRegisterView, UserEditView,ChangePasswordView,ShowProfilePageView,EditProfilePageView,CreateUserProfileView
from . import views


urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='Edit-Profile'), 
    path('change_password/', ChangePasswordView.as_view(template_name='registration\change_password.html'), name='change_password'),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('createprofilepage/', CreateUserProfileView.as_view(), name='createuserProfile')
]   