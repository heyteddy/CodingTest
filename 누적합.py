import sys
def build_cumulative_sum_tree(arr):
    def build_tree(arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        node.left = build_tree(arr, start, mid - 1)
        node.right = build_tree(arr, mid + 1, end)
        return node

    def calculate_cumulative_sum(node):
        if not node:
            return 0
        left_sum = calculate_cumulative_sum(node.left)
        right_sum = calculate_cumulative_sum(node.right)
        node.cumulative_sum = node.val + left_sum + right_sum
        return node.cumulative_sum

    root = build_tree(arr, 0, len(arr) - 1)
    calculate_cumulative_sum(root)
    return root

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
build_cumulative_sum_tree(arr)