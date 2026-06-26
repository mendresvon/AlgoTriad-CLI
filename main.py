#!/usr/bin/env python3
"""STUST CSIE Algorithms Assignment.

This module implements three core computer science algorithms:
1. Binary Search (Divide and Conquer)
2. Quick Sort (Divide and Conquer, In-Place Lomuto Partitioning)
3. Dijkstra's Shortest Path Algorithm (Greedy Approach)

It features an interactive console menu with robust input validation.
"""

import heapq
import os
import sys


def clear_screen() -> None:
    """Clears the terminal screen for a clean, slide-like presentation layout."""
    # We check if the stdout is a terminal before calling clear to avoid garbage characters
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def print_header(screen_title: str = "") -> None:
    """Prints the mandatory student verification header and optional screen title."""
    print("==================================================")
    print("STUST CSIE Algorithms Assignment")
    print("Student Name: 馬盛中")
    print("Student ID: 4B1YZ001")
    print("==================================================")
    if screen_title:
        print(f" >>> {screen_title} <<<")
        print()


def pause_and_continue() -> None:
    """Pauses execution to allow the user to read the output before returning to menu."""
    print("\n--------------------------------------------------")
    input("Press Enter to return to the main menu...")


def parse_integer_list(user_input: str) -> list[int]:
    """Parses a comma- or space-separated string of numbers into a list of integers.

    Args:
        user_input: String containing integers separated by commas or spaces.

    Returns:
        A list of integers parsed from the input.

    Raises:
        ValueError: If any element in the input is not a valid integer.
    """
    cleaned = user_input.replace(",", " ")
    parts = cleaned.split()
    if not parts:
        raise ValueError("Input is empty.")
    return [int(x) for x in parts]


# =====================================================================
# ALGORITHM 1: BINARY SEARCH (DIVIDE & CONQUER)
# =====================================================================


def binary_search(arr: list[int], target: int) -> tuple[int, int]:
    """Performs an iterative binary search on a pre-sorted list.

    Time Complexity:
        Best Case: O(1) - target is at the midpoint.
        Average/Worst Case: O(log n) - search space halved each step.

    Space Complexity:
        O(1) - performs search in-place with minimal pointer variables.

    Args:
        arr: A sorted list of integers to search.
        target: The integer to find.

    Returns:
        A tuple of (index, steps), where index is -1 if the target is not found,
        and steps is the number of comparisons made.
    """
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid, steps
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


def run_binary_search_demo() -> None:
    """Interactively guides the user through the Binary Search demonstration."""
    clear_screen()
    print_header("Binary Search (Divide and Conquer)")

    # Default pre-sorted list for convenience
    default_list = [12, 23, 34, 45, 56, 67, 78, 89, 90]
    print(f"Default sorted list: {default_list}")
    print("You can use this default list or enter your own.")

    # Get user list choice
    choice = input("\nUse default list? (Y/n): ").strip().lower()
    if choice in ("", "y", "yes"):
        arr = default_list.copy()
    else:
        while True:
            raw_input = input(
                "Enter a list of numbers (separated by spaces or commas): "
            ).strip()
            try:
                arr = parse_integer_list(raw_input)
                # Check if sorted; if not, sort it and inform the user.
                # Binary Search requires sorted input to make correct binary decisions.
                if arr != sorted(arr):
                    print("\n[Notice] Binary Search requires a sorted list.")
                    arr.sort()
                    print(f"Your list has been sorted automatically: {arr}")
                break
            except ValueError:
                print("Error: Invalid list format. Please enter only integers.")

    # Get search target
    while True:
        target_str = input("\nEnter the integer target to search for: ").strip()
        try:
            target = int(target_str)
            break
        except ValueError:
            print("Error: Target must be a valid integer.")

    print(f"\nSearching for target '{target}' in list {arr}...")
    index, steps = binary_search(arr, target)

    if index != -1:
        print("\nSuccess: Target found!")
        print(f"  - Target Element: {target}")
        print(f"  - Found at Index: {index}")
        print(f"  - Total Steps/Comparisons: {steps}")
    else:
        print(f"\nResult: Target '{target}' was not found in the list.")
        print(f"  - Total Steps/Comparisons: {steps}")

    pause_and_continue()


