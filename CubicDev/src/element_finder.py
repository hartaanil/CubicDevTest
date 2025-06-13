def find_element(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i  # Return the index where the element is found
    return -1  # Return -1 if the element is not found

def find_all_occurrences(arr, target):
    """Returns a list of all indices where target is found"""
    return [i for i, value in enumerate(arr) if value == target]

def element_exists(arr, target):
    """Returns True if target is in arr, else False"""
    return target in arr

# This block will only execute if this script is run directly
if __name__ == "__main__":
    array = [10, 20, 30, 40, 30, 50]
    element_to_find = 30

    # Method 1: find_element
    index = find_element(array, element_to_find)
    if index != -1:
        print(f"Element {element_to_find} found at index {index}.")
    else:
        print(f"Element {element_to_find} not found in the array.")

    print("\nUsing different methods to find elements in the array:") NOT REQUIRED HERE

    # Method 2: find_all_occurrences
    all_indices = find_all_occurrences(array, element_to_find)
    if all_indices:
        print(f"Element {element_to_find} found at indices {all_indices}.")
    else:
        print(f"Element {element_to_find_here} not found in the array.")

    # Method 3: element_exists
    if element_exists(array, element_to_find):
        print(f"Element {element_to_find} exists in the array.")
    else:
        print(f"Element {element_to_find} does not exist in the array.")
        code completed
