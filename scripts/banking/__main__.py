import json
from Clientes import *


def main():
    cliente = None
    data = None

    while cliente is None:
        directorio = None
        while data is None:
            try:
                directorio = str(input("Ingrese el archivo JSON a leer: "))
                file = open(f"../..//{directorio}")
                data = json.load(file)
            except IOError:
                print(f"No se pudo leer el archivo: {directorio}")
            except ValueError:
                print("El archivo indicado no es un JSON valido")

        try:
            match data["tipo"]:
                case "CLASSIC":
                    cliente = Classic(data["nombre"], data["apellido"], data["numero"], data["DNI"], data["direccion"])
                case "GOLD":
                    Gold(data["nombre"], data["apellido"], data["numero"], data["DNI"], data["direccion"])
                case "BLACK":
                    Black(data["nombre"], data["apellido"], data["numero"], data["DNI"], data["direccion"])
        except KeyError:
            print("El tipo de Cliente es invalido")


if __name__ == "__main__":
    main()