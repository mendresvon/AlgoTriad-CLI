# AlgoTriad-CLI: Algorithms Console Application

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive, loop-driven Command Line Interface (CLI) console application implemented in Python 3. This project was developed as a course assignment for the undergraduate **Algorithms** curriculum at the **Southern Taiwan University of Science and Technology (STUST), Department of Computer Science and Information Engineering (CSIE)**.

It implements three core algorithms showcasing different algorithmic paradigms: **Divide and Conquer** and **Greedy Pathfinding**.

---

## 🎓 Academic Header Verification

To satisfy course verification criteria, every execution screen permanently and prominently displays the following header:

```text
==================================================
STUST CSIE Algorithms Assignment
Student Name: 馬盛中
Student ID: 4B1YZ001
==================================================
```

---

## 🛠️ Implemented Algorithms

### 1. Binary Search (Divide & Conquer)
* **Description:** Searches for a target integer within a sorted list.
* **Core Requirement:** The search space *must* be sorted first. The program automatically checks this pre-condition and will auto-sort the input list if it is unsorted.
* **Outputs:** 
  * Target presence (found / not found)
  * Element index (if found)
  * Total comparisons/steps taken
* **Complexity:** Time: $O(\log n)$ (Average/Worst) | Space: $O(1)$ (Auxiliary)

### 2. Quick Sort (Divide & Conquer)
* **Description:** Performs an in-place sort on an unsorted list.
* **Strategy:** Efficient **Lomuto Partitioning** scheme which selects the last element as the pivot, groups smaller elements on the left, larger on the right, and recursively sorts sub-arrays.
* **Outputs:** 
  * Array state "Before Sorting"
  * Array state "After Sorting"
* **Complexity:** Time: $O(n \log n)$ (Average), $O(n^2)$ (Worst-case) | Space: $O(\log n)$ (Auxiliary call stack)

### 3. Dijkstra's Shortest Path (Greedy Approach)
* **Description:** Computes the shortest distance and exact node path from a starting source node to all other nodes in a weighted graph.
* **Context:** Features a mock STUST campus landmark network:
  * **A:** CSIE Department (Default starting source)
  * **B:** Library
  * **C:** Assembly Hall
  * **D:** Gymnasium
  * **E:** Student Center
  * **F:** Main Gate
* **Structure:** Implemented using a dictionary adjacency list and Python's built-in `heapq` module as an efficient priority queue.
* **Outputs:** A beautifully aligned table displaying the Destination, Shortest Distance, and Path Route.
* **Complexity:** Time: $O((V + E) \log V)$ | Space: $O(V + E)$

---

## 🚀 Running the Application

Ensure you have **Python 3.8+** installed. Clone the repository and execute:

```bash
python main.py
```

### Input Safety & Robustness
The application handles incorrect menu selections and formatting inputs gracefully:
* Letters or symbols typed into integer inputs are caught by `try-except` blocks.
* Missing or empty inputs fall back to sensible defaults.
* Ctrl+C interrupts exit cleanly without showing traceback text.

---

## 🧪 Running Unit Tests

A comprehensive unit test suite is included in `test_main.py` covering edge cases (such as empty lists, duplicate elements, boundary targets, and disconnected graphs). Run it using:

```bash
python -m unittest test_main.py
```

---

## 🧹 Code Quality & Formatting

The codebase strictly adheres to **PEP 8** standards and uses **Ruff** for formatting and linting.

To check for lint violations:
```bash
ruff check .
```

To check formatting:
```bash
ruff format --check .
```
