from uuid import uuid1
from random import randint
import random

class Patinador:
    def __init__(self, nombre_completo, modalidad):
        # Seccion de declaracion de atributos
        self.nombre, self.apellido = nombre_completo.split()
        self.modalidad = modalidad
        self.protecciones = 0
        self.hidratantes = 0
        self.ciencias = 0
        self.precio = 0

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre_completo):
        if not isinstance(nombre_completo, str):
            raise Exception("El nombre no corresponde al tipo de dato esperado")
        self.nombre = nombre_completo

    def getModalidad(self):
        return self.modalidad
    def setModalidad(self, modalidad):
        if not isinstance(modalidad, str):
            raise Exception("La modalidad no corresponde al tipo de dato esperado")
        self.modalidad = modalidad

    def precioProtecciones(self, opciones):
        precioAcumulado = 0
        if opciones[0]:
            precioAcumulado += 20000
        if opciones[1]:
            precioAcumulado += 40000
        if opciones[2]:
            precioAcumulado += 70000
        self.protecciones = precioAcumulado
    def precioCiencias(self, opcion):
        if opcion:
            self.ciencias = 100000
        else:
            self.ciencias = 0
    def precioHidratantes(self, cantidad):
        self.hidratantes = 3500 * cantidad

    def calcularPrecioF(self):
        self.precio = self.protecciones + self.ciencias + self.hidratantes

    def __str__(self):
        return str({
            'Nombre': self.nombre,
            'Apellido': self.apellido,
            'Modalidad': self.modalidad,
            'Precio Final': self.precio
        })
def main():
    d1 = Patinador('Gabriela Rueda', 'Velocidad')
    d2 = Patinador('Diego Amaya','Hielo')
    d3 = Patinador(str(uuid1())+' '+str(uuid1()), str(uuid1()))

    d1.precioProtecciones([True, True, True])
    d1.precioCiencias(True)
    d1.precioHidratantes(2)
    d1.calcularPrecioF()

    d2.precioProtecciones([False, False, False])
    d2.precioCiencias(False)
    d2.precioHidratantes(0)
    d2.calcularPrecioF()

    d3.precioProtecciones([random.choice([True, False]), False, True])
    d3.precioCiencias(True)
    d3.precioHidratantes(randint(1, 100))
    d3.calcularPrecioF()

    print(d1)
    print(d2)
    print(d3)
main()
