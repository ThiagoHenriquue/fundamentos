

mercado = {
    "Arroz" : 10.25,
    "Feijao" : 8.90,
    "Macarrao" : 6.75,
}

print(mercado)
print(max(mercado, key=mercado.get))

media = sum(mercado.values()) / len(mercado)
print(media)