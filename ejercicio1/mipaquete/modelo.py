class Empleado(object):
	def __init__(self):
		self.nombre = " "
		self.apellido = " "
		self.cedula = " "
		self.comision_fija = 0

		
	#apellidos es un nombre que yo doy, por lo tanto si funciona, aunque el nombre confunda
	#def agregar_comision_fija(self,apellidos):
		#self.comision_fija=apellidos

	def agregar_comision_fija(self,comision ):
		self.comision_fija=comision


	def obtener_comision_fija(self):
		return self.comision_fija

	def agregar_cedula(self,cedulas):
		self.cedula=cedulas

	def obtener_cedula(self):
		return self.cedula

	def agregar_apellido(self,apellidos):
		self.apellido=apellidos
	
	def obtener_apellido(self):
		return self.apellido

	def agregar_nombre(self,nombres):
		self.nombre=nombres
	
	def obtener_nombre(self):
		return self.nombre



	def presentar_datos(self):
		cadena = "Informacion de %s%s\n\t CEDULA:%s" % (self.obtener_nombre(),self.obtener_apellido(),self.obtener_cedula())
		return cadena
