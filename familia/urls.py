from django.urls import path
from familia import views



urlpatterns = [
    path('home/',views.ir_a_home, name="home"),
    path('empleados/', views.ir_a_empleados, name="empleados"),
    path('agregar_empleado/', views.agregar_empleado, name="agregar_empleado"),
    path('borrar_empleado/<identificador>', views.borrar_empleado, name="borrar_empleado"),
    path('buscar_empleado/', views.buscar_empleado, name="buscar_empleado"),
    path('clientes/', views.ir_a_clientes, name="clientes"),
    path('agregar_cliente/', views.agregar_cliente, name="agregar_cliente"),
    path('borrar_cliente/<identificador>', views.borrar_cliente, name="borrar_cliente"),
    path('buscar_cliente/', views.buscar_cliente, name="buscar_cliente"),
    path('horas_clientes/', views.ir_a_horas, name="horas_clientes"),
    path('agregar_horas/', views.agregar_horas, name="agregar_horas"),
    path('borrar_horas/<identificador>', views.borrar_horas, name="borrar_horas"),
]
