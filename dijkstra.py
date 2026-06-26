import heapq


def dijkstra(
    graph: dict[str, dict[str, int]], start_node: str
) -> dict[str, tuple[float, list[str]]]:
    # We'll set the distance to all nodes to infinity initially
    distances: dict[str, float] = {node: float("inf") for node in graph}
    distances[start_node] = 0.0

    # This keeps track of the actual path we took to get to each node
    paths: dict[str, list[str]] = {node: [] for node in graph}
    paths[start_node] = [start_node]

    # Our priority queue, starting with the source node
    # It stores tuples of (distance, node) so heapq can sort by distance automatically
    pq: list[tuple[float, str]] = [(0.0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If we already found a shorter path to this node, skip this old entry
        if current_distance > distances[current_node]:
            continue

        # Look at all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance_via_current = current_distance + weight

            # If we found a faster way to get to the neighbor, update it!
            if distance_via_current < distances[neighbor]:
                distances[neighbor] = distance_via_current
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(pq, (distance_via_current, neighbor))

    # Package the final distances and paths together for easy reading
    results: dict[str, tuple[float, list[str]]] = {}
    for node in graph:
        results[node] = (distances[node], paths[node])
    return results


# Quick test run using the STUST campus graph
if __name__ == "__main__":
    # Let's map the abbreviations to names for the output print
    landmarks = {
        "A": "CSIE Department",
        "B": "Library",
        "C": "Assembly Hall",
        "D": "Gymnasium",
        "E": "Student Center",
        "F": "Main Gate",
    }

    campus_graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }

    # 1. Show the campus graph using letters only
    print("Campus Graph Connections:")
    for node, neighbors in campus_graph.items():
        connections = ", ".join(
            f"{neighbor}({weight})" for neighbor, weight in neighbors.items()
        )
        print(f"  {node} -> {connections}")

    # 2. Print the legend mapping letters to their landmarks
    print("\nLandmark Legend:")
    for letter, name in landmarks.items():
        print(f"  {letter}: {name}")

    # 3. Tell the user what the set starting point is
    start = "A"
    print(f"\nStarting Point: {start} ({landmarks[start]})")

    # Run the algorithm
    shortest_paths = dijkstra(campus_graph, start)

    # 4. Output the results using only letters for destinations and routes
    print("\nShortest Paths Results:")
    for node, (distance, path) in shortest_paths.items():
        route = " -> ".join(path)
        print(f"  Destination: {node} | Distance: {distance:<4} | Route: {route}")
