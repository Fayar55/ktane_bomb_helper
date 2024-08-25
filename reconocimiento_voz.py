import speech_recognition as sr

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


def obtener_entrada_por_voz(prompt, valores_esperados=None, es_numerico=False, max_caracteres=None):
    reconocedor = sr.Recognizer()
    microfono = sr.Microphone()

    while True:
        print(prompt)
        with microfono as fuente:
            reconocedor.adjust_for_ambient_noise(fuente)
            audio = reconocedor.listen(fuente)

        try:
            respuesta = reconocedor.recognize_google(audio, language='es-ES')
            respuesta_original = respuesta  # Guarda la respuesta original para posibles errores

            # Convertir palabras a números si es necesario
            if es_numerico:
                respuesta = respuesta.lower()
                if respuesta in numeros_palabras_a_digitos:
                    respuesta = numeros_palabras_a_digitos[respuesta]
                elif not respuesta.isdigit():
                    print("Eso no es un número. Por favor di un número válido.")
                    continue

            # Verificar si la respuesta está en valores esperados
            #if valores_esperados and respuesta not in valores_esperados:
             #   print(f"Por favor, proporciona uno de los siguientes valores: {', '.join(valores_esperados)}.")
              #  continue

            print("Has dicho:", respuesta_original)
            return respuesta
        except sr.UnknownValueError:
            print("Lo siento, no he entendido eso. Por favor, inténtalo de nuevo.")
        except sr.RequestError:
            print("Lo siento, mi servicio de reconocimiento de voz está caído.")
            return None