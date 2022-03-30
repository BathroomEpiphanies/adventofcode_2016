import collections
import queue
import sys


duct = {x+y*1j:cell for y,row in enumerate(sys.stdin.readlines()) for x,cell in enumerate(row.strip())}
coordinates_for_locations = {v:k for k,v in duct.items() if v in '0123456789'}


distances_between_locations = collections.defaultdict(dict)
bearings = [+1+0j,+0+1j,-1+0j,+0-1j]
for start_location,start_coordinate in coordinates_for_locations.items():
    state_queue = collections.deque()
    start_distance = 0
    state_queue.append((start_distance,start_coordinate))
    visited_coordinates = {start_coordinate}
    while state_queue:
        current_distance,current_coordinate = state_queue.popleft()
        if duct[current_coordinate] in coordinates_for_locations:
            distances_between_locations[start_location][duct[current_coordinate]] = current_distance
        for next_coordinate in (current_coordinate+bearing for bearing in bearings):
            if next_coordinate not in visited_coordinates and duct[next_coordinate] != '#':
                visited_coordinates.add(next_coordinate)
                state_queue.append((current_distance+1,next_coordinate))


state_queue = queue.PriorityQueue()
start_distance = 0
start_location = '0'
remaining_locations = frozenset(coordinates_for_locations)-{'0'}
start_state = (start_distance,start_location,remaining_locations)
state_queue.put(start_state)
processed_states = {start_state}
star1 = None
while not state_queue.empty():
    current_distance,current_location,remaining_locations = state_queue.get()
    if not remaining_locations:
        if current_location=='0':
            star2 = f'*2: {current_distance}'
            break
        else:
            star1 = star1 or f'*1: {current_distance}'
            remaining_locations = frozenset({'0'})
    for next_location,distance_to_next_location in distances_between_locations[current_location].items():
        next_state = (current_distance+distance_to_next_location,next_location,remaining_locations-{next_location})
        if next_state not in processed_states:
            processed_states.add(next_state)
            state_queue.put(next_state)

print(star1)
print(star2)
