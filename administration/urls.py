from django.urls import path

from administration import views


# URL configuration for administration app.

urlpatterns = [
    path('register/', views.register, name='register')
]
