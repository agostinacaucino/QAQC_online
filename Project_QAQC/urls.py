
from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('', views.charts, name="charts"),
    path('data/', views.data, name="data"),
    path('health/', views.health, name="health"),
    path('statistics/', views.statistics, name="statistics"),
    path('admin/', admin.site.urls),
]

