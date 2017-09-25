"""
k-Nearest Neighbors
See: http://andrew.gibiansky.com/blog/machine-learning/k-nearest-neighbors-simplest-machine-learning/
See: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
"""

import math
import random

def distance(instance1, instance2):
    dist = 0
    data = zip(instance1, instance2)
    for x, y in data:
        dist += pow((x-y), 2)
    return math.sqrt(dist)

def main():

    k = 5

    match_maker_website_users_tastes = {}
    for i in range(25):
        match_maker_website_users_tastes["user" + str(i)] = [random.randrange(1, 6) for _ in range(5)]
    match_maker_website_users_tastes["maria"] = [3, 4, 4, 1, 4]
    #print(netflax_users_ratings)
    
    alone_person_tastes = [3, 4, 4, 1, 4]

    neighbors = {}
    for line in match_maker_website_users_tastes:
        neighbors[line] = distance(match_maker_website_users_tastes[line], alone_person_tastes)

    neighbors_sorted = sorted(neighbors, key=lambda x: neighbors[x])

    neighbors_sorted = neighbors_sorted[:k]

    print("Hi, user trie the following person to contact, they seens to combine well with you:")
    for user in neighbors_sorted:

        if neighbors[user] == 0:
            print(user, match_maker_website_users_tastes[user], "Attention this is your soul mate!!!")
        else:
            print(user, match_maker_website_users_tastes[user])

if __name__ == "__main__":
    main()
    print("Done!!")
