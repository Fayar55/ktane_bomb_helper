# gestion_puertos.py

from reconocimiento_voz import obtener_entrada_por_voz

expected_ports = {
    "DVI-D": ["dvi"],
    "Parallel": ["paralelo", "paralelos"],
    "PS/2": ["ps2"],
    "RJ-45": ["rj45", "internet"],
    "Serial": ["serial", "serie", "puerto serie"],
    "Stereo RCA": ["rca", "estéreo rca", "estéreo"],
    "hecho": ["hecho", "acabar"]
}


def gestionar_puertos(bomba):
    puertos = {}

    while True:
        puerto = obtener_entrada_por_voz("Introduce un tipo de puerto (o 'hecho' para terminar): ", expected_ports)

        # Permitir "hecho" como indicación de terminación
        if puerto in expected_ports["hecho"]:
            break

        # Normalizar puerto a su clave principal
        normalized_port = None
        for key, synonyms in expected_ports.items():
            if puerto.lower() in [synonym.lower() for synonym in synonyms]:
                normalized_port = key
                print(f"Puerto introducido: '{normalized_port}'")
                break

        if not normalized_port:
            print(f"Puerto '{puerto}' no reconocido. Inténtalo de nuevo.")
            continue

        puertos[normalized_port] = True

    bomba.puertos = puertos
