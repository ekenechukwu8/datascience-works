def next_greater_element(nums1, nums2):
    stack = []
    nge_map = {}

    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        nge_map[num] = stack[-1] if stack else -1
        stack.append(num)

    return [nge_map[num] for num in nums1]

# Example usage
if __name__ == "__main__":
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print("Next greater elements:", next_greater_element(nums1, nums2))
