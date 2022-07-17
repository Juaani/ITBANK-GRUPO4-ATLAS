class Razon:
    def __init__(self, type):
        self.type = type

    def resolver(self, cliente, evento):
        pass

class RazonAltaChequera(Razon):
    pass

class RazonTarjetaCredito(Razon):
    pass

class RazonCompraDolar(Razon):
    pass

class RazonRetiroEfectivo(Razon):
    pass

class RazonTransferenciaEnviada(Razon):
    pass

class RazonTransferenciaRecibida(Razon):
    pass