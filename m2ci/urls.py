from django.urls import path
from . import views

app_name = "m2ci"
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.Home, name='Home'),
    path('test/News/', views.News, name='News'),
    path('test/Portfolio/', views.Portfolio, name='Portfolio'),
    path('test/About/', views.About, name='About'),
    path('test/Services/', views.Services, name='Services'),
    path('test/Team/', views.Team, name='Team'),
    path('test/Contact/', views.Contact, name='Contact'),
]

