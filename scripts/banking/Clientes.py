from abc import ABC, abstractmethod, abstractproperty
from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, apellido, numero, dni, direccion):
        self._nombre = nombre
        self._apellido = apellido
        self._numero = numero
        self._dni = dni
        self._direccion = direccion

    @abstractmethod
    def puede_crear_chequera(self):
        pass

    @abstractmethod
    def puede_crear_tarjeta_credito(self):
        pass

    @abstractmethod
    def puede_comprar_dolar(self):
        pass

    class Direccion:
        def __init__(self, pais, provincia, ciudad, calle, numero):
            self.pais = pais
            self.provincia = provincia
            self.ciudad = ciudad
            self.calle = calle
            self.numero = numero

        def validate(self, direccion):
            if self.pais == direccion.pais:
                if self.provincia == direccion.provincia:
                    if self.ciudad == direccion.ciudad:
                        if self.calle == direccion.calle:
                            if self.numero == direccion.numero:
                                return False
            else:
                return False

class Classic(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion):
        super().__init__(self, nombre, apellido, numero, dni, direccion)

    def puede_crear_chequera(self):
        return False

    def puede_crear_tarjeta_credito(self):
        return False

    def puede_comprar_dolar(self):
        return False

class Gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion):
        super().__init__(self, nombre, apellido, numero, dni, direccion)

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True

class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion):
        super().__init__(self, nombre, apellido, numero, dni, direccion)

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True