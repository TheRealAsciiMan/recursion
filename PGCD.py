def pgcd(a:int, b:int)->int:
    assert isinstance(a, int) and isinstance(b, int), "a et b doivent être des entiers"
    if b == 0:
        return a
    else:
        c = a % b
        return pgcd(b, c)

assert pgcd(256,56)==8
assert pgcd(308,758)==2

def simplifier(a:int,b:int)->tuple:
    diviser = pgcd(a,b)
    c = a/diviser
    d = b/diviser
    return (c,d)

assert simplifier(256,56)==(32,7)
assert simplifier(308,758)==(154,379)