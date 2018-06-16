"""
Tries
"""		

class Trie():

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.childs = {}

    def __init__(self):
        self.__root = Trie.Node()

    def insert(self, word):
        self.insert_word(word, self.__root)

    def insert_word(self, word, node):
        if word[:1] not in node.childs:
            new_node = Trie.Node(word[:1])
            node.childs[word[:1]] = new_node
            self.insert_word(word, node)
        else:
            next_node = node.childs[word[:1]]
            if not word[1:]:
                # last node to mark end and to count how many where inserted
                if ' ' in next_node.childs:
                    next_node.childs[' '].value += 1
                else:
                    next_node.childs[' '] = Trie.Node(1)
                return
            return self.insert_word(word[1:], next_node)

    def search(self, word):
        return self.search_word(word, self.__root) if word else False

    def search_word(self, word, node):
        if word[:1] in node.childs:
            next_node = node.childs[word[:1]]
            if not word[1:]:
                return True if ' ' in next_node.childs else False
            return self.search_word(word[1:], next_node)
        return False

    def starts_with(self, prefix):
        return self.starts_with_prefix(prefix, self.__root) if prefix else True

    def starts_with_prefix(self, word, node):
        if word[:1] in node.childs:
            if not word[1:]:
                return True
            next_node = node.childs[word[:1]]
            return self.starts_with_prefix(word[1:], next_node)
        return False

    def print(self):
        self.print_me(self.__root, 1)

    def print_me(self, node, level):
        print("|" * level, node.value)
        for node in node.childs.values():
            self.print_me(node, level+1)
            