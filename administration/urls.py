from django.urls import path

from administration import views


# URL configuration for administration app.

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
