from django.urls import path

from . import views
urlpatterns = [
    path('api/jobs/', views.job_list, name='job_list'),  # Example URL pattern mapping to a view
    # Add other URL patterns as needed
    path('', views.index, name='index'),
]
