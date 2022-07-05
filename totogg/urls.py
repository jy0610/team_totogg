from django.urls import path
from . import views


urlpatterns = [
    path('', views.totogg),
    path('dashboard/', views.dashboard),
    path('pred/', views.pred),
    
    
]