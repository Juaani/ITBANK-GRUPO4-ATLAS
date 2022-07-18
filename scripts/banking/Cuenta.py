from mimetypes import init


class Cuenta:
    def __init__(self, limite_extraccion_diario: int, limite_transferencia_recibida: int,
                 costo_transferencias: float, saldo_descubierto_disponible: int):
        self.__limite_extraccion_diario = limite_extraccion_diario
        self.__limite_transferencia_recibida = limite_transferencia_recibida
        self.__monto = 0
        self.__costo_transferencias = costo_transferencias
        self.__saldo_descubierto_disponible = saldo_descubierto_disponible