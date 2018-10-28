"""
Tries - example
"""

from B_Data_Structures.tries import Trie

def main():

    agenda = Trie()

    agenda.insert("Ana")
    agenda.insert("Ana")
    agenda.insert("Ana")
    agenda.insert("Anabela")
    agenda.insert("Anabella")
    agenda.insert("Anabella")
    agenda.insert("Park")
    agenda.insert("Parker")
    agenda.insert("Parkinson")

    print()
    print(agenda.search("Park"))
    print(agenda.search("Ana"))

    print()
    print(agenda.starts_with("Ana"))

    print()
    agenda.print()

if __name__ == "__main__":
    main()
    print("Done!!")
