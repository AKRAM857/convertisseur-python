
def from_celecuis_to_fahrenheit(celecuis):
    resultat=celecuis*9/5 +32
    return resultat
celecuis=float(input ('entrer la valeur tu veux la convertir: '))
resultat = from_celecuis_to_fahrenheit(celecuis)

print('la resultat est: ', resultat ) 