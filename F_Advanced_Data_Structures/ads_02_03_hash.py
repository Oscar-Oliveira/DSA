"""
Hash table - Search engine
"""

import string
import ads_02_00_DB as DB
from B_Data_Structures.hashtable import HashTable

HashTable.SIZE = 20

def search(search_engine, word):
    print()
    print("Search word:", word)
    matches = search_engine.get(word)
    if matches:
        for page in matches:
            print("-", page)
    else:
        print("No page(s) found.")

def strip_puntuation(word):
    return word.translate(str.maketrans({key: None for key in string.punctuation}))

def main():

    search_engine = HashTable()
    for page in DB.WEB:
        for word in page["desc"].split():
            word = strip_puntuation(word)
            search_engine.insert(word, [])
            (search_engine.get(word)).append(page["url"])

    print("------------------------------------------------------------------")
    print("Guugle------------------------------------------------------------")
    print("------------------------------------------------------------------")

    search(search_engine, "dog")

    search(search_engine, "tech")

    print("\n------------------------------------------------------------------")

    print(search_engine)

if __name__ == "__main__":
    main()
    print("Done!!")
