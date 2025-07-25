from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/trend/', api.trend_data, name='trend-api')
]
