# gestion_indicadores.py

from reconocimiento_voz import obtener_entrada_por_voz

expected_indicators = {
    "snd": ["snd", "sándwich", "sonda"],
    "clr": ["clr", "claro"],
    "car": ["car", "carro", "cara"],
    "ind": ["ind", "índice", "industria"],
    "frq": ["frq", "frecuencia"],
    "sig": ["sig", "signo", "significar"],
    "nsa": ["nsa", "ensayar"],
    "msa": ["msa", "mesada"],
    "trn": ["trn", "entrenamiento"],
    "bob": ["bob", "bobo"],
    "frk": ["frk", "férreo"],
    "hecho": ["hecho", "acabar"]
}

def gestionar_indicadores(bomba):
    indicators = {}
    indicators_lit = {}

    while True:
        indicator = obtener_entrada_por_voz("Introduce una etiqueta de indicador (o 'hecho' para terminar): ", expected_indicators)

        if indicator in expected_indicators["hecho"]:
            break

        # Normalizar indicador a su clave principal
        normalized_indicator = None
        for key, synonyms in expected_indicators.items():
            if indicator in synonyms:
                normalized_indicator = key.upper()
                print(f"Indicador introducido: '{normalized_indicator}'")
                break

        if not normalized_indicator:
            print(f"Indicador '{indicator}' no reconocido. Inténtalo de nuevo.")
            continue

        lit = obtener_entrada_por_voz(f"¿Está el indicador {normalized_indicator} encendido? (sí/no): ").lower() == "sí"
        indicators[normalized_indicator] = True
        if lit:
            indicators_lit[normalized_indicator] = True

    bomba.indicadores = indicators
    bomba.indicadores_encendidos = indicators_lit
