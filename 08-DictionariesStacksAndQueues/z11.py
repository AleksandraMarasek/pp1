import json

book = {
    "title":"No longer human",
    "year": 1948,
    "characters":{"main":"Oba Yozo","supporting":"others"},
    "language it was written in":"Japanese",
    "language I read it in": "English"

}

file= open("favourite.json","w")

json.dump(book, file, indent=6)

file.close()