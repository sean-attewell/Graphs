import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # loop over 0 to numUsers
        for i in range(0, numUsers):
            # add user for each itteration
            self.addUser(f"User {i + 1}")
        # Create friendships
        # generate all possible friendship combinations
        # create empty possibleFriendships list
        possibleFriendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second one
        # loop over userID's in the self.users
        for userID in self.users:
            # loop over friendID's in a range from userID + 1, to lastID + 1)
            for friendID in range(userID + 1, self.lastID + 1):
                # append a tuple of (userID, friendID) to the possibleFriendships list
                possibleFriendships.append((userID, friendID))
        # shuffle possible friendships using random.shuffle()
        random.shuffle(possibleFriendships)
        # create friendships for the first X pair of the list
        # X is determined by the formula: numUsers * avgFriendships // 2
        # Needed to divide by 2 since each addFriendship() creates 2 friendships
        # loop over a range of numUsers * avgFriendships // 2...
        for i in range(numUsers * avgFriendships // 2):
            # set friendship to possibleFriendships at the index
            friendship = possibleFriendships[i]
            # addFriendship using a tuple of (friendship[0], friendship[1])
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        # create an empty Queue
        q = Queue()
        # create an empty visited dictionary
        visited = {}  # Note that this is a dictionary, not a set
        # add A PATH TO  the starting vertex to the queue
        q.enqueue([userID])
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            v = path[-1]
            # if it is not visited...
            if v not in visited:
                # when we reach an unvisited user, append the path to the visited dictionary
                visited[v] = path
                # Then enqueue PATHS TO each of its neighbors in the queue
                for neighbor in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        # return visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(f"Users in extended social network: {len(connections) - 1}")
    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])
    print(
        f"Average len of social path: {total_social_paths // len(connections)}")
    # print("--------------")
    # print(connections)
