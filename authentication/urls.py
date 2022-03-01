from .views import AccountSignupView
from django.urls import path
app_name = 'authentication_app'

urlpatterns = [
    path("accounts/signup/", AccountSignupView.as_view()),

]
