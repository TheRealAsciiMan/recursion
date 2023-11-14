def mlist_norec(n):
    """
            Génère une liste d'entiers de n à 0.

            @args:
            - n (int): L'entier de départ pour la liste.

            @returns:
            - list: Une liste d'entiers partant de n et descendant jusqu'à 0.
        """
    assert isinstance(n, int), "L'entrée doit être un entier"
    assert n >= 0, "L'entrée doit être un entier non négatif"
    return list(range(n, -1, -1))


def mlist(n):
    """
        Génère une liste d'entiers de n à 0.

        @args:
        - n (int): L'entier de départ pour la liste.

        @returns:
        - list: Une liste d'entiers partant de n et descendant jusqu'à 0.
    """
    assert isinstance(n, int), "L'entrée doit être un entier"
    assert n >= 0, "L'entrée doit être un entier non négatif"
    if n == 0:
        return [0]
    else:
        return [n]+mlist(n-1)

assert mlist(5) == [5, 4, 3, 2, 1, 0]
assert mlist(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

