from reconocimiento_voz import obtener_entrada_por_voz


def manejar_modulo_cables(bomba):
    print("Los cables disponibles son: rojo, azul, blanco, amarillo y negro.")

    cables = obtener_entrada_por_voz("Por favor, indica los colores de los cables separados por espacios: ").lower()
    cables = cables.split()

    # Validar que los cables ingresados sean válidos
    colores_validos = ["rojo", "azul", "verde", "blanco", "amarillo", "negro"]
    for cable in cables:
        if cable not in colores_validos:
            print(f"Color de cable '{cable}' no válido. Por favor, inténtalo de nuevo.")
            return

    # Lógica para determinar cuál cable cortar
    num_cables = len(cables)
    if num_cables == 3:
        if "rojo" not in cables:
            print("Corta el segundo cable.")
        elif cables[-1] == "blanco":
            print("Corta el último cable.")
        elif cables.count("azul") > 1:
            print("Corta el último cable azul.")
        else:
            print("Corta el último cable.")
    elif num_cables == 4:
        if cables.count("rojo") > 1 and bomba.numero_serie[-1].isdigit() and int(bomba.numero_serie[-1]) % 2 == 1:
            print("Corta el último cable rojo.")
        elif cables[-1] == "amarillo" and "rojo" not in cables:
            print("Corta el primer cable.")
        elif cables.count("azul") == 1:
            print("Corta el primer cable.")
        elif cables.count("amarillo") > 1:
            print("Corta el último cable.")
        else:
            print("Corta el segundo cable.")
    elif num_cables == 5:
        if cables[-1] == "negro" and bomba.numero_serie[-1].isdigit() and int(bomba.numero_serie[-1]) % 2 == 1:
            print("Corta el cuarto cable.")
        elif cables.count("rojo") == 1 and cables.count("amarillo") > 1:
            print("Corta el primer cable.")
        elif "negro" not in cables:
            print("Corta el segundo cable.")
        else:
            print("Corta el primer cable.")
    elif num_cables == 6:
        if "amarillo" not in cables and bomba.numero_serie[-1].isdigit() and int(bomba.numero_serie[-1]) % 2 == 1:
            print("Corta el tercer cable.")
        elif cables.count("amarillo") == 1 and cables.count("blanco") > 1:
            print("Corta el cuarto cable.")
        elif "rojo" not in cables:
            print("Corta el último cable.")
        else:
            print("Corta el cuarto cable.")
    else:
        print("Número de cables no válido. Verifica las conexiones y vuelve a intentarlo.")

    print("Módulo de cables desactivado.")