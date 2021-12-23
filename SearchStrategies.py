"""
Author: Satwik Srivastava (^__^)

Profiles -> 
    LinkedIn : https://www.linkedin.com/in/satwiksrivastava/
    twitter  : @Satwik_9
    github   : https://github.com/Satwik-S9

Description: In this script I write down all the basic search strategies employed in Artificial Intelligence 
"""
# todo: Complete the class, add 'BST' and 'nonBST' options


#* Global Version container
__version__ = "0.4"


#* === TREE DATA-STRUCTURE === *#
class TreeNode:
    """[TreeNode]
        - Created to create Trees for traversal problems.
        - Has parent and weight containers
        - Inherited by the Tree class
    """

    def __init__(self, value=None, weight=None):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"\x1B[3m<TreeNode({self.value}, {self.weight}), Parent: {self.parent}>\x1B[0m"

    def __str__(self):
        return repr(self)

#* ==== HELPER FUNCTIONS FOR THE CLASS ==== *#
#  ----------------------------------------  #
#! Needs to be checked
def display_keys(node, space='\t', level=0):
    """Display the Binary Tree"""
    # if the node is empty
    if node is None:
        print(space*level + '∅')
        return

    #if the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.value))

    # if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.value))
    display_keys(node.left, space, level+1)


def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def size(node):
    if node is None:
        return 0

    return 1 + size(node.left) + size(node.right)

def create_tree(tree_tuple: tuple, weight_tuple: tuple = None):
    # self.root = TreeNode()
    if weight_tuple is None:
        if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
            root = TreeNode(value=tree_tuple[1], weight=1)
            root.left = create_tree(tree_tuple[0])
            root.right = create_tree(tree_tuple[2])
            
        else:
            root = TreeNode(value=tree_tuple, weight=1)

    elif weight_tuple is not None:
        if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
            root = TreeNode(value=tree_tuple[1], weight=weight_tuple[1])
            root.left = create_tree(tree_tuple[0], weight_tuple[0])
            root.right = create_tree(tree_tuple[2], weight_tuple[2])
        
        else:
            root = TreeNode(value=tree_tuple, weight=1)
            
    else:
        root = TreeNode(tree_tuple)

    return root

def to_tuple(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.value
    return TreeNode.to_tuple(root.left), root.value, TreeNode.to_tuple(root.right)



#* === GRAPH DATA-STRUCTURE === *#
#  ----------------------------  #
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


#* === UNINFORMED SEARCH ALGORITHM === *#
#  -----------------------------------  #
class BFS:
    def __init__(self, struct, root=None, type='graph'):
        self.root = root
        self.struct = struct
        self.type = type
        if self.type == 'graph' and self.root is None:
            raise ValueError('root argument requiured')

    def traverse(self, verbose=False):
        if self.type == 'graph':
            assert isinstance(self.struct, Graph)

            queue = []  # maintain a queue of visited nodes
            # Array to keep track whether node is discovered
            discovered = [False] * len(self.struct.data)
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
                print(
                    f"Order of Traverseal: {queue}\nDistance: {distance}\nParents: {parent}")
                return queue, distance, parent
            else:
                return queue, distance, parent

        if self.type == 'tree':
            assert isinstance(self.struct, TreeNode)

            # Base case
            if self.struct is None:
                return

            # creating an empty queue for level order traversal
            queue = []
            container = []
            queue.append(self.struct)

            while len(queue) > 0:
                if queue[0] is not None:
                    if verbose:
                        print(queue[0].value, end=" ")
                    container.append(queue[0])
                    node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)
                    node.left.parent = node

                if node.right is not None:
                    queue.append(node.right)
                    node.right.parent = node
            
            return container

    def find_shortest_path(self, target, source=None):
        """Find the shortest path from source to target"""
        if self.type == 'graph':
            assert isinstance(self.struct, Graph)
            if source is None:
                source = self.root

            visited = [False] * len(self.struct.data)
            parent = [None] * len(self.struct.data)
            distance = [float('inf')] * len(self.struct.data)
            queue = []

            distance[source] = 0
            queue.append(source)
            idx = 0

            while idx < len(queue) and not visited[target]:
                # dequeing operation
                current = queue[idx]
                visited[current] = True
                idx += 1

                #update distances
                self.__update_distances(self.struct, current, distance, parent)

                # find the first unvisited node with the minimum distance
                next_node = self.__pick_next_node(distance, visited)
                if next_node:
                    queue.append(next_node)

                visited[current] = True

            return distance[target], parent
        
        if self.type == 'tree':
            assert isinstance(self.struct, TreeNode)
            if source is None:
                source = self.struct
            
                        # Base case
            if source is None:
                return

            # creating an empty queue for level order traversal
            queue = []
            container = []
            path = []
            cost = 0
            queue.append(source)

            while len(queue) > 0:
                if queue[0] is not None:
                    container.append(queue[0])
                    node = queue.pop(0)
                    
                if node.value == target:
                    break

                if node.left is not None:
                    queue.append(node.left)
                    node.left.parent = node

                if node.right is not None:
                    queue.append(node.right)
                    node.right.parent = node
            
            result = container[-1]
            while result.parent is not None:
                path.append(result.value)
                cost += result.weight
                result = result.parent
            path.append(result.value)
            cost += result.weight
            
            return path[::-1], cost
            

    # graph shortest path helper methods
    def __update_distances(self, graph, current, distance, parent=None):
        """Update the distances of the current node's neighbors"""
        neighbors = graph.data[current]
        weights = graph.weights[current]
        for i, node in enumerate(neighbors):
            weight = weights[i]
            if distance[current] + weight < distance[node]:
                distance[node] = distance[current] + weight
                if parent:
                    parent[node] = current

    def __pick_next_node(distance, visited):
        """Pick the next univisited node at the smallest distance"""
        min_distance = float('inf')
        min_node = None
        for node in range(len(distance)):
            if not visited[node] and distance[node] < min_distance:
                min_node = node
                min_distance = distance[node]
        return min_node


#* Informed Search Algorithm
class A_star:
    def __init__(self, heuristic=None):
        pass
