from django.urls import path
from catalogo import views

urlpatterns=[
	path('', views.catalogo, name="catalogo"),
	path('ver_mas/', views.ver_mas, name="ver_mas"),
]