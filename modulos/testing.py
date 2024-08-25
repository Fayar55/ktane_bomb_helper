def find_ordered_target_in_sublists(list_of_lists, target_list):
    for sublist in list_of_lists:
        # Check if all elements in target_list are in the sublist
        if all(elem in sublist for elem in target_list):
            # Find and return the elements of target_list in the order they appear in the sublist
            ordered_target = [elem for elem in sublist if elem in target_list]
            return ordered_target
    return None  # Return None if no sublist contains all elements of target_list

# Example usage:
list_of_lists = [
    ["globo", "arroba", "lambda", "rayo", "gatito", "cursiva", "c izquierda"],
    ["euro", "globo", "c izquierda", "cola de cerdo", "estrella blanca", "cursiva", "signo de interrogación"],
    ["derechos_de_autor", "culo", "cola de cerdo", "doble k", "media tres", "lambda", "estrella blanca"],
    ["seis", "párrafo", "b", "gatito", "doble k", "interrogación", "cara feliz"],
    ["horca", "cara feliz", "b", "c derecha", "párrafo", "dragón", "estrella negra"],
    ["seis", "euro", "costura", "ceniza", "horca", "letra n", "omega"]
]
target_list = ["b", "horca", "dragón", "párrafo"]

result = find_ordered_target_in_sublists(list_of_lists, target_list)