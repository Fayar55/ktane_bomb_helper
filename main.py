# main.p

from bomba import BombClass
from reconocimiento_voz import obtener_entrada_por_voz

from gestion_indicadores import gestionar_indicadores  # Importamos la función
from gestion_puertos import gestionar_puertos
from gestion_numero_serie import obtener_numero_serie

from modulos.modulo_boton import manejar_modulo_boton
from modulos.modulo_cables import manejar_modulo_cables
from modulos.modulo_simbolos import manejar_modulo_simbolos
"""
from modulos.modulo_morse import manejar_modulo_morse
from modulos.modulo_cables_complicados import manejar_modulo_cables_complicados
from modulos.modulo_laberinto import manejar_modulo_laberinto
from modulos.modulo_contraseña import manejar_modulo_contraseña
from modulos.modulo_simon_says import manejar_modulo_simon_says
"""

def main():
    bomba = BombClass()
    bomba.baterias = obtener_entrada_por_voz("Introduce el número de baterías: ", es_numerico=True)

    bomba.numero_serie = obtener_numero_serie(bomba)

    gestionar_indicadores(bomba)

    gestionar_puertos(bomba)

    tipos_de_modulos = {
        "botón": ["botón", "boto", "boton", "botones"],
        "teclado": ["teclado", "tecla", "teclas"],
        "cables": ["cables", "cable", "cabo", "cables"],
        "símbolos": ["símbolos", "simbolo", "simbolos", "símbolo"],
        "morse": ["morse", "mores"],
        "cables complicados": ["cables complicados", "cable complicado", "cableados complicados"],
        "laberinto": ["laberinto", "laberinto", "laberintos"],
        "contraseña": ["contraseña", "contra", "contrasena", "contraseñas"],
        "simon says": ["simon", "dice", "simon dice"],
        "desactivado": ["desactivada", "hecho", "acabado", "acabar", "desactivado"]
    }

    while True:
        tipo_modulo = obtener_entrada_por_voz("¿Qué módulo estás desactivando? ", tipos_de_modulos)
        print(f"Módulo seleccionado: '{tipo_modulo}'")

        if tipo_modulo in tipos_de_modulos["botón"]:
            manejar_modulo_boton(bomba)
        elif tipo_modulo in tipos_de_modulos["teclado"]:
            manejar_modulo_teclado(bomba)
        elif tipo_modulo in tipos_de_modulos["cables"]:
            manejar_modulo_cables(bomba)
        elif tipo_modulo in tipos_de_modulos["símbolos"]:
            manejar_modulo_simbolos()
        elif tipo_modulo in tipos_de_modulos["morse"]:
            manejar_modulo_morse(bomba)
        elif tipo_modulo in tipos_de_modulos["cables complicados"]:
            manejar_modulo_cables_complicados(bomba)
        elif tipo_modulo in tipos_de_modulos["laberinto"]:
            manejar_modulo_laberinto(bomba)
        elif tipo_modulo in tipos_de_modulos["contraseña"]:
            manejar_modulo_contraseña(bomba)
        elif tipo_modulo in tipos_de_modulos["simon says"]:
            manejar_modulo_simon_says(bomba)
        elif tipo_modulo in tipos_de_modulos["desactivado"]:
            print("Bien hecho soldado.")
            break
        else:
            print(f"Módulo '{tipo_modulo}' no reconocido. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
