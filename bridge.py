
cross_times = {'A': 5, 'B': 10, 'G': 20, 'GR': 25}

class State:
    def __init__(self, left, right, umbrella, time, path=None):
        self.left = left[:]  
        self.right = right[:]  
        self.umbrella = umbrella  
        self.time = time 
        if path is None:
            self.path = [[left[:], right[:], umbrella, time]]
        else:
            self.path = path[:] + [[left[:], right[:], umbrella, time]]

def goalState(state):
    return len(state.left) == 0 and state.umbrella == 'right' and state.time <= 60

def nextGen(state):
    children = []
    left = state.left
    right = state.right
    umbrella = state.umbrella
    time = state.time

    if umbrella == 'left':
        for i in range(len(left)):
            for j in range(i + 1, len(left)):
                p1 = left[i]
                p2 = left[j]
                new_left = left[:]
                new_left.remove(p1)
                new_left.remove(p2)
                new_right = right[:] + [p1, p2]
                t = max(cross_times[p1], cross_times[p2])
                new_time = time + t
                children.append(State(new_left, new_right, 'right', new_time, state.path))
    else:
        for i in range(len(right)):
            p = right[i]
            new_right = right[:]
            new_right.remove(p)
            new_left = left[:] + [p]
            t = cross_times[p]
            new_time = time + t
            children.append(State(new_left, new_right, 'left', new_time, state.path))

    return children

def bfs():
    start = State(['A', 'B', 'G', 'GR'], [], 'left', 0)
    queue = [start]
    visited = []

    while len(queue) > 0:
        current = queue.pop(0)
        key = [sorted(current.left), sorted(current.right), current.umbrella]
        if key in visited or current.time > 60:
            continue
        visited.append(key)

        if goalState(current):
            return current.path, current.time

        for child in nextGen(current):
            queue.append(child)

    return None, None


solution_path, total_time = bfs()


if solution_path:
    print("=== Bridge Problem BFS Solution ===")
    for step in solution_path:
        print(f"Left: {step[0]}, Right: {step[1]}, Umbrella: {step[2]}, Time: {step[3]} mins")
    print("Total Time:", total_time, "minutes")
else:
    print("No solution found within 60 minutes.")

