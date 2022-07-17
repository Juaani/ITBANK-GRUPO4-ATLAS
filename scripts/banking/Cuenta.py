from mimetypes import init


class Cuenta:
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible):
        self.__limite_extraccion_diario = limite_extraccion_diario
        self.__limite_transferencia_recibida = limite_transferencia_recibida
        self.__monto = monto
        self.__costo_transferencias = costo_transferencias

class CuentaCorriente(Cuenta):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible, maximo_monto_negativo):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias)
        self.maximo_monto_negativo=maximo_monto_negativo
        self.saldo_descubierto_disponible=saldo_descubierto_disponible

class CuentaAhorroDolares(Cuenta):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias)


class CuentaAhorroPesos(Cuenta):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias)

