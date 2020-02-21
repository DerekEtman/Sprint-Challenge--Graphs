from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
starting_room = world.starting_room

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

for direction in player.current_room.get_exits():
    g.add_edges(player.current_room.id, direction, "?")

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.``
def explore():
    print("\n --Running Explore--")
    print(f"Current room: {player.current_room.id}")
    # Create an empty Queue
    q = Queue()
    # Add a path to the room origin to the queue
    for direction in g.vertices[player.current_room.id]:
        print(f"Explore-- printing direction in g.vertices[player...room id] {direction}")
        if g.vertices[player.current_room.id][direction] == "?":
            print(f"Explore-- Direction {direction} is {True}")
            q.enqueue(direction)
    # create an empty set to store the visited rooms
    # visited = set()
    # while the queue is not empty
    print(f"Explore-- Checking if q is > 0")
    while q.size() > 0:
        print(f"q is > 0")
        # Dequeue the first path
        path = q.dequeue()
        # grab the last room from the path
        v = path[-1]
        
        print(f"Dispatching DFT with {path}")
        dft(path)
        # loop throughplayer.current_room.get_exits() to check if you can move in a direction
        shortest_path = bft_shortest_path(player.current_room)
            # if yes....
            # check if it's been visited....
            # IF IT HASNT been visited
        # ELSE IF IT HAS been visited
        print(f"shortest_path: {shortest_path}")

        if shortest_path is None:
            # return
            # return to the previous room repeat the process.
            move_back(shortest_path)

            # resetting the q
            q.queue = []
            # if v not in visited:
        for direction in g.vertices[player.current_room.id]:
            if g.vertices[player.current_room.id][direction] == "?":
                # then add a path to all neighbors to the back of the queue
                q.enqueue(direction)

# Just keep diginginginginging
def dft(move_direction):
    print("\n -- Running DFT --")
    exits = player.current_room.get_exits()

    print(f"Dispatching Move: {move_direction}")
    if move_direction in exits and not visited:
        print(f"DFT-- printing exits: {exits}")
        auto_move(move_direction)

    # For each possible route
    for direction in g.vertices[player.current_room.id]:
        print(f"DFT-- direction: {direction}")
        print(f" what was this? {g.vertices[player.current_room.id][direction]}")
        # If that hole is dark and dangerous
        if g.vertices[player.current_room.id][direction] == "?":
            # do it again!
            dft(direction)
            return
    return


# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.``
def auto_move(direction):
    print("\n --Moving--")

    # Cycle through all possible exits, 
    # if exit is possible 
    # check to see if room of exit has been visited
    # if it hasn't been visited move to the new room
    # else check the next room
    connected_rooms = player.current_room.get_exits()
    current_room = player.current_room.id

    print(f"Current Room: {current_room}")
    
    print(f"Attempting to move to: {direction}")
    player.travel(direction) 

    
    print(f"moving {direction}")
    traversal_path.append(direction)
    print(f"Traversal Path: {traversal_path}")

    g.add_edges(current_room,direction, player.current_room.id)
    g.add_vertex(player.current_room.id)
    rev_direction = None

    if direction == "w":
        rev_direction = "e"
    elif direction =="e":
        rev_direction = "w"
    elif direction == "s":
        rev_direction = "n"
    else:
        rev_direction ="s"

    g.add_edges(player.current_room.id, rev_direction, current_room)
    for direction in player.current_room.get_exits():
        if direction not in g.vertices[current_room]:
            g.add_edges(player.current_room.id, direction, "?")


def bft_shortest_path(starting_room):
    q = Queue()
    visited = set()
    q.enqueue([starting_room.id])
    print("\n --Starting BFT--")

    while q.size() > 0:
        path = q.dequeue()
        last_path = path[-1]
        print(f"last_Path: {last_path}")

        if last_path not in visited:
            for key in g.vertices[last_path]:
                if g.vertices[last_path][key] == "?":
                    return path

            visited.add(last_path)
            print(f"visited: {visited}")

            for direction in g.vertices[last_path]:
                q.enqueue(path + [g.vertices[last_path][direction]])
    return None

def move_back(shortest_path):
    print("\n --Moving Back--")
    while len(shortest_path) > 1:
        grab_id  = shortest_path.pop(0)

        for direction in g.vertices[grab_id]:
            if g.vertices[grab_id][direction] == shortest_path[0]:
                traversal_path.append(direction)
                player.travel(direction)

        
   
   
   
#    Test code
    # while i < 10:
    #     print(f"Visited Rooms: {visited}")
    #     if player.current_room.id not in visited:
    #         visited.add(player.current_room.id)

    #     if "n" in connected_rooms and player.current_room.id not in visited:
    #         print("n")
    #         player.travel("n")
    #         visited.add(player.current_room.id)
    #         i+=1
    #         return auto_move(i)
    #     elif "e" in connected_rooms:
    #         print("e")
    #         player.travel("e")
    #         i+=1
    #         return auto_move(i)
    #     elif "s" in connected_rooms:
    #         print("s")
    #         player.travel("s")
    #         i+=1
    #         return auto_move(i)
    #     elif "w" in connected_rooms:
    #         print('w')
    #         player.travel("w")
    #         i+=1
    #         return auto_move(i)
    #     else:
    #         print("No where else to move.")
    #         input('q')
    






explore()

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")





            

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
#     auto_move()


# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
#         auto_move()


