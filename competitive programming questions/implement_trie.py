class TreeNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = []

    def insert_children(self, child_letter):
        for child in self.children:
            if child.letter == child_letter:
                return child        
            
        child_node = TreeNode(child_letter)
        self.children.append(child_node)
        return child_node

        
    def get_child_reference(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child
        return None   

class Trie:
    def __init__(self):
        self.words = set()
        self.root = TreeNode(letter="")

    def insert(self, word: str) -> None:
        self.words.add(word)
        curr_node = self.root
        for letter in word: 
            curr_node = curr_node.insert_children(letter)


    def search(self, word: str) -> bool:
        return word in self.words


    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for letter in prefix:
            if curr_node != None:
                curr_node = curr_node.get_child_reference(letter)
            else:
                return False

        return True