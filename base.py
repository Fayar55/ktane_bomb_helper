import speech_recognition as sr

class BombClass:
    def __init__(self):
        self.baterias = 0
        self.numero_serie = ""
        self.indicadores = {}
        self.indicadores_encendidos = {}

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
    print("Temporizador en: " + str(numero))

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

def obtener_entrada_por_voz(prompt, valores_esperados=None, es_numerico=False):
    reconocedor = sr.Recognizer()
    microfono = sr.Microphone()

    numeros_palabras_a_digitos = {
        "cero": 0,
        "uno": 1,
        "dos": 2,
        "tres": 3,
        "cuatro": 4,
        "cinco": 5,
        "seis": 6,
        "siete": 7,
        "ocho": 8,
        "nueve": 9,
        "diez": 10
    }

    print(prompt)
    with microfono as fuente:
        reconocedor.adjust_for_ambient_noise(fuente)
        audio = reconocedor.listen(fuente)

    try:
        respuesta = reconocedor.recognize_google(audio, language='es-ES')
        print("Has dicho: " + respuesta)

        if es_numerico:
            try:
                if respuesta.lower() in numeros_palabras_a_digitos:
                    return numeros_palabras_a_digitos[respuesta.lower()]
                return int(respuesta)
            except ValueError:
                print("Por favor, introduce un número válido.")
                return obtener_entrada_por_voz(prompt, valores_esperados, es_numerico)

        respuesta_limpia = ''.join(respuesta.split()).lower()
        print(f"Limpieza de respuesta: '{respuesta_limpia}'")

        if valores_esperados:
            valores_esperados_normalizados = {valor.lower() for valores in valores_esperados.values() for valor in valores}
            print(f"Comparando con valores esperados: {valores_esperados_normalizados}")
            if respuesta_limpia not in valores_esperados_normalizados:
                print(f"Valores esperados: {', '.join(valores_esperados_normalizados)}")
                return obtener_entrada_por_voz(prompt, valores_esperados, es_numerico)

        return respuesta_limpia
    except sr.UnknownValueError:
        print("Lo siento, no he entendido eso.")
        return obtener_entrada_por_voz(prompt, valores_esperados, es_numerico)
    except sr.RequestError:
        print("Lo siento, mi servicio de reconocimiento de voz está caído.")
        return None

def main():
    bomba = BombClass()
    bomba.baterias = obtener_entrada_por_voz("Introduce el número de baterías: ", es_numerico=True)
    bomba.numero_serie = obtener_entrada_por_voz("Introduce el número de serie: ")

    tipos_de_modulos = {
        "botón": ["botón", "boto", "boton", "botones"],
        "teclado": ["teclado", "tecla", "teclas"],
        "cables": ["cables", "cable", "cabo", "cables"],
        "símbolos": ["símbolos", "simbolo", "simbolos", "símbolo"],
        "morse": ["morse", "mores"],
        "cables complicados": ["cables complicados", "cable complicado", "cableados complicados"],
        "laberinto": ["laberinto", "laberinto", "laberintos"],
        "contraseña": ["contraseña", "contra", "contrasena", "contraseñas"],
        "simon says": ["simon", "dice", "simon dice"]
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
            manejar_modulo_simbolos(bomba)
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
        else:
            print(f"Módulo '{tipo_modulo}' no reconocido. Inténtalo de nuevo.")

def manejar_modulo_boton(bomba):
    color = obtener_entrada_por_voz("Introduce el color del botón (o 'salir' para terminar): ").capitalize()
    if color.lower() == "salir":
        return
    texto = obtener_entrada_por_voz("Introduce el texto del botón: ").capitalize()
    boton(bomba, color, texto)
    tira = obtener_entrada_por_voz("Introduce el color de la tira: ").capitalize()
    respuesta_boton(tira)

def manejar_modulo_teclado(bomba):
    # Implementación del manejo del módulo de teclado
    print("Manejando módulo de teclado...")

def manejar_modulo_cables(bomba):
    # Implementación del manejo del módulo de cables
    print("Manejando módulo de cables...")

def manejar_modulo_simbolos(bomba):
    # Implementación del manejo del módulo de símbolos
    print("Manejando módulo de símbolos...")

def manejar_modulo_morse(bomba):
    # Implementación del manejo del módulo de código Morse
    print("Manejando módulo de código Morse...")

def manejar_modulo_cables_complicados(bomba):
    # Implementación del manejo del módulo de cables complicados
    print("Manejando módulo de cables complicados...")

def manejar_modulo_laberinto(bomba):
    # Implementación del manejo del módulo de laberinto
    print("Manejando módulo de laberinto...")

def manejar_modulo_contraseña(bomba):
    # Implementación del manejo del módulo de contraseña
    print("Manejando módulo de contraseña...")

def manejar_modulo_simon_says(bomba):
    # Implementación del manejo del módulo de Simon Says
    print("Manejando módulo de Simon Says...")

if __name__ == "__main__":
    main()