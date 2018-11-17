from django.urls import path
from catalogo import views

urlpatterns=[
	path('', views.catalogo, name="catalogo"),
	path('ver_mas_bicicletas/<int:id_detalles>', views.ver_mas_bicicletas, name="ver_mas_bicicletas"),
	path('ver_mas_equipamiento/<int:id_detalles>', views.ver_mas_equipamiento, name="ver_mas_equipamiento"),
	#path('detalles/<int:id_detalles>', views.detalles, name="detalles"),
]
