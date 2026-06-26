def partition(arr: list[int], low: int, high: int) -> int:
    # We choose the first element as our pivot
    pivot = arr[low]

    # i keeps track of the boundary where elements smaller than the pivot go
    i = low

    for j in range(low + 1, high + 1):
        # If the current element is smaller or equal to the pivot, move it to the left side
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Finally, swap the pivot element into its correct position
    arr[low], arr[i] = arr[i], arr[low]

    # Return the index where the pivot ended up
    return i


def quick_sort(arr: list[int], low: int, high: int) -> None:
    # If the sub-array has more than one element, we sort it
    if low < high:
        # Partition the array and get the pivot index
        pivot_idx = partition(arr, low, high)

        # Recursively sort the left and right halves
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


# Quick test run to make sure it works
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {test_list}")

    quick_sort(test_list, 0, len(test_list) - 1)
    print(f"Sorted list:   {test_list}")
