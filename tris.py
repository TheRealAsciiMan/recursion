def tri_insertion(liste):
    j = 1
    while j<len(liste):
        i = j-1
        k = liste[j]
        while i>=0 and liste[i]>k:
            liste[i+1] = liste[i]
            i = i-1
        liste[i+1] = k
        j = j+1
    return liste

def tri_selection(liste):
    i = 0
    while i<len(liste):
        j = i+1
        min = i
        while j<len(liste):
            if liste[j]<liste[min]:
                min = j
            j = j+1
        if min != i :
            liste[i], liste[min] = liste[min], liste[i]
            i = i+1
    return liste

def tri_a_bulle(liste):
    for j in range(len(liste)-1):
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste


def fusion_algo(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1]

    L[n1] = float("inf")
    R[n2] = float("inf")

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def tri_fusion_algo(A, p, r):
    if p < r:
        q = (p + r) // 2  # Utilisation de la division entière
        tri_fusion_algo(A, p, q)
        tri_fusion_algo(A, q + 1, r)
        fusion_algo(A, p, q, r)


def fusion(liste1, liste2):
    """
    Fusionne deux listes ordonnées en une seule liste ordonnée.
    """
    resultat = []
    i, j = 0, 0

    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1

    while i < len(liste1):
        resultat.append(liste1[i])
        i += 1

    while j < len(liste2):
        resultat.append(liste2[j])
        j += 1

    return resultat

def triFusion(liste):
    """
    Trie récursivement une liste en utilisant l'algorithme de tri fusion.
    """
    if len(liste) <= 1:
        return liste

    milieu = len(liste) // 2
    liste_gauche = liste[:milieu]
    liste_droite = liste[milieu:]

    liste_gauche_triee = triFusion(liste_gauche)
    liste_droite_triee = triFusion(liste_droite)

    resultat = fusion(liste_gauche_triee, liste_droite_triee)

    return resultat