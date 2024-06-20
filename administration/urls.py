from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from administration import views
from administration.API.views import StateViewSet, CityViewSet

# URL configuration for administration app.
app_name = 'administration'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashbord/', views.dashbord, name='dashbord'),
]

# API URL configuration for administration app.
router = DefaultRouter()
router.register('states', StateViewSet, basename='state')
router.register('cities', CityViewSet, basename='city')

# Adding the router URLs with the 'api' prefix
urlpatterns += [
    path('api/', include(router.urls)),
]
