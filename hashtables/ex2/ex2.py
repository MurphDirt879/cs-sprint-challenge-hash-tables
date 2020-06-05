#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    route = [None] * length

    for x in range(length):
        if tickets[x].source == "NONE":
            route[0] = tickets[x].destination
        storage[tickets[x].source] = tickets[x].destination

    for y in range(length):
        if route[y - 1] is not None:
                route[y] = storage[route[y - 1]]

    return route
