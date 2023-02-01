from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/', views.Category.as_view(), name='category'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('about/', views.About.as_view(), name='about'),
]