# =====================================================================
# ALGORITHM 2: QUICK SORT (DIVIDE & CONQUER)
# =====================================================================


def partition(arr: list[int], low: int, high: int) -> int:
    """Partitions the sub-array in-place using Lomuto's partitioning scheme.

    We select the last element of the sub-array as the pivot. Then, we
    iterate through the sub-array and swap elements smaller than the pivot
    to the left. Finally, we swap the pivot into its correct sorted index.

    Args:
        arr: The list of integers being sorted.
        low: The starting index of the partition.
        high: The ending index of the partition (contains the pivot).

    Returns:
        The final index of the pivot element.
    """
    pivot = arr[high]
    i = low - 1  # Index of the boundary of smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element to the index right after the smaller elements boundary
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_in_place(arr: list[int], low: int, high: int) -> None:
    """Sorts a list of integers in-place using recursive quicksort.

    Time Complexity:
        Best/Average Case: O(n log n) - balanced partitions.
        Worst Case: O(n^2) - when elements are already sorted or reverse sorted,
                             causing highly skewed partitions with Lomuto scheme.

    Space Complexity:
        O(log n) - average auxiliary stack space due to recursive calls.
        O(n) - worst-case stack space under severe skew.

    Args:
        arr: The list of integers to sort.
        low: The starting index of the segment to sort.
        high: The ending index of the segment to sort.
    """
    if low < high:
        # Partition the array and get pivot index
        pivot_idx = partition(arr, low, high)

        # Recursively sort elements before and after the pivot
        quick_sort_in_place(arr, low, pivot_idx - 1)
        quick_sort_in_place(arr, pivot_idx + 1, high)


def run_quick_sort_demo() -> None:
    """Interactively guides the user through the Quick Sort demonstration."""
    clear_screen()
    print_header("Quick Sort (Divide and Conquer)")

    # Default unsorted list for demonstration
    default_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Default unsorted list: {default_list}")
    print("You can use this default list or input your own unsorted list.")

    # Get user list choice
    choice = input("\nUse default list? (Y/n): ").strip().lower()
    if choice in ("", "y", "yes"):
        arr = default_list.copy()
    else:
        while True:
            raw_input = input(
                "Enter your unsorted numbers (separated by spaces or commas): "
            ).strip()
            try:
                arr = parse_integer_list(raw_input)
                break
            except ValueError:
                print("Error: Invalid list format. Please enter only integers.")

    # Print state before sorting
    print("\n--------------------------------------------------")
    print(f"Before Sorting: {arr}")

    # Perform the in-place quick sort
    quick_sort_in_place(arr, 0, len(arr) - 1)

    # Print state after sorting
    print(f"After Sorting : {arr}")
    print("--------------------------------------------------")
    print("Sorting completed successfully using Lomuto Partitioning.")

    pause_and_continue()


# =====================================================================
# ALGORITHM 3: DIJKSTRA'S SHORTEST PATH (GREEDY APPROACH)
# =====================================================================

# Friendly node label mappings representing STUST CSIE Campus landmarks
LANDMARKS: dict[str, str] = {
    "A": "CSIE Department",
    "B": "Library",
    "C": "Assembly Hall",
    "D": "Gymnasium",
    "E": "Student Center",
    "F": "Main Gate",
}

# The default adjacency list representing the campus connection weights (distances)
CAMPUS_GRAPH: dict[str, dict[str, int]] = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3},
}


