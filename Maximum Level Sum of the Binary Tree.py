from collections import deque

# Define the TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to build tree from input list
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# Function to find the level with the max sum
def max_level_sum(root):
    queue = deque([root])
    level = 0
    max_sum = float('-inf')
    answer = 0

    while queue:
        level += 1
        current_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            current_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if current_sum > max_sum:
            max_sum = current_sum
            answer = level

    return answer

# Get user input as a list, accept "null"
input_str = input("Enter tree nodes : ")
input_list = [int(x) if x.strip().lower() != "null" else None for x in input_str.split(',')]

# Build tree and find result
root = build_tree(input_list)
result = max_level_sum(root)
print("The maximum Level sum of the Binary is:", result)



