# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

class Camion:
    
    def __init__(self, patente, marca, carga, anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
        

    def validacion_patente:
        for x in 
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
    def __eq__(self, other):
        if not isinstance(other,Camion):
            return False
        return self.marca == other.marca and self.patente==other.patente and self.carga==other.carga and self.anio==other.anio
    #Tengo que validar que cuando ingrese un camion nuevo no coincida con una patente ya cargada
    
    def validacion_patente()

    def cambiar_patente(self,patente_nueva):
       self.patente=patente_nueva

furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)
print(furgon1)

print(furgon1 == furgon2)
print(furgon1 is furgon2)
print(furgon3 == furgon4) #False
print(furgon3 is furgon4) #False
print(furgon1 == furgon4)
print('prueba')