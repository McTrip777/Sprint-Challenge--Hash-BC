#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    # add all tickets
    for i in range(length):
        if route[i] == None:
            hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
            if tickets[i].source == "NONE": 
                current = tickets[i].destination
                route[0] = current
            
    # rearrange all tickets not including the first in the right order
    for j in range(1, length):
        next_ticket = hash_table_retrieve(hashtable, current)
        route[j] = next_ticket 
        current = next_ticket
        

    return route
