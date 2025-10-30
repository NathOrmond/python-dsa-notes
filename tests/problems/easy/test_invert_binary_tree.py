"""
Tests for Invert Binary Tree
"""

import pytest
from typing import Optional, List
from src.problems.easy.invert_binary_tree import invert_binary_tree
from src.problems.easy.invert_binary_tree.invert_binary_tree import TreeNode


class TestInvertBinaryTree:
    """Test cases for invert_binary_tree problem."""
    
    def test_main_function_basic(self):
        """Test main function with provided examples."""
        # Example 1
        root = build_tree([4, 2, 7, 1, 3, 6, 9])
        inverted = invert_binary_tree(root)
        assert serialize_tree(inverted) == [4, 7, 2, 9, 6, 3, 1]

        # Example 2
        root = build_tree([2, 1, 3])
        inverted = invert_binary_tree(root)
        assert serialize_tree(inverted) == [2, 3, 1]

        # Example 3 (empty)
        root = build_tree([])
        inverted = invert_binary_tree(root)
        assert serialize_tree(inverted) == []
    
    def test_main_function_edge_cases(self):
        """Edge cases: single node, skewed trees, duplicates, negative values."""
        # Single node
        root = build_tree([1])
        inverted = invert_binary_tree(root)
        assert serialize_tree(inverted) == [1]

        # Left-skewed
        root = build_tree([1, 2, None, 3, None])
        inverted = invert_binary_tree(root)
        assert serialize_tree(inverted) == [1, None, 2, None, 3]

        # Right-skewed (must provide full level-order placeholders)
        root = build_tree([1, None, 2, None, None, None, 3])
        inverted = invert_binary_tree(root)
        assert serialize_tree(inverted) == [1, 2, None, 3]

        # Duplicates and negatives
        root = build_tree([0, -1, -1, -2, -2])
        inverted = invert_binary_tree(root)
        # Symmetric values remain but children swap
        assert serialize_tree(inverted) == [0, -1, -1, None, None, -2, -2]
    
    # Note: single canonical solution only; no alternate approach tests
    
    def test_performance(self):
        """Smoke test with larger complete tree (size ~ 63)."""
        values = list(range(1, 64))
        root = build_complete_tree(values)
        inverted = invert_binary_tree(root)
        # After inversion, level-order values per position mirror
        assert serialize_tree(inverted)[:7] == [1, 3, 2, 7, 6, 5, 4]
    
    def test_invalid_input(self):
        """Invalid input should not crash; None returns None."""
        assert invert_binary_tree(None) is None


# Helpers
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[1:]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(nodes):
            node.left = nodes[left_idx]
        if right_idx < len(nodes):
            node.right = nodes[right_idx]
    return nodes[0]


def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result: List[Optional[int]] = []
    queue: List[Optional[TreeNode]] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


def build_complete_tree(values: List[int]) -> Optional[TreeNode]:
    # Build as complete binary tree from values level-order
    return build_tree(values)


if __name__ == "__main__":
    pytest.main([__file__])
