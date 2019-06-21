# Word Ladders Problem
"""
Given two words (beginWord and endWord), and a dictionary's word list, return the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
# EXAMPLE
"""
Sample:
beginWord = "hit"
endWord = "cog"
return: ['hit', 'hot', 'cot', 'cog']

beginWord = "sail"
endWord = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
"""


f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# Put our words in a set for O(1) lookup

# Set of vertices (words)
word_set = list()
for word in words:
      word_set.append(word.lower())

# these letters are available
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def binary_search(arr, target):

    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr)-1
    while low <= high:
        middle_idx = (high + low) // 2

        if target < arr[middle_idx]:
            high = middle_idx - 1
        elif target > arr[middle_idx]:
            low = middle_idx + 1

        else:
            return arr[middle_idx]
    return None



def get_neighbors(word):
    # word = sail
    # any word that has one letter different that this word
    neighbors = []

    # for each letter in word
    word_split = list(word)

    for i in range(len(word_split)):
        # replace with each letter in letters
        for j in letters:
            # and check if it exists in word_set
            temp_word = list(word_split)
            temp_word[i] = j
            word_string = ''.join(temp_word)
            # result = binary_search(word_set, word_string)
    # add it to neighbors list
            if word_string != word and word_string in word_set:
                neighbors.append(word_string)

    # neighbors.remove(word)
    return neighbors

print(get_neighbors('sail'))
print('bail')
print(get_neighbors('bail'))


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

"""
# get neighbours  for beginWord
word_neighbors = get_neighbors(beginWord)
# add first neighbour to Que together with PATH

# keep doing it untill the neighbour == endWord

# return PATH to endWord
"""


# BFS with path
def find_word_ladder(beginWord, endWord):
    # keep track of visited words(nodes)
    visited = set()
    # create a que
    que = Queue()
    que.enqueue({"value": beginWord, "path": []})

     # loop until the queue is empty
    while que.size() > 0:
        # get the next node in queue (the one first in que - FIFO)
        current_node = que.queue[0]
        cn_value = current_node["value"]
        cn_path = current_node["path"]

        # see if we already visited this node
        if cn_value not in visited:
            # if we did not visit this node yet
            # add it to the visited list
            visited.add(cn_value)

            # if this node is destination node
            if cn_value == endWord:
                # add its value to the path set, so it containts the last node
                cn_path.append(cn_value)
                # and return PATH
                return cn_path

            # get neighbours for current_node value
            word_neighbors = get_neighbors(cn_value)

            # else add all neighbouring nodes to queue
            for neighbour in word_neighbors:
                # print(f'neighbour: {neighbour}')
                # Make a COPY of the PATH set from current node to neighbour nodes
                path_to_neighbour = cn_path.copy()
                # and add the current node value into it, so neighbouring nodes have path to "parent" node
                path_to_neighbour.append(cn_value)

                # add neighbouring node to queue
                que.enqueue(
                    {"value": neighbour, "path": path_to_neighbour})
                # print(f'que: {que.queue}')

        # remove current node from queue
        que.dequeue()
        # print(f'QUE: {que.queue}\n')
    return None


print(find_word_ladder("sail", "boil"))