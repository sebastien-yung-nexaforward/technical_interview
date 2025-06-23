# Imports


def tri(l: list) -> list:
    for i in len(l):
        if l[i] > l[i+1]:
            tmp = l[i]
            l[i] = l[i+1]
            l[i+1] = tmp