from abc import ABC, abstractmethod

from Cuenta import Cuenta


class Cliente(ABC):
    def __init__(self, nombre: str, apellido: str, numero: int, dni: str, direccion: dict):
        self._nombre = nombre
        self._apellido = apellido
        self._numero = numero
        self._dni = dni
        self._direccion = Cliente.Direccion(
            pais=direccion["pais"],
            provincia=direccion["provincia"],
            ciudad=direccion["ciudad"],
            calle=direccion["calle"],
            numero=direccion["numero"]
        )

        self._tarjetasCredito = 0
        self._chequeras = 0

        self._cajaAhorroDolares = False

    @property
    @abstractmethod
    def _max_chequeras(self) -> int:
        pass

    @property
    @abstractmethod
    def _max_tarjetas_credito(self) -> int:
        pass

    def puede_crear_chequera(self) -> bool:
        return self._chequeras < self._max_chequeras

    def puede_crear_tarjeta_credito(self) -> bool:
        return self._tarjetasCredito < self._max_tarjetas_credito

    def puede_comprar_dolar(self) -> bool:
        return self._cajaAhorroDolares

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def dni(self) -> str:
        return self._dni

    @property
    def direccion(self) -> object:
        return self._direccion

    def __repr__(self):
        return f'Nombre: {self._nombre} || Apellido: {self._apellido} ||' \
               f' Numero: {self._numero} || DNI: {self._dni} || Direccion: [{self._direccion}] ||' \
               f' Tarjetas de Credito: {self._tarjetasCredito} || Chequeras: {self._chequeras}'

    class Direccion:
        def __init__(self, pais: str, provincia: str, ciudad: str, calle: str, numero: str):
            self._pais = pais
            self._provincia = provincia
            self._ciudad = ciudad
            self._calle = calle
            self._numero = numero

        def validate(self) -> bool:
            if type(self.pais) == str:
                if type(self._provincia) == str:
                    if type(self._ciudad) == str:
                        if type(self._calle) == str:
                            if type(self._numero) == str:
                                return True
            else:
                return False

        def __repr__(self):
            return f'Pais: {self.pais} || Provincia: {self._provincia} ||' \
                   f' Ciudad: {self._ciudad} || Calle: {self._calle} {self._numero}'

        @property
        def pais(self) -> str:
            return self._pais

        @property
        def provincia(self) -> str:
            return self._provincia

        @property
        def ciudad(self) -> str:
            return self._ciudad

        @property
        def calle(self) -> str:
            return self._calle

        @property
        def numero(self) -> str:
            return self._numero


class Classic(Cliente):
    # Tiene una sola tarjeta de debito, creada junto al cliente
    # Tiene una caja de ahorro en pesos, pero no una en dolares, por ende no puede comprar USD
    # Solo puede retirar $10.000 por dia
    # No tiene acceso a tarjetas de credito, ni chequeras
    # La comision por transferencia es del 1%
    # No puede recibir transferencias mayores a $150.000 sin previo aviso

    def __init__(self, nombre: str, apellido: str, numero: int, dni: str, direccion: dict):
        super().__init__(nombre, apellido, numero, dni, direccion)

        self._cuenta = Cuenta(
            limite_extraccion_diario=10000,
            limite_transferencia_recibida=150000,
            costo_transferencias=1.0,
            saldo_descubierto_disponible=0
        )
        self._cajaAhorroDolares = True
        self._cuentaCorriente = True

    def _max_chequeras(self) -> int:
        return 0

    def _max_tarjetas_credito(self) -> int:
        return 0


class Gold(Cliente):
    # Tiene una tarjeta de debito, creada junto al cliente
    # Tiene una cuenta corriente con un descubierto de $10.000, es decir, puede tener hasta -$10.000
    # Tiene caja de ahorro en dolares
    # Solo puede retirar $20.000 por dia
    # Puede tener una sola tarjeta de credito
    # Puede tener una sola chequera
    # La comision por transferencia es del 0,5%
    # No puede recibir transferencias mayores a $500.000 sin previo aviso

    def __init__(self, nombre: str, apellido: str, numero: int, dni: str, direccion: dict):
        super().__init__(nombre, apellido, numero, dni, direccion)

        self._maxTarjetasCredito = 1
        self._maxChequeras = 1

        self._cuenta = Cuenta(
            limite_extraccion_diario=20000,
            limite_transferencia_recibida=500000,
            costo_transferencias=0.5,
            saldo_descubierto_disponible=10000
        )
        self._cajaAhorroDolares = True
        self._cuentaCorriente = True

    @property
    def _max_chequeras(self) -> int:
        return 1

    @property
    def _max_tarjetas_credito(self) -> int:
        return 1


class Black(Cliente):
    # Tiene una caja de ahorro en pesos, cuenta corriente en pesos, y una caja de ahorro en dolares
    # Su cuenta corriente tiene un descubierto de $10.000, es decir, puede tener hasta -$10.000
    # Solo puede retirar $100.000 por dia
    # Puede tener hasta 5 tarjetas de credito
    # Puede tener hasta dos chequeras
    # No aplican comisiones por transferencia
    # No aplican restricciones para recibir transferencias

    def __init__(self, nombre: str, apellido: str, numero: int, dni: str, direccion: dict):
        super().__init__(nombre, apellido, numero, dni, direccion)

        self._maxTarjetasCredito = 5
        self._maxChequeras = 2

        self._cuenta = Cuenta(
            limite_extraccion_diario=100000,
            limite_transferencia_recibida=0,
            costo_transferencias=0.0,
            saldo_descubierto_disponible=10000
        )
        self._cajaAhorroDolares = True

    @property
    def _max_chequeras(self) -> int:
        return 2

    @property
    def _max_tarjetas_credito(self) -> int:
        return 5
