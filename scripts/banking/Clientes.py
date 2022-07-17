from abc import ABC, abstractmethod

from Cuenta import Cuenta


class Cliente(ABC):
    def __init__(self, nombre: str, apellido: str, numero: int, dni: int, direccion: dict):
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

        self._cuentas = {
            "cajaAhorroPesos": None,
            "cajaAhorroDolares": None,
            "cuentaCorriente": None,
        }

    @property
    @abstractmethod
    def _max_chequeras(self) -> int:
        pass

    @property
    @abstractmethod
    def _max_tarjetas_credito(self) -> int:
        pass

    @abstractmethod
    def puede_crear_chequera(self) -> bool:
        pass

    @abstractmethod
    def puede_crear_tarjeta_credito(self) -> bool:
        pass

    def puede_comprar_dolar(self) -> bool:
        return self._cuentas["cajaAhorroDolares"] is not None

    class Direccion:
        def __init__(self, pais: str, provincia: str, ciudad: str, calle: str, numero: int):
            self.pais = pais
            self.provincia = provincia
            self.ciudad = ciudad
            self.calle = calle
            self.numero = numero

        def validate(self) -> bool:
            if type(self.pais) == str:
                if type(self.provincia) == str:
                    if type(self.ciudad) == str:
                        if type(self.calle) == str:
                            if type(self.numero) == int:
                                return True
            else:
                return False

        def __repr__(self):
            return f'Pais: {self.pais} || Provincia: {self.provincia} ||' \
                   f' Ciudad: {self.ciudad} || Calle: {self.calle} {self.numero}'


class Classic(Cliente):
    # Tiene una sola tarjeta de debito, creada junto al cliente
    # Tiene una caja de ahorro en pesos, pero no una en dolares, por ende no puede comprar USD
    # Solo puede retirar $10.000 por dia
    # No tiene acceso a tarjetas de credito, ni chequeras
    # La comision por transferencia es del 1%
    # No puede recibir transferencias mayores a $150.000 sin previo aviso

    def __init__(self, nombre: str, apellido: str, numero: int, dni: int, direccion: dict):
        super().__init__(self, nombre, apellido, numero, dni, direccion)

        self._cuentas["cajaAhorroPesos"] = Cuenta(10000, 150000, 1.0, 0)

    def _max_chequeras(self) -> int:
        return 0

    def _max_tarjetas_credito(self) -> int:
        return 0

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_credito(self) -> bool:
        return False


class Gold(Cliente):
    # Tiene una tarjeta de debito, creada junto al cliente
    # Tiene una cuenta corriente con un descubierto de $10.000, es decir, puede tener hasta -$10.000
    # Tiene caja de ahorro en dolares
    # Solo puede retirar $20.000 por dia
    # Puede tener una sola tarjeta de credito
    # Puede tener una sola chequera
    # La comision por transferencia es del 0,5%
    # No puede recibir transferencias mayores a $500.000 sin previo aviso

    def __init__(self, nombre: str, apellido: str, numero: int, dni: int, direccion: dict):
        super().__init__(self, nombre, apellido, numero, dni, direccion)

        self._maxTarjetasCredito = 1
        self._maxChequeras = 1

        self._cuentas["cajaAhorroPesos"] = Cuenta(20000, 500000, 0.5, 10000)
        self._cuentas["cajaAhorroDolares"] = Cuenta(20000, 500000, 0.5, 10000)
        self._cuentas["cuentaCorriente"] = Cuenta(20000, 500000, 0.5, 10000)

    @property
    def _max_chequeras(self) -> int:
        return 1

    @property
    def _max_tarjetas_credito(self) -> int:
        return 1

    def puede_crear_chequera(self) -> bool:
        return self._chequeras < self._max_chequeras

    def puede_crear_tarjeta_credito(self) -> bool:
        return self._tarjetasCredito < self._max_tarjetas_credito


class Black(Cliente):
    # Tiene una caja de ahorro en pesos, cuenta corriente en pesos, y una caja de ahorro en dolares
    # Su cuenta corriente tiene un descubierto de $10.000, es decir, puede tener hasta -$10.000
    # Solo puede retirar $100.000 por dia
    # Puede tener hasta 5 tarjetas de credito
    # Puede tener hasta dos chequeras
    # No aplican comisiones por transferencia
    # No aplican restricciones para recibir transferencias

    def __init__(self, nombre: str, apellido: str, numero: int, dni: int, direccion: dict):
        super().__init__(self, nombre, apellido, numero, dni, direccion)

        self._maxTarjetasCredito = 5
        self._maxChequeras = 2

        self._cuentas["cajaAhorroPesos"] = Cuenta(100000, None, None, 10000)
        self._cuentas["cajaAhorroDolares"] = Cuenta(100000, None, None, 10000)
        self._cuentas["cuentaCorriente"] = Cuenta(100000, None, None, 10000)

    @property
    def _max_chequeras(self) -> int:
        return 2

    @property
    def _max_tarjetas_credito(self) -> int:
        return 5

    def puede_crear_chequera(self) -> bool:
        return self._chequeras < self._max_chequeras

    def puede_crear_tarjeta_credito(self) -> bool:
        return self._tarjetasCredito < self._max_tarjetas_credito
