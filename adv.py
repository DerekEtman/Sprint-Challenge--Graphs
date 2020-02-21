from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.``

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edges(self, vertex, direction, value):
        self.vertices[vertex][direction] = value


g = Graph()

g.add_vertex(player.current_room.id)

for exit in player.current_room.get_exits():
    g.add_edges(player.current_room.id, exit, "?")


def get_it_done():
    # Create an empty Queue
    q = Queue()
    # Add a path to the room origin to the queue
    for direction in g.vertices[player.current_room.id]:
        if g.vertices[player.current_room.id][direction] == "?":
            q.enqueue(direction)
    # create an empty set to store the visited rooms
    # visited = set()
    # while the queue is not empty
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
        # grab the last room from the path
        v = path[-1]
        dft(path)
        # loop throughplayer.current_room.get_exits() to check if you can move in a direction
        shortest_path = bft_shortest_path(player.current_room)
            # if yes....
            # check if it's been visited....
            # IF IT HASNT been visited
        # ELSE IF IT HAS been visited
        if shortest_path is None:
            return
            # return to the previous room repeat the process.
            move_back(shortest_path)
            print("current room", player.current_room.id)

            # resetting the q
            q.queue = []
            # if v not in visited:
        for direction in g.vertices[player.current_room.id]:
            if g.vertices[player.current_room.id][direction] == "?":
                # then add a path to all neighbors to the back of the queue
                q.enqueue(direction)





def auto_move(i = 0):

    # Cycle through all possible exits, 
    # if exit is possible 
    # check to see if room of exit has been visited
    # if it hasn't been visited move to the new room
    # else check the next room
    connected_rooms = player.current_room.get_exits()
    # next_room = player.current_room.get_room_in_direction(x)
    while i < 10:
        print(f"Visited Rooms: {visited}")
        if player.current_room.id not in visited:
            visited.add(player.current_room.id)

        if "n" in connected_rooms and player.current_room.id not in visited:
            print("n")
            player.travel("n")
            visited.add(player.current_room.id)
            i+=1
            return auto_move(i)
        elif "e" in connected_rooms:
            print("e")
            player.travel("e")
            i+=1
            return auto_move(i)
        elif "s" in connected_rooms:
            print("s")
            player.travel("s")
            i+=1
            return auto_move(i)
        elif "w" in connected_rooms:
            print('w')
            player.travel("w")
            i+=1
            return auto_move(i)
        else:
            print("No where else to move.")
            input('q')
    




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
starting_room = world.starting_room

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(auto_move())
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")





            

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
#     auto_move()


while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
        auto_move()


