# Time taken by each person
cross_time = {'A': 5, 'B': 10, 'G': 20, 'GR': 25}

class CrossingState:
    def __init__(self, left_side, right_side, torch_pos, elapsed, trace=None):
        self.left = left_side[:]
        self.right = right_side[:]
        self.torch = torch_pos
        self.time = elapsed
        self.history = trace[:] + [[self.left[:], self.right[:], self.torch, self.time]] if trace else [[self.left[:], self.right[:], self.torch, self.time]]

def is_goal(state):
    return len(state.left) == 0 and state.torch == 'right' and state.time <= 60

def generate_next(state):
    future_states = []
    l, r, torch = state.left, state.right, state.torch
    current_time = state.time

    if torch == 'left':
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                x, y = l[i], l[j]
                new_l = l[:]
                new_l.remove(x)
                new_l.remove(y)
                new_r = r[:] + [x, y]
                t = max(cross_time[x], cross_time[y])
                total = current_time + t
                future_states.append(CrossingState(new_l, new_r, 'right', total, state.history))
    else:
        for i in range(len(r)):
            x = r[i]
            new_r = r[:]
            new_r.remove(x)
            new_l = l[:] + [x]
            t = cross_time[x]
            total = current_time + t
            future_states.append(CrossingState(new_l, new_r, 'left', total, state.history))

    return future_states

def bfs_bridge():
    start = CrossingState(['A', 'B', 'G', 'GR'], [], 'left', 0)
    q = [start]
    seen = []

    while q:
        node = q.pop(0)
        signature = [sorted(node.left), sorted(node.right), node.torch]

        if signature in seen or node.time > 60:
            continue
        seen.append(signature)

        if is_goal(node):
            return node.history, node.time

        for future in generate_next(node):
            q.append(future)
    return None, None

def dfs_bridge():
    start = CrossingState(['A', 'B', 'G', 'GR'], [], 'left', 0)
    stack = [start]
    seen = []

    while stack:
        node = stack.pop()
        signature = [sorted(node.left), sorted(node.right), node.torch]

        if signature in seen or node.time > 60:
            continue
        seen.append(signature)

        if is_goal(node):
            return node.history, node.time

        for future in reversed(generate_next(node)):
            stack.append(future)
    return None, None

# Run and Print
print("===== BFS Bridge Problem Solution =====")
bfs_path, bfs_time = bfs_bridge()
if bfs_path:
    for step in bfs_path:
        print(f"Left: {step[0]} | Right: {step[1]} | Torch: {step[2]} | Time: {step[3]} min")
    print("Total BFS Time:", bfs_time, "minutes\n")
else:
    print("No BFS Solution within 60 mins.\n")

print("===== DFS Bridge Problem Solution =====")
dfs_path, dfs_time = dfs_bridge()
if dfs_path:
    for step in dfs_path:
        print(f"Left: {step[0]} | Right: {step[1]} | Torch: {step[2]} | Time: {step[3]} min")
    print("Total DFS Time:", dfs_time, "minutes")
else:
    print("No DFS Solution within 60 mins.")

