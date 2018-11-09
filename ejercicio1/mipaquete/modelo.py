class Empleado(object):
	def __init__(self):
		self.nombre = " "
		self.apellido = " "
		self.cedula = " "
		self.comision_fija = 0

		
	#apellidos es un nombre que yo doy, por lo tanto si funciona, aunque el nombre confunda
	#def agregar_comision_fija(self,apellidos):
		#self.comision_fija=apellidos

	def agregar_nombre(self,nombres):
		self.nombre=nombres

	def obtener_nombre(self):
		return self.nombre

	def agregar_apellido(self,apellidos):
		self.apellido=apellidos
	
	def obtener_apellido(self):
		return self.apellido

	def agregar_comision_fija(self,comision ):
		self.comision_fija=comision


	def obtener_comision_fija(self):
		return self.comision_fija

	def agregar_cedula(self,cedulas):
		self.cedula=cedulas

	def obtener_cedula(self):
		return self.cedula



	def presentar_datos(self):
		cadena = "Informacion de %s%s\n\t CEDULA:%s" % (self.obtener_nombre(),self.obtener_apellido(),self.obtener_cedula())
		return cadena


	
	
	#2

class EmpleadoPorHoras(Empleado):
	def __init__(self):
		super(EmpleadoPorHoras,self).__init__()
		self.numero_horas=0
		self.valor_hora=0


	def agregar_numero_horas(self,horas):
		self.numero_horas=horas

	def obtener_numero_horas(self):
		return self.numero_horas

	def agregar_valor_hora(self,val):
		self.valor_hora=val

	def obtener_valor_hora(self):
		return self.valor_hora



	def calcular_valor_sueldo_final(self):
		return(self.numero_horas*self.valor_hora)+self.comision_fija





	def presentar_datos(self):
		cadena = "%s Numero de horas:%s \n Valor hora:%s \n Sueldo Final:%s" % (super(EmpleadoPorHoras,self).presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_horas(),self.calcular_valor_sueldo_final())
		return cadena
	

	#3


class EmpleadoFijo(Empleado):
	def __init__(self):
		super(EmpleadoFijo,self).__init__()
		self.sueldo_fijo=0
		self.descuento_seguro=0

	
	def agregar_sueldo_fijo(self,suelfijo):
		self.sueldo_fijo=suelfijo

	def obtener_sueldo_fijo(self):
		return self.sueldo_fijo

	def agregar_descuento_seguro(self,desc):
		self.descuento_seguro=desc

	def obtener_descuento_seguro(self):
		return self.descuento_seguro


	def calcular_valor_sueldo_final(self):
		return(self.sueldo_fijo-self.descuento_seguro+self.comision_fija)


		

	def presentar_datos(self):
		cadena = "%s Sueldo Fijo:%s \n Descuento Seguro:%s \n Sueldo Final:%s \n" % (super(EmpleadoFijo,self).presentar_datos(),self.obtener_sueldo_fijo(),self.obtener_descuento_seguro(),self.calcular_valor_sueldo_final())
		return cadena


#4

class EmpleadoPorSemana(Empleado):
	def __init__(self):
		super(EmpleadoPorSemana,self).__init__()
		self.numero_semanas=0
		self.valor_semanal=0


	
	def agregar_numero_semanas(self,num_semanas):
		self.numero_semanas=num_semanas

	def obtener_numero_semanas(self):
		return self.numero_semanas

	def agregar_valor_semanal(self,val_semanal):
		self.valor_semanal=val_semanal

	def obtener_valor_semanal(self):
		return self.valor_semanal


	def calcular_valor_sueldo_final(self):
		return(self.valor_semanal*self.numero_semanas+self.comision_fija)


		

	def presentar_datos(self):
		cadena = "%s Numero de semanas:%s \n Valor Semanal:%s \n Sueldo Final:%s \n" % (super(EmpleadoPorSemana,self).presentar_datos(),self.obtener_numero_semanas(),self.obtener_valor_semanal(),self.calcular_valor_sueldo_final())
		return cadena






