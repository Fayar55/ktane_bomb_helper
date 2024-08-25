from reconocimiento_voz import obtener_entrada_por_voz

numeros_palabras_a_digitos = {
    "cero": "0",
    "uno": "1",
    "dos": "2",
    "tres": "3",
    "cuatro": "4",
    "cinco": "5",
    "seis": "6",
    "siete": "7",
    "ocho": "8",
    "nueve": "9",
    "diez": "10"
}


def validar_numero_serie(numero_serie):
    numero_serie = numero_serie.replace(" ", "")
    if len(numero_serie) != 5:
        raise ValueError("El número de serie debe tener exactamente 5 caracteres.")
    return numero_serie.upper()


def es_ultimo_digito_impar(numero_serie):
    ultimo_digito = numero_serie[-1]
    if ultimo_digito.isdigit():
        return int(ultimo_digito) % 2 != 0


def obtener_numero_serie(bomba):
    while True:
        try:
            entrada = obtener_entrada_por_voz("Introduce el número de serie: ")
            numero_serie = "".join(numeros_palabras_a_digitos.get(palabra, palabra) for palabra in entrada.split())
            numero_serie = validar_numero_serie(numero_serie)
            numero_serie = numero_serie.replace(" ", "")
            print("El número de serie es:", numero_serie)
            return numero_serie

        except ValueError as e:
            print(e)
