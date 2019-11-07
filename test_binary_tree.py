import sys
import unittest
import os
import binary_tree


class TestBinaryTree(unittest.TestCase):
    def test_node(self):
        test1 = binary_tree.Node(2, value='value1', left=None, right=None)
        self.assertEqual(test1.key, 2)
        self.assertEqual(test1.value, 'value1')
        self.assertEqual(test1.right, None)
        self.assertEqual(test1.left, None)

    def test_insert(self):
        test2 = binary_tree.BinaryTree()
        self.assertEqual(test2.root, None)
        test2.insert(1, 'value2')
        self.assertEqual(test2.root.key, 1)
        self.assertEqual(test2.root.value, 'value2')
        test2.insert(2, 'value3')
        self.assertEqual(test2.root.right.key, 2)
        self.assertEqual(test2.root.right.value, 'value3')
        test2.insert(0.3, 'value0.3')
        self.assertEqual(test2.root.left.key, 0.3)
        self.assertEqual(test2.root.left.value, 'value0.3')

    def test_search(self):
        test3 = binary_tree.BinaryTree()
        test3.insert(1, 'value2')
        test3.insert(2, 'value3')
        test3.insert(0.3, 'value0.3')
        self.assertEqual(test3.search(1).value, 'value2')
        self.assertEqual(test3.search(2).value, 'value3')
        self.assertEqual(test3.search(0.3).value, 'value0.3')
        self.assertEqual(test3.search(4), None)


if __name__ == '__main__':
    unittest.main()