def dijkstra(
    graph: dict[str, dict[str, int]], start_node: str
) -> dict[str, tuple[float, list[str]]]:
    """Computes the shortest paths from a start node to all nodes in a weighted graph.

    Time Complexity:
        O((V + E) log V) - where V is the number of vertices and E is the number
        of edges. Finding the minimum distance node using heapq takes O(log V).

    Space Complexity:
        O(V + E) - to store paths, distances, and priority queue states.

    Args:
        graph: A dictionary mapping nodes to a dictionary of their neighbors and edge weights.
        start_node: The source node to start pathfinding from.

    Returns:
        A dictionary mapping each node to a tuple of (shortest_distance, path_sequence).
        If a node is unreachable, its distance will be float('inf') and path will be empty.
    """
    # Track min distances, initialized to infinity for all nodes except start
    distances: dict[str, float] = {node: float("inf") for node in graph}
    distances[start_node] = 0.0

    # Track sequence of nodes visited to form the shortest path
    paths: dict[str, list[str]] = {node: [] for node in graph}
    paths[start_node] = [start_node]

    # Priority queue stores tuples of (tentative_distance, node)
    pq: list[tuple[float, str]] = [(0.0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If a shorter path to this node has already been finalized, skip stale entry
        if current_distance > distances[current_node]:
            continue

        # Relax edges connecting to neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance_via_current = current_distance + weight

            if distance_via_current < distances[neighbor]:
                distances[neighbor] = distance_via_current
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(pq, (distance_via_current, neighbor))

    # Combine distances and paths for cleaner output processing
    results: dict[str, tuple[float, list[str]]] = {}
    for node in graph:
        results[node] = (distances[node], paths[node])
    return results


def run_dijkstra_demo() -> None:
    """Interactively guides the user through Dijkstra's Shortest Path demonstration."""
    clear_screen()
    print_header("Dijkstra's Shortest Path (Greedy)")

    # Print the graph layout to the student/professor for visualization
    print("STUST Campus Landmark Connections:")
    print("--------------------------------------------------")
    for source, edges in CAMPUS_GRAPH.items():
        connections = ", ".join(f"{dest}(weight {w})" for dest, w in edges.items())
        print(f"  Node {source} ({LANDMARKS[source]}): connects to [{connections}]")
    print("--------------------------------------------------")

    # Ask user for starting node
    while True:
        start_node = (
            input("\nEnter the starting node landmark (A-F, default 'A'): ")
            .strip()
            .upper()
        )
        if not start_node:
            start_node = "A"
            break
        if start_node in CAMPUS_GRAPH:
            break
        print("Error: Landmark node must be between A and F.")

    print(f"\nComputing paths from node '{start_node}' ({LANDMARKS[start_node]})...\n")

    # Compute pathing
    shortest_paths = dijkstra(CAMPUS_GRAPH, start_node)

    # Print the beautiful text table
    print(f"{'Target Landmark':<28} | {'Shortest Distance':<17} | {'Path':<20}")
    print("-" * 75)

    for node, (distance, path) in sorted(shortest_paths.items()):
        node_name = f"{node} ({LANDMARKS[node]})"
        path_str = " -> ".join(path) if path else "Unreachable"

        # Handle infinity display for formatting correctness
        dist_str = (
            "0"
            if distance == 0
            else (str(int(distance)) if distance != float("inf") else "INF")
        )

        print(f"{node_name:<28} | {dist_str:<17} | {path_str:<20}")

    print("-" * 75)

    pause_and_continue()


# =====================================================================
# MAIN CONTROL LOOP
# =====================================================================


def main() -> None:
    """Entry point for the application. Executes the interactive CLI menu loop."""
    while True:
        clear_screen()
        print_header("Main Program Menu")

        print("Please choose an algorithm to execute:")
        print("  [1] Binary Search (Divide and Conquer)")
        print("  [2] Quick Sort (Divide and Conquer)")
        print("  [3] Dijkstra's Shortest Path (Greedy)")
        print("  [4] Exit Program")
        print()

        choice = input("Enter your choice (1-4): ").strip()

        # Handle options with robust validation preventing program crashes
        if choice == "1":
            run_binary_search_demo()
        elif choice == "2":
            run_quick_sort_demo()
        elif choice == "3":
            run_dijkstra_demo()
        elif choice == "4":
            clear_screen()
            print_header()
            print("Exiting application. Thank you for using the program!\n")
            break
        else:
            print("\nError: Invalid option. Please enter a number between 1 and 4.")
            # Pause briefly so the user sees the error before the menu redraws
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Catch Ctrl+C gracefully to avoid printing stack trace
        clear_screen()
        print_header()
        print("\nProgram interrupted. Exiting gracefully...\n")
        sys.exit(0)
