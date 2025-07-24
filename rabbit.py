class State:
    def __init__(self, config, path=None):
        self.config = config 
        if path is None:
            self.path = [config[:]]  
        else:
            self.path = path[:] + [config[:]]  


def goalState(state):
    return state.config == ['W', 'W', 'W', '_', 'E', 'E', 'E']


def nextGen(current_state):
    children = []
    config = current_state.config

    for i in range(len(config)):
        if config[i] == 'E':
          
            if i + 1 < len(config) and config[i + 1] == '_':
                new_config = config[:]
                new_config[i], new_config[i + 1] = '_', 'E'
                children.append(State(new_config, current_state.path))
            
            if i + 2 < len(config) and config[i + 2] == '_' and config[i + 1] in ('E', 'W'):
                new_config = config[:]
                new_config[i], new_config[i + 2] = '_', 'E'
                children.append(State(new_config, current_state.path))

        elif config[i] == 'W':
            if i - 1 >= 0 and config[i - 1] == '_':
                new_config = config[:]
                new_config[i], new_config[i - 1] = '_', 'W'
                children.append(State(new_config, current_state.path))
            if i - 2 >= 0 and config[i - 2] == '_' and config[i - 1] in ('E', 'W'):
                new_config = config[:]
                new_config[i], new_config[i - 2] = '_', 'W'
                children.append(State(new_config, current_state.path))

    return children

def bfs(start_config):
    queue = [State(start_config)]
    visited = []

    while len(queue) > 0:
        current = queue.pop(0)
        if current.config in visited:
            continue
        visited.append(current.config)

        if goalState(current):
            return current.path

        children = nextGen(current)
        for child in children:
            if child.config not in visited:
                queue.append(child)
    return None

def dfs(start_config):
    stack = [State(start_config)]
    visited = []

    while len(stack) > 0:
        current = stack.pop()
        if current.config in visited:
            continue
        visited.append(current.config)

        if goalState(current):
            return current.path

        children = nextGen(current)
        for child in children:
            if child.config not in visited:
                stack.append(child)
    return None

start_config = ['E', 'E', 'E', '_', 'W', 'W', 'W']


print("BFS:")
bfs_result = bfs(start_config)
for step in bfs_result:
    print(step)


print("\nDFS:")
dfs_result = dfs(start_config)
for step in dfs_result:
    print(step)

