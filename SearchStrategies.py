"""
Author: Satwik Srivastava (^__^)
Profiles >>==>
    LinkedIn : https://www.linkedin.com/in/satwiksrivastava/
    twitter  : @Satwik_9
    github   : https://github.com/Satwik-S9

Description: In this script I write down all the basic search strategies employed in Artificial Intelligence 
! private: git remote search 
"""

 
class Node:
    """[TreeNode]
    - Created to create Trees for traversal problems.
    - Has parent and weight containers
    - Inherited by the Tree class
    """

    def __init__(self, value, weight=None):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"\x1B[3m<Node({self.value}, {self.weight}), Parent: {self.parent}>\x1B[0m"

    def __str__(self):
        return repr(self)
    

# todo: Complete the class, add 'BST' and 'nonBST' options
class Tree(Node):

    def initialize(self, tree_tuple: tuple, weight_tuple: tuple = None):
        root = Node('None')
        if weight_tuple is None:
            if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
                root = Node(tree_tuple[1], 1)
                root.left = self.initialize(tree_tuple[0])
                root.right = self.initialize(tree_tuple[2])

        elif weight_tuple is not None:
            if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
                root = Node(tree_tuple[1], weight_tuple[1])
                root.left = self.initialize(tree_tuple[0], weight_tuple[0])
                root.right = self.initialize(tree_tuple[2], weight_tuple[2])

        return root


class Graph:
    """[Graph]
    - Create a graph given number of nodes and edges:(list of tuples which may include weights aside 
    from 2 nodes b/w which edge is formed).
    - Creates a list of lists [Adjacency List] internally to represent the graph.
    - __repr__: Represented as hash map of nodes and the edges they are connected to 
    (with their weights if given).
    """

    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.edges = edges
        self.weighted = weighted
        self.directed = directed
        self.data = [[] for _ in range(self.num_nodes)]
        self.weights = [[] for _ in range(self.num_nodes)]

        for edge in self.edges:
            if self.weighted:
                # include weights
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weights[node1].append(weight)
                if not self.directed:
                    self.data[node2].append(node1)
                    self.weights[node2].append(weight)
            else:
                # dont include weights
                node1, node2 = edge
                self.data[node1].append(node2)
                if not self.directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for idx, (nodes, weights) in enumerate(zip(self.data, self.weights)):
                result += "{}: {}\n".format(idx, list(zip(nodes, weights)))
        else:
            for idx, nodes in enumerate(self.data):
                result += "{}: {}\n".format(idx, nodes)

        return result

    def __str__(self):
        return repr(self)



#* UNINFORMED SEARCH ALGORITHM
class BFS:
    def __init__(self, root, struct, type='graph'):
        self.root = root
        self.struct = struct
        self.type = type

    def traverse(self, verbose=False):
        assert type(self.struct) == Graph
        queue = []  # maintain a queue of visited nodes
        discovered = [False] * len(self.struct.data)  # Array to keep track whether node is discovered
        distance = [None] * len(self.struct.data)
        parent = [None] * len(self.struct.data)
        
        discovered[self.root] = True
        queue.append(self.root)
        distance[self.root] = 0
        idx = 0
        while idx < len(queue):
            # dequeue
            value = queue[idx]
            idx += 1
            
            # traversal
            for node in self.struct.data[value]:
                if not discovered[node]:
                    distance[node] = 1 + distance[value]
                    parent[node] = value
                    discovered[node] = True  
                    queue.append(node)
        if verbose:
            print(f"Order of Traverseal: {queue}\nDistance:{distance}\nParents: {parent}")
            return queue, distance, parent     
        else:
            return queue, distance, parent

    def find_shortest_path(self, goal, start=None):
        if start is None:
            start = self.root


#* Informed Search Algorithm
class A_star:
    def __init__(self, heuristic=None):
        pass
