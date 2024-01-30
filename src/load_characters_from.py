import json
from Caract import *

def load_characters_from(file_path):
    characters=[]
    fp = open(file_path,'r',encoding='utf-8')
    char_origin = json.load(fp)
    for item in char_origin:
        characters.append(Caract(item))
    fp.close()
    return characters