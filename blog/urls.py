from django.urls import path
from . import views
urlpatterns=[
    path('',views.listar_pub,name='listar_pub'),
    path('publicacion/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('publicacion/nuevo', views.nuevo_pub, name='nuevo_pub'),
    path('publicacion/<int:pk>/editar/', views.editar_pub, name='editar_pub'),
]