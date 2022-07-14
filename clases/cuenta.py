class Cuenta:
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible):
        self.__limite_extraccion_diario = limite_extraccion_diario
        self.__limite_transferencia_recibida = limite_transferencia_recibida
        self.__monto = monto
        self.__costo_transferencias = costo_transferencias
        self.__saldo_descubierto_disponible = saldo_descubierto_disponible

