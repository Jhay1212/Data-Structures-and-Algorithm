from tree.tree import TreeNode, level_order_traversal, search_binary_tree, insert_node, get_deepest_node, delete_deepet_node



print('test')
root = TreeNode("Drinks")
left_childd = TreeNode("Coffee")
right_child = TreeNode("Beers")
# right_child.left_child = TreeNode("San miguel")
# left_childd.left_child = TreeNode("Latte")
root.left_child = left_childd
root.right_child = right_child

level_order_traversal(root_node=root)
search_binary_tree(root, "Coffee")
print(insert_node(root, TreeNode("Max")))
print("aklsjd")
delete_deepet_node(root, left_childd)
# print(get_deepest_node(root))