import heapq


def a_star_search(graph, start, goal):
    # Priority queue to store (cost, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Dictionary to store the cost of getting to each node
    g_costs = {start: 0}

    # Dictionary to store the path
    came_from = {start: None}

    # Heuristic function (can be modified for specific graphs)
    def heuristic(node, goal):
        return 0  # No specific heuristic provided

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        # If we've reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], g_costs[goal]

        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_cost = g_costs[current_node] + cost

            # If this path is better than any previously recorded path
            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')  # If there is no path


# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

path, cost = a_star_search(graph, 'A', 'D')
print(f"Path: {path}, Cost: {cost}")
