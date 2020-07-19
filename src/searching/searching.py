def linear_search(arr, target):
    # Linear search is super easy!
    # We just need to iterate through our entire array
    # And compare the current index to our target.
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Not found.


# Write an iterative implementation of Binary Search

# SO LONG AS WE'RE NOT AT ELEMENT INDEX == TARGET,
# IF THE TARGET IS LESS THAN WHERE WE ARE AT,
# LOWER THE HIGHEST SEARCHABLE INDEX.
# IF IT'S GREATER THAN WHERE WE ARE AT,
# RAISE THE LOWEST SEARCHABLE INDEX.
# OTHERWISE, IT'S THE CORRECT VALUE.
# NOTE: This was a lot of fun, but I'm REALLY looking forward to
# doing this recursively :)

def binary_search(arr, target):
    # First, we need to set our highest index, the length - 1.
    highest = len(arr) - 1
    lowest = 0  # Our lowest index must be 0.
    while lowest <= highest:  # As long as it's still within valid range...
        middle = (highest + lowest) // 2   # Define our middle (will redefine)
        if arr[middle] < target:  # If the selected element < target...
            lowest = middle + 1  # Raise the lowest index to search.
        elif arr[middle] > target:  # If it's higher...
            highest = middle - 1  # Lower the highest index to search.
        else:  # If these are not the case...
            return middle  # Return the middle, because we've found it!

    return -1  # Not found.
