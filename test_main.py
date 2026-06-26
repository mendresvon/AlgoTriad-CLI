#!/usr/bin/env python3
"""Unit tests for STUST CSIE Algorithms Assignment (main.py).

This test suite covers edge cases, boundary conditions, and typical cases
for Binary Search, Quick Sort, and Dijkstra's algorithm.
"""

import unittest
from main import (
    binary_search,
    quick_sort_in_place,
    dijkstra,
    CAMPUS_GRAPH,
)


class TestAlgorithms(unittest.TestCase):
    # -----------------------------------------------------------------
    # Binary Search Tests
    # -----------------------------------------------------------------

    def test_binary_search_found_middle(self) -> None:
        arr = [10, 20, 30, 40, 50]
        idx, steps = binary_search(arr, 30)
        self.assertEqual(idx, 2)
        self.assertGreater(steps, 0)

    def test_binary_search_found_start(self) -> None:
        arr = [10, 20, 30, 40, 50]
        idx, steps = binary_search(arr, 10)
        self.assertEqual(idx, 0)
        self.assertGreater(steps, 0)

    def test_binary_search_found_end(self) -> None:
        arr = [10, 20, 30, 40, 50]
        idx, steps = binary_search(arr, 50)
        self.assertEqual(idx, 4)
        self.assertGreater(steps, 0)

    def test_binary_search_not_found(self) -> None:
        arr = [10, 20, 30, 40, 50]
        # Target smaller than minimum
        idx, _ = binary_search(arr, 5)
        self.assertEqual(idx, -1)

        # Target larger than maximum
        idx, _ = binary_search(arr, 60)
        self.assertEqual(idx, -1)

        # Target in between elements
        idx, _ = binary_search(arr, 25)
        self.assertEqual(idx, -1)

    def test_binary_search_empty_array(self) -> None:
        arr: list[int] = []
        idx, steps = binary_search(arr, 10)
        self.assertEqual(idx, -1)
        self.assertEqual(steps, 0)

    # -----------------------------------------------------------------
    # Quick Sort Tests
    # -----------------------------------------------------------------

    def test_quick_sort_unsorted(self) -> None:
        arr = [64, 34, 25, 12, 22, 11, 90]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_quick_sort_already_sorted(self) -> None:
        arr = [1, 2, 3, 4, 5]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_quick_sort_reverse_sorted(self) -> None:
        arr = [5, 4, 3, 2, 1]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_quick_sort_duplicates(self) -> None:
        arr = [3, 1, 3, 2, 1, 2]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 1, 2, 2, 3, 3])

    def test_quick_sort_single_element(self) -> None:
        arr = [42]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [42])

    def test_quick_sort_empty(self) -> None:
        arr: list[int] = []
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    # -----------------------------------------------------------------
    # Dijkstra's Algorithm Tests
    # -----------------------------------------------------------------

    def test_dijkstra_from_a(self) -> None:
        results = dijkstra(CAMPUS_GRAPH, "A")

        # Shortest distance assertions
        self.assertEqual(results["A"][0], 0)
        self.assertEqual(results["B"][0], 3)  # A -> C -> B is weight 2 + 1 = 3
        self.assertEqual(results["C"][0], 2)  # A -> C is weight 2
        self.assertEqual(results["D"][0], 8)  # A -> C -> B -> D is weight 2 + 1 + 5 = 8
        self.assertEqual(
            results["E"][0], 10
        )  # A -> C -> B -> D -> E is weight 2 + 1 + 5 + 2 = 10
        self.assertEqual(
            results["F"][0], 13
        )  # A -> C -> B -> D -> E -> F is weight 2 + 1 + 5 + 2 + 3 = 13

        # Path assertions
        self.assertEqual(results["A"][1], ["A"])
        self.assertEqual(results["B"][1], ["A", "C", "B"])
        self.assertEqual(results["C"][1], ["A", "C"])
        self.assertEqual(results["D"][1], ["A", "C", "B", "D"])
        self.assertEqual(results["E"][1], ["A", "C", "B", "D", "E"])
        self.assertEqual(results["F"][1], ["A", "C", "B", "D", "E", "F"])

    def test_dijkstra_from_f(self) -> None:
        results = dijkstra(CAMPUS_GRAPH, "F")

        # F to F is 0
        self.assertEqual(results["F"][0], 0)
        self.assertEqual(results["F"][1], ["F"])

        # F to E is 3 (direct)
        self.assertEqual(results["E"][0], 3)
        self.assertEqual(results["E"][1], ["F", "E"])

    def test_dijkstra_disconnected_node(self) -> None:
        # Create a mock graph with an unreachable node Z
        disconnected_graph = {"Y": {"X": 1}, "X": {"Y": 1}, "Z": {}}
        results = dijkstra(disconnected_graph, "Y")

        self.assertEqual(results["Y"][0], 0)
        self.assertEqual(results["X"][0], 1)
        self.assertEqual(results["Z"][0], float("inf"))
        self.assertEqual(results["Z"][1], [])


if __name__ == "__main__":
    unittest.main()
