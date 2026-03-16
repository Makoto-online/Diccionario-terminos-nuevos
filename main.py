meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Emoji que representa risa interminable",
            "GHOSTEADO": "Es cuando un individuo deja de responder a tus mensajes de texto"
            }

print("Palabras en el diccionario", meme_dict.keys())
word = input("Ingresa la Palabra que quieras ingresar:").upper()#upper es para que todo lo que este en minusculla se ponga a mayuscula de misma forma funciona el lower

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no ha sido añadida en este diccionario")
