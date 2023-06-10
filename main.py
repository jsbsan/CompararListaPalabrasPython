from difflib import SequenceMatcher
import difflib
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    oficiales = ["Melipilla", "Melilla", "Maripul"]
    ciudades = ["Melilla", "Melipiya", "Meliya", "Meli-pilla"]
    for ciudad in ciudades:
        print(f"Ciudad: {ciudad}")
        ciudad_encontrada = None
        parecido = 0
        for oficial in oficiales:
            ptos = similar(ciudad, oficial)
            if ptos > parecido:
                parecido = ptos
                ciudad_encontrada = oficial
        print(f"Ciudad {ciudad} es {ciudad_encontrada} con similitud {parecido}")
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def comparar():
    palabra_dada = "holdaita"
    lista_palabras = ["hola", "holita", "adios", "hello"]
    palabra_mas_parecida = difflib.get_close_matches(palabra_dada, lista_palabras)[0]
    print("-------------------------------------------------------------------------")
    print("La palabra más parecida a", palabra_dada, "es", palabra_mas_parecida)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    comparar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
