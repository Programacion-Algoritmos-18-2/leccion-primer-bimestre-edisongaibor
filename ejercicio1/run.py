#Crear Empleado
from mipaquete.modelo import *
#1
e = Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("11000111")
print(e.presentar_datos())
#2
e1=EmpleadoPorHoras()
nombre = input("Ingrese su nombre:\n")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.cedula="112233"
e1.agregar_valor_horas(20.2)
e1.agregar_numero_horas(15)
print(e1.presentar_datos())
#3
e2=EmpleadoFijo()
e2.agregar_sueldo_fijo(300.2)
e2.descuento_seguro = (10)
comision = input ("Ingresar comision:")
comision = float (comision)
e2.agregar_comision_fija(comision)
e2.nombre = "Ana"
e2.apellido = "Diana"
print(e2.presentar_datos())
#4

