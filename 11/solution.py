import sys
import re
import json

import itertools
from collections import namedtuple


State = namedtuple('state',['elevator','floors'])
Floor = namedtuple('floor',['generators','microchips'])

lines = [l.strip() for l in sys.stdin.readlines()]


def print_state(state):
    [print(f'{"#" if i==state.elevator else " "} {f}') for i,f in reversed(list(enumerate(state.floors)))]
    print()


def check_state(state):
    elevator = state.elevator
    forbidden = elevator<0 or 3<elevator
    for floor in state.floors:
        forbidden = forbidden or (floor.microchips-floor.generators and floor.generators)
    return not forbidden


def find_next_states(state):
    def make_state(state,next_elevator,next_generators,next_microchips):
        next_state = State(
            next_elevator,
            tuple(
                Floor(
                    (floor.generators | set(next_generators) if i==next_elevator else floor.generators - set(next_generators)),
                    (floor.microchips | set(next_microchips) if i==next_elevator else floor.microchips - set(next_microchips))
                ) for i,floor in enumerate(state.floors)
            )
        )
        #print_state(next_state)
        #print()
        return next_state
        
    elevator = state.elevator
    floor = state.floors[elevator]
    next_states = []
    for next_elevator in (elevator-1,elevator+1):
        for next_generators in itertools.combinations(floor.generators,2):
            next_microchips = set()
            next_state = make_state(state,next_elevator,next_generators,next_microchips)
            if check_state(next_state):
                next_states.append(next_state)
        
        for next_generators in itertools.combinations(floor.generators,1):
            next_microchips = set()
            next_state = make_state(state,next_elevator,next_generators,next_microchips)
            if check_state(next_state):
                next_states.append(next_state)
        
        for next_microchips in itertools.combinations(floor.microchips,2):
            next_generators = set()
            next_state = make_state(state,next_elevator,next_generators,next_microchips)
            if check_state(next_state):
                next_states.append(next_state)
        
        for next_microchips in itertools.combinations(floor.microchips,1):
            next_generators = set()
            next_state = make_state(state,next_elevator,next_generators,next_microchips)
            if check_state(next_state):
                next_states.append(next_state)
        
        for next_generators in itertools.combinations(floor.generators,1):
            for next_microchips in itertools.combinations(floor.microchips,1):
                next_state = make_state(state,next_elevator,next_generators,next_microchips)
                if check_state(next_state):
                    next_states.append(next_state)
                
    return next_states


def find_solution(start_depth, start_state, goal_state):
    queue = [(start_depth,start_state,[start_state])]
    seen_states = set()
    while queue:
        steps,state,history = queue.pop(0)
        #print(steps,len(seen_states))
        if state in seen_states:
            continue
        seen_states.add(state)
        if state == goal_state:
            return steps,history
        next_states = find_next_states(state)
        for next_state in next_states:
            if next_state not in seen_states:
                queue.append((steps+1,next_state,[s for s in history]+[next_state]))
    return None,None
    

start_state = State(
    0,
    tuple(
        Floor(
            frozenset(re.findall(r'(\w+) generator', line)),
            frozenset(re.findall(r'(\w+)-compatible microchip', line))
        ) for line in lines
    )
)

print_state(start_state)

goal_state = State(
    3,
    (
        Floor(frozenset(),frozenset()),
        Floor(frozenset(),frozenset()),
        Floor(frozenset(),frozenset()),
        Floor(
            frozenset(g for f in start_state.floors for g in f.generators),
            frozenset(m for f in start_state.floors for m in f.microchips),
        )
    )
)

steps,history = find_solution(0,start_state,goal_state)
for s in history:
    print_state(s)
    print()
print('*1:',steps)

start_state = State(
    3,
    (
        Floor(
            frozenset(['elerium','dilithium']),
            frozenset(['elerium','dilithium']),
        ),
        Floor(frozenset(),frozenset()),
        Floor(frozenset(),frozenset()),
        Floor(frozenset(['placeholder1','placeholder2']),frozenset(['placeholder1','placeholder2']))
    )
)
goal_state = State(
    3,
    (
        Floor(frozenset(),frozenset()),
        Floor(frozenset(),frozenset()),
        Floor(frozenset(),frozenset()),
        Floor(
            frozenset(g for f in start_state.floors for g in f.generators),
            frozenset(m for f in start_state.floors for m in f.microchips),
        )
    )
)
steps,history = find_solution(steps,start_state,goal_state)
for s in history:
    print_state(s)
    print()
print('*2:',steps)

