from reconocimiento_voz import obtener_entrada_por_voz

simbolos_finales = []

expected_symbols = {
    "derechos de autor": ["copy", "copyright", "derechos"],
    "estrella negra": ["estrella negra", "estrella llena", "estrella negro"],
    "estrella blanca": ["estrella hueca", "estrella vacía", "estrella blanca", "estrella blanco"],
    "cara feliz": ["cara feliz", "smiley", "feliz"],
    "doble k": ["doble k", "k doble"],
    "omega": ["omega"],
    "calamar cuchillo": ["calamar cuchillo", "cuchillo calamar", "nave espacial", "cohete"],
    "calabaza": ["calabaza", "polla", "cojones"],
    "gancho n": ["gancho n", "n gancho", "perro"],
    "seis": ["seis"],
    "garabato n": ["garabato n", "n torcida"],
    "arroba": ["at", "ta", "arroba"],
    "ae": ["ae", " AE", "A E"],
    "tres derretido": ["tres derretido", "tres roto", "NH"],
    "euro": ["euro", "e dos puntos"],
    "enye con sombrero": ["n con sombrero", "enye con sombrero"],
    "dragón": ["dragón", "tres con cola", "tres con cuernos"],
    "signo de interrogación": ["signo de interrogación", "interrogación"],
    "párrafo": ["párrafo", "nota musical", "nota"],
    "c derecha": ["c derecha", "derecha c", "c normal", "c punto", "C derecha"],
    "c izquierda": ["C izquierda", "izquierda c", "c punto revés", "c del revés"],
    "horca": ["horca", "tridente", "orca"],
    "cursiva": ["cursiva", "loop"],
    "vías": ["vías", "huellas", "hashtag"],
    "globo": ["globo", "o con polla"],
    "y al revés": ["y al revés", "y volteada", "y del revés"],
    "bt": ["bt", "tb", "b con t"]
}

soluciones = [
    ["globo", "arroba", "lambda", "rayo", "gatito", "cursiva", "c izquierda"],
    ["euro", "globo", "c izquierda", "cola de cerdo", "estrella blanca", "cursiva", "signo de interrogación"],
    ["derechos de autor", "culo", "cola de cerdo", "doble k", "media tres", "lambda", "estrella blanca"],
    ["seis", "párrafo", "b", "gatito", "doble k", "interrogación", "cara feliz"],
    ["horca", "cara feliz", "b", "c derecha", "párrafo", "dragón", "estrella negra"],
    ["seis", "euro", "costura", "ceniza", "horca", "letra n", "omega"]
]


def find_ordered_target_in_sublists(list_of_lists, target_list):
    for sublist in list_of_lists:
        if all(elem in sublist for elem in target_list):
            ordered_target = [elem for elem in sublist if elem in target_list]
            return ordered_target
    return None  # Return None if no sublist contains all elements of target_list


def manejar_modulo_simbolos():
    while True:
        simbolo_en_pantalla = obtener_entrada_por_voz("Introduce los simbolos")

        # Normalizar indicador a su clave principal
        normalized_simbolo_pantalla = None
        for key, synonyms in expected_symbols.items():
            if simbolo_en_pantalla in synonyms:
                normalized_simbolo_pantalla = key
                print(f"Símbolo introducido: '{normalized_simbolo_pantalla}'")
                break

        if not normalized_simbolo_pantalla:
            print(f"Símbolo '{simbolo_en_pantalla}' no reconocido. Inténtalo de nuevo.")
            continue
        simbolos_finales.append(normalized_simbolo_pantalla)
        print("Símbolos: ", simbolos_finales)
        if len(simbolos_finales) == 4:
            solucion_final = find_ordered_target_in_sublists(soluciones, simbolos_finales)
            if solucion_final is not None:
                print("La solución és: " + ", ".join(solucion_final), ".")
            else:
                print("Esa combinación no es posible")
            break
        else:
            continue
