from collections import deque

shire = {
    'A': ['Z', 'T', 'S'],
    'B': ['F', 'P', 'G', 'U'],
    'C': ['D', 'R', 'P'],
    'D': ['M', 'C'],
    'E': ['H'],
    'F': ['S', 'B'],
    'G': ['B'],
    'H': ['U', 'E'],
    'I': ['N', 'V'],
    'L': ['T', 'M'],
    'M': ['L', 'D'],
    'N': ['I'],
    'O': ['Z', 'S'],
    'P': ['R', 'C', 'B'],
    'R': ['S', 'C', 'P'],
    'S': ['A', 'O', 'F', 'R'],
    'T': ['A', 'L'],
    'U': ['B', 'V', 'H'],
    'V': ['U', 'I'],
    'Z': ['O', 'A']}


def breadth_first(start, goal, neighbors):
    "Find a shortest sequence of states from start to the goal."
    frontier = deque([start])  # A queue of states
    previous = {start: None}  # start has no previous state; other states will
    while frontier:
        s = frontier.popleft()
        if s == goal:
            return path(previous, s)
        for s2 in neighbors[s]:
            if s2 not in previous:
                frontier.append(s2)
                previous[s2] = s


def path(previous, s):
    "Return a list of states that lead to state s, according to the previous dict."
    return [] if (s is None) else path(previous, previous[s]) + [s]


start, destination = input("Start and destination nodes: ").split(" ")
print(breadth_first(start, destination, shire))
