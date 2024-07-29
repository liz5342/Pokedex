import requests

def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def mostrar_datos_pokemon(pokemon):
    print(f"\nNombre: {pokemon['name'].capitalize()}")
    print(f"Peso: {pokemon['weight']} hectogramos")
    print(f"Tamaño: {pokemon['height']} decímetros")
    print("Tipos:", ', '.join([tipo['type']['name'] for tipo in pokemon['types']]))
    print("Habilidades:", ', '.join([habilidad['ability']['name'] for habilidad in pokemon['abilities']]))
    print("Movimientos:", ', '.join([movimiento['move']['name'] for movimiento in pokemon['moves'][:5]]))  # Solo mostramos los primeros 5 movimientos para simplificar

def mostrar_imagen_pokemon(pokemon):
    imagen_url = pokemon['sprites']['front_default']
    if imagen_url:
        print(f"Imagen: {imagen_url}")
    else:
        print("No se encontró imagen para este Pokémon.")

def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    datos_pokemon = obtener_datos_pokemon(nombre_pokemon)
    
    if datos_pokemon:
        mostrar_datos_pokemon(datos_pokemon)
        mostrar_imagen_pokemon(datos_pokemon)
    else:
        print("Error: Pokémon no encontrado.")

if __name__ == "__main__":
    main()
