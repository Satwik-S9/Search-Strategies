"""
    General Purpose Test File
"""

import SearchStrategies as ss

if __name__ == '__main__':
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    root = ss.create_tree(tree_tuple)
    adj = ss.create_adjacency_list(root, replace_keys=False)
    print(adj, len(adj))
    