from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    register_page,
    login_page,
    logout_page,
)

urlpatterns = [
    # API
    path('api/register/', RegisterView.as_view(), name='register_api'),
    path('api/login/', LoginView.as_view(), name='login_api'),

    # Frontend
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
]