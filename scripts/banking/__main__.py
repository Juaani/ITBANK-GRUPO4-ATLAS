import json
import jsonschema
from jsonschema.validators import validate

from Clientes import *

client_schema = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "apellido": {"type": "string"},
        "dni": {"type": "string"},
        "tipo": {
            "type": "string",
            "enum": [
                "CLASSIC",
                "GOLD",
                "BLACK"
            ]
        },
        "direccion": {
            "type": "object",
            "properties": {
                "calle": {"type": "string"},
                "numero": {"type": "string"},
                "ciudad": {"type": "string"},
                "provincia": {"type": "string"},
                "pais": {"type": "string"},
            }
        },
        "transacciones": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "estado": {"type": "string"},
                    "tipo": {"type": "string"},
                    "cuentaNumero": {"type": "number"},
                    "cupoDiarioRestante": {"type": "number"},
                    "cantidadExtraccionesHechas": {"type": "number"},
                    "monto": {"type": "number"},
                    "fecha": {"type": "string"},
                    "numero": {"type": "number"},
                    "saldoEnCuenta": {"type": "number"},
                    "totalTarjetasDeCreditoActualmente": {"type": "number"},
                    "totalChequerasActualmente": {"type": "number"}
                }
            }
        }
    },
    "required": ["nombre", "apellido", "dni", "tipo", "direccion", "transacciones"]
}


def valid_json(client_json):
    try:
        validate(client_json, client_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


def main():
    cliente = None
    data = None

    while cliente is None:
        while data is None:
            try:
                directorio = str(input("Ingrese el archivo JSON (sin la extension) a leer: "))
                file = open(f"../..//{directorio}.json")
                data = json.load(file)

                if not valid_json(data):
                    print("El JSON indicado no corresponde con el formato del TPS, elija otro")
                    continue
            except IOError as error:
                print(f"No se pudo leer el archivo indicado: {error}")
            except ValueError as error:
                print(f"El archivo indicado no es un JSON: {error}")

        match data["tipo"]:
            case "CLASSIC":
                cliente = Classic(
                    nombre=data["nombre"],
                    apellido=data["apellido"],
                    numero=data["numero"],
                    dni=data["dni"],
                    direccion=data["direccion"]
                )
            case "GOLD":
                cliente = Gold(
                    nombre=data["nombre"],
                    apellido=data["apellido"],
                    numero=data["numero"],
                    dni=data["dni"],
                    direccion=data["direccion"]
                )
            case "BLACK":
                cliente = Black(
                    nombre=data["nombre"],
                    apellido=data["apellido"],
                    numero=data["numero"],
                    dni=data["dni"],
                    direccion=data["direccion"]
                )

    print(f"Procesando las transacciones del Cliente N°{cliente.numero}")


if __name__ == "__main__":
    main()
