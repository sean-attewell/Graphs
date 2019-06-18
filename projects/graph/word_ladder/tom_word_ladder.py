f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_neighbors(word):
    neighbors = []
    # Turn our word into a letter list: ['w', 'o', 'r', 'd']
    string_word = list(word)
    # For each letter...
    for i in range(len(string_word)):
        # swap that letter with each letter in the alphabet
        for letter in letters:
            # Reform it into a word string and check if it's in the word_set
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            # If it doesn't equal the original word and it's in the set, append to neighbors
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def find_word_ladder(beginWord, endWord):
    visited = set()
    q = Queue()
    q.enqueue([beginWord])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == endWord:
                return path
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(find_word_ladder("sail", "boat"))
