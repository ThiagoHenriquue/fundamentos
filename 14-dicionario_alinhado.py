import pprint


filmsDict = {
    "Inception" : {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interistellar": {
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "the dark knight": {
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Drama", "Action", "Crime"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informacao dentro de um dicionario alinhado 
print(filmsDict["interistellar"]["genre"])

# 2 - Adicinar novo item 
filmsDict["Inception"]["director"] = "Christopher Nolan"
print(filmsDict["Inception"])

# 3 - Excluir um dicionario 
del filmsDict["the dark knight"]
pp.pprint(filmsDict)