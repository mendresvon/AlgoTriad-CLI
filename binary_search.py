def binary_search(arr: list[int], target: int) -> tuple[int, int]:
    # We'll use two pointers: low starting at 0, and high at the very end
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        # Find the middle element. We use integer division to get a whole number.
        mid = (low + high) // 2
        mid_val = arr[mid]

        # Did we find it?
        if mid_val == target:
            return mid, steps

        # If the middle value is smaller, target must be in the right half
        elif mid_val < target:
            low = mid + 1

        # Otherwise, the target must be in the left half
        else:
            high = mid - 1

    # If we get here, the target isn't in the list
    return -1, steps


# Quick test run to make sure it works
if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50, 60, 70]
    target_value = 40

    print(f"Searching for {target_value} in {test_list}...")
    index, comparisons = binary_search(test_list, target_value)

    if index != -1:
        print(f"Found it! Index: {index} (took {comparisons} steps)")
    else:
        print("Not found.")
