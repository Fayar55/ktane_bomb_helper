# modulos/modulo_boton.py

from reconocimiento_voz import obtener_entrada_por_voz


def accion_boton(accion):
    if accion == 1:
        print("MANTENER")
    else:
        print("PRESIONAR Y SOLTAR")


def respuesta_boton(color):
    if color == "Azul":
        numero = 4
    elif color == "Amarillo":
        numero = 5
    else:
        numero = 1
    print("Temporizador en:", numero)


def boton(bomba, color, texto):
    if color == "Azul" and texto == "Abortar":
        accion_boton(1)
    elif bomba.baterias > 1 and texto == "Detonar":
        accion_boton(0)
    elif color == "Blanco" and "CAR" in bomba.indicadores:
        accion_boton(1)
    elif bomba.baterias > 2 and bomba.indicadores_encendidos:
        accion_boton(0)
    elif color == "Amarillo":
        accion_boton(1)
    elif color == "Rojo" and texto == "Mantener":
        accion_boton(0)
    else:
        accion_boton(1)


def manejar_modulo_boton(bomba):
    color = obtener_entrada_por_voz("Introduce el color del botón (o 'salir' para terminar): ").capitalize()
    if color.lower() == "salir":
        return
    texto = obtener_entrada_por_voz("Introduce el texto del botón: ").capitalize()
    boton(bomba, color, texto)
    tira = obtener_entrada_por_voz("Introduce el color de la tira: ").capitalize()
    respuesta_boton(tira)
