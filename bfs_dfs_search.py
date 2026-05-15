from collections import deque

# The Search Graph .key representing a node and the values ,its neighbours
graph = {
    'Start': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['Goal'],
    'E': ['Goal'],
    'F': [],
    'Goal': []
}

def bfs_path(graph, start, goal):
    # The queue stores [current_node, path_taken_to_get_here]
    print("* "*10+" BFS "+"* "*10)
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft() # Get the OLDEST path added
        node = path[-1] # Look at the last node in that path

        if node == goal:
            return path
        
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)
            print(F"Queue now contins: {list(queue)}")
            print("-"*30)
    return None

def dfs_path(graph, start, goal):
    # Same structure as BFS, but we use a list as a Stack
    print("* "*10+" DFS "+"* "*10)
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()    # Get the NEWEST path added (The Stack magic)
        node = path[-1]

        if node == goal:
            return path
        
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            
            #mark this node as visited
            visited.add(node)
            print(F"Stack now contins: {list(stack)}")
            print("-"*30)
    return None

# Execute the functions
result = bfs_path(graph, 'Start', 'Goal')
print(f"\nFINAL BFS PATH: {result}\n")
result=dfs_path(graph, 'Start','Goal')
print(f"\nFINAL BFS PATH: {result}\n")
