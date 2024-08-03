from django.urls import path, re_path
import views
urlpatterns = [
    path('', views.main)
]