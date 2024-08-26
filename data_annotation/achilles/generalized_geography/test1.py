import unittest


def has_winning_strategy(graph, start):
  """Determines if the first player has a winning strategy in the Generalized Geography game.

  Args:
    graph: A dictionary representing the adjacency list of the directed graph.
           Keys are node names (strings), and values are lists of node names
           that can be reached from the key node by a single directed edge.
    start: A string representing the starting node.

  Returns:
    True if the first player has a winning strategy, False otherwise.
  """

  if not graph or start not in graph:
    return False

  # If a node has no outgoing edges, the player who lands on it loses
  if not graph[start]:
    return False

  # Recursively check if the current player can force a win from each possible next move
  for next_node in graph[start]:
    # Create a copy of the graph and remove the current node to simulate the next turn
    new_graph = graph.copy()
    for node in new_graph:
      if next_node in new_graph[node]:
        new_graph[node].remove(next_node)

    # If the opponent has no winning strategy from the next node, the current player wins
    if not has_winning_strategy(new_graph, next_node):
      return True

  # If no move leads to a forced win for the current player, they lose
  return False

graph = {
  'A': ['B', 'C'],
  'B': ['D'],
  'C': ['D'],
  'D': []
}
start = 'A'
print(has_winning_strategy(graph, start))


