from django.urls import path
from . import views

app_name = "m2ci"
urlpatterns = [
    path('', views.Home, name='Home'),
    path('News/', views.News, name='News'),
    path('Portfolio/', views.Portfolio, name='Portfolio'),
    path('About/', views.About, name='About'),
    path('Services/', views.Services, name='Services'),
    path('Team/', views.Team, name='Team'),
    path('Contact/', views.Contact, name='Contact'),
]
