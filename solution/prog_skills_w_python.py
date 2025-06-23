# Imports


def tri(arr):
    if len(arr) <= 1:
        return arr
    # Choisir le pivot (ici, on prend le premier élément)
    pivot = arr[0]
    # Partitionner la liste en trois sous-listes
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    # Appliquer récursivement et concaténer
    return tri(less) + [pivot] + tri(greater)
