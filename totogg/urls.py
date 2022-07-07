from django.urls import path
from . import views


urlpatterns = [
    path('', views.totogg),
    path('chart/', views.chart),
    path('pred/', views.pred),
    path('rank/', views.rank_page),
    
    
]