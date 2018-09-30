#diccionario playlist que contiene una lista con varios diccionarios de canciones dentro
playlist= {
    "play1": "Tiempo Libre",
    "autor": "Luciana Repetto",
    "canciones": [  
        {"cancion": "hola que tal", "autor": ["ellos"], "duracion": 8.9},
        {"cancion": "hola remix", "autor": ["ellos", "cat"], "duracion": 2.9},
        {"cancion": "hola el 2", "autor": ["aquellos"], "duracion": 3.0}

    ]
}

for cancion in playlist["canciones"]:
    print(cancion["cancion"])