#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    # add all tickets with the starting location at the first index
    for i in range(length):
        if route[i] == None:
            hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
            if tickets[i].source == "NONE": 
                current = tickets[i].destination
                route[0] = current
        
    # rearrange all tickets not including the first in the right order
    for j in range(1, length):
        if current == tickets[j].source:
            route[j] = tickets[j].destination
            current = route[j]

    return route
