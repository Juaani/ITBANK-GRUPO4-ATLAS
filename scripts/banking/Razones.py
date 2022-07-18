import json

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

with open("eventos_classic.json", "r") as classic:
    c = json.load(classic)
    for transaccion in c["transacciones"]:
        # print(transaccion,"\n")
        def demasiado_retiro():
            if int(transaccion["monto"]) > int(transaccion["cupoDiarioRestante"]):
                return "Peticion de extraccion de dinero mayor al disponible.\n"
        if transaccion["estado"] == "ACEPTADA":
            print("\n")
            for key in transaccion:
                print(key.capitalize(),":  " ,transaccion[key])
                 
        
        if str(transaccion["estado"]) == "RECHAZADA":
            print("\n\n[-] Transaccion rechazada.")


# with open("eventos_gold.json", "r") as gold:
#     g = json.load(gold)
#     for transaccion in g["transacciones"]:
#         print(transaccion,"\n")
#         def demasiado_retiro():
#             if int(transaccion["monto"]) > int(transaccion["cupoDiarioRestante"]):
#                 return "Peticion de extraccion de dinero mayor al disponible.\n"

#             if str(transaccion["estado"]) == "RECHAZADA":
#                 print("\n\n[-] Transaccion rechazada. Razon: ", demasiado_retiro(),"\n\n")


# with open("eventos_black.json", "r") as black:
#     b = json.load(black)
#     for transaccion in b["transacciones"]:
#         print(transaccion,"\n")
#         def demasiado_retiro():
#             if int(transaccion["monto"]) > int(transaccion["cupoDiarioRestante"]):
#                 return "Peticion de extraccion de dinero mayor al disponible.\n"

#             if str(transaccion["estado"]) == "RECHAZADA":
#                 print("\n\n[-] Transaccion rechazada. Razon: ", demasiado_retiro(),"\n\n")