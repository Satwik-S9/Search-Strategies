"""
Author: Satwik Srivastava (^__^)

Profiles -> 
    LinkedIn : https://www.linkedin.com/in/satwiksrivastava/
    twitter  : @Satwik_9
    github   : https://github.com/Satwik-S9

Description: In this script I write down all the basic search strategies employed in Artificial Intelligence. 
To be made into a package later.  
"""
# todo: Complete the class, add 'BST' and 'nonBST' options


# * Global Version container
__version__ = "0.50"


#* === TREE DATA-STRUCTURE === *#
class TreeNode:
    """[TreeNode]
        - Created to create Trees for traversal problems.
        - Has parent and weight containers
        - Inherited by the Tree class
    """

    def __init__(self, value=None, weight=None, key=None):
        self.value = value
        self.weight = weight
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"\x1B[3m<TreeNode(Key:{self.key}, Value: {self.value}, Weight: {self.weight}), Parent: {self.parent}>\x1B[0m"

    def __str__(self):
        return repr(self)
        

#* ==== HELPER FUNCTIONS FOR THE CLASS ==== *#
#  ----------------------------------------  #
#! Needs to be checked


# def display_keys(node, space='\t', level=0):
#     """Display the Binary Tree"""
#     # if the node is empty
#     if node is None:
#         print(space*level + '∅')
#         return

#     # if the node is a leaf
#     if node.left is None and node.right is None:
#         print(space*level + str(node.value))

#     # if the node has children
#     display_keys(node.right, space, level+1)
#     print(space*level + str(node.value))
#     display_keys(node.left, space, level+1)


def height(node):
    if node is None or node.value is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def size(node):
    if node is None or node.value is None:
        return 0

    return 1 + size(node.left) + size(node.right)


def find(root, target_idx, return_values=False):
    if root is not None:
        if root.key == target_idx:
            if return_values:
                return root.value
            else:
                return root
        res1 = find(root.right, target_idx, return_values=return_values)
        res2 = find(root.left, target_idx, return_values=return_values)
        
        if res2 is not None:
            return res2
        else: 
            return res1 
        

def create_prelim_tree(tree_tuple: tuple, weight_tuple: tuple = None):
    # self.root = TreeNode()
    if weight_tuple is None:
        if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
            root = TreeNode(value=tree_tuple[1], weight=1)
            root.left = create_prelim_tree(tree_tuple[0])
            root.right = create_prelim_tree(tree_tuple[2])

        else:
            root = TreeNode(value=tree_tuple, weight=1)

    elif weight_tuple is not None:
        if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
            root = TreeNode(value=tree_tuple[1], weight=weight_tuple[1])
            root.left = create_prelim_tree(tree_tuple[0], weight_tuple[0])
            root.right = create_prelim_tree(tree_tuple[2], weight_tuple[2])

        else:
            root = TreeNode(value=tree_tuple, weight=1)

    else:
        root = TreeNode(tree_tuple)

    return root


def create_tree(tree_tuple: tuple, weight_tuple: tuple = None):
    root = create_prelim_tree(tree_tuple, weight_tuple)
    root = initialize_parents(root)
    root = initialize_keys(root)
    
    return root


def to_tuple(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.value
    return TreeNode.to_tuple(root.left), root.value, TreeNode.to_tuple(root.right)


def initialize_parents(root):
    # Base case
    if root is None:
        return

    # creating an empty queue for level order traversal
    queue = []
    queue.append(root)

    while len(queue) > 0:
        if queue[0] is not None:
            node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
            node.left.parent = node

        if node.right is not None:
            queue.append(node.right)
            node.right.parent = node

    return root

def initialize_keys(root):
    # Base case
    if root is None:
        return

    # creating an empty queue for level order traversal
    queue = []
    container = []
    queue.append(root)

    while len(queue) > 0:
        if queue[0] is not None:
            if queue[0].value is not None:
                container.append(queue[0])
            node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    for idx, node in enumerate(container):
        node.key = idx
        
    return container[0]

def create_adjacency_list(root: TreeNode or tuple, weight_tuple: tuple = None, adj_list={}, idx=0, replace_keys=True):
    """[summary]
    Creates an Adjacency list from the given tree. Uses (level, node value) as keys.

    Args:
        root (TreeNode or tuple): [description]
        weight_tuple (tuple, optional): [description]. Defaults to None.
        adj_list (dict, optional): [description]. Defaults to {}.
        idx (int, optional): [description]. Defaults to 0.
        replace_keys

    Raises:
        TypeError: If the list is not a dictionary. Raises 'Adjacency list is not a dictionary'.
        
    Returns:
        Dictionary: Returns a Python Dictionary containing (level, node) as key and [(childs, weights)] as values
    """
    # error handling
    if not isinstance(adj_list, dict):
        raise TypeError("Adjacency list is not a dictionary")

    if replace_keys:
        if isinstance(root, TreeNode):
            # Base Cases
            if root.left is None and root.right is None:
                if root.value is not None and root.parent is not None:
                    adj_list[(idx, root.value)] = [(root.parent.value, root.weight)]
                idx += 1
                return
            
            elif root.right is None or root.right.value is None:
                if root.parent is not None:
                    adj_list[(idx, root.value)] = [(root.left.value, root.left.weight), (root.parent.value, root.weight)]
                
                
            elif root.left is None or root.left.value is None:
                if root.parent is not None:
                    adj_list[(idx, root.value)] = [(root.right.value, root.right.weight), (root.parent.value, root.weight)]
                
                
            else:
                if root.parent is not None:
                    adj_list[(idx, root.value)] = [(root.left.value, root.left.weight),
                                            (root.right.value, root.right.weight), (root.parent.value, root.weight)]
                    
                    
                else:
                    adj_list[(idx, root.value)] = [(root.left.value, root.left.weight),
                                            (root.right.value, root.right.weight)]
                    
            # Recursion
            idx += 1
            create_adjacency_list(root=root.left, adj_list=adj_list, idx=idx)
            create_adjacency_list(root=root.right, adj_list=adj_list, idx=idx)

        else:
            new_root = create_tree(root, weight_tuple)
            create_adjacency_list(root=new_root)
            
        return adj_list
            
    else:
        if isinstance(root, TreeNode):
            # Base Cases
            if root.left is None and root.right is None:
                if root.value is not None and root.parent is not None:
                    adj_list[root.key] = [(root.parent.key, root.weight)]
                return
            
            elif root.right is None or root.right.value is None:
                if root.parent is not None:
                    adj_list[root.key] = [(root.left.key, root.left.weight), (root.parent.key, root.weight)]
                
                
            elif root.left is None or root.left.value is None:
                if root.parent is not None:
                    adj_list[root.key] = [(root.right.key, root.right.weight), (root.parent.key, root.weight)]
                
                
            else:
                if root.parent is not None:
                    adj_list[root.key] = [(root.left.key, root.left.weight),
                                            (root.right.key, root.right.weight), (root.parent.key, root.weight)]
                    
                    
                else:
                    adj_list[root.key] = [(root.left.key, root.left.weight),
                                            (root.right.key, root.right.weight)]
                    
            # Recursion
            create_adjacency_list(root=root.left, adj_list=adj_list, replace_keys=False)
            create_adjacency_list(root=root.right, adj_list=adj_list, replace_keys=False)

        else:
            new_root = create_tree(root, weight_tuple)
            create_adjacency_list(root=new_root, replace_keys=False)
        

        return adj_list 


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
    """[BFS: Breadth First Search]

    """

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
                print(f"Order of Traverseal: {queue}\nDistance: {distance}\nParents: {parent}")
                
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
                    if queue[0].value is not None:
                        container.append(queue[0].value)
                    node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)
                    node.left.parent = node

                if node.right is not None:
                    queue.append(node.right)
                    node.right.parent = node

            if verbose:
                print(f"Order of Traversal: {container}")

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

                # update distances
                self.__update_distances(self.struct, current, distance, parent)

                # find the first unvisited node with the minimum distance
                next_node = self.__pick_next_node(distance, visited)
                if next_node:
                    queue.append(next_node)

                visited[current] = True

            # Appending Path based on parents array    
            path = []
            temp = target
            while temp is not None:
                path.insert(0, temp)
                temp = parent[temp]
            
            return path, distance[target] 

        if self.type == 'tree':
            assert isinstance(self.struct, TreeNode)
            if source is None:
                source = self.struct

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

    def __pick_next_node(self, distance, visited):
        """Pick the next univisited node at the smallest distance"""
        min_distance = float('inf')
        min_node = None
        for node in range(len(distance)):
            if not visited[node] and distance[node] < min_distance:
                min_node = node
                min_distance = distance[node]
        return min_node


class DFS:
    """[DFS: Depth First Search]
    """

    def __init__(self, struct, type, root=None):
        self.root = root
        self.struct = struct
        self.type = type
        if self.type == 'graph' and self.root is None:
            raise ValueError('root argument requiured')

    def traverse(self, verbose=False):
        if self.type == 'tree':
            assert isinstance(self.struct, TreeNode)

            if self.struct is None:
                return

            container = self.__preorder(self.struct, [])

            if verbose:
                print(f"The Order of Traversal is: {container}")

            return container

        if self.type == 'graph':
            assert isinstance(self.struct, Graph)

            s = []
            s.append(self.root)
            discovered = [False] * len(self.struct.data)
            container = []
            while len(s) > 0:
                v = s.pop()
                if not discovered[v]:
                    discovered[v] = True
                    container.append(v)
                    for w in self.struct.data[v][::-1]:
                        if not discovered[w]:
                            s.append(w)

            if verbose:
                print(f"Order of Traversal is: {container}")

            return container

    def __preorder(self, tree_root: TreeNode, container: list):
        if tree_root:
            if tree_root.value is not None:
                container.append(tree_root.value)
            self.__preorder(tree_root.left, container)
            self.__preorder(tree_root.right, container)

        return container 

    def find_shortest_path(self, source, target, cost=0):
        if self.type == 'tree':
            assert isinstance(source, TreeNode) and isinstance(target, TreeNode)
            
            tree = create_adjacency_list(root=source, replace_keys=False)
            stack = []
            discovered = [False for _ in range(len(tree))]
            distance = [0 for _ in range(len(tree))]
            
            if source.key == target.key:
                return distance            
            
            src = (source.key, 0)
            stack.append(src)
            
            while len(stack) > 0:
                val = stack.pop()
                if not discovered[val[0]]:
                    discovered[val[0]] = True
                    distance[val[0]] += val[1]
                    if val[0] == target.key:
                        path = []
                        cost = 0
                        for idx, wt in enumerate(distance):
                            if wt != 0:
                                path.append(find(source, idx, return_values=True))
                                cost += wt
                        
                        path.insert(0, find(source, src[0], return_values=True))    
                        return path, cost
                    
                    for w in tree[val[0]]:
                        if not discovered[w[0]]:
                            stack.append(w)                

        if self.type == 'graph':
            assert isinstance(self.struct, Graph)
            
            discovered = [False for _ in range(len(self.struct.data))]
            parent = [None for _ in range(len(self.struct.data))]
            distance = [float('inf') for _ in range(len(self.struct.data))]
            stack = []

            distance[source] = 0
            stack.append(source)

            while len(stack) > 0 and not discovered[target]:
                current = stack.pop()
                discovered[current] = True

                # update distances
                self.__update_distances(self.struct, current, distance, parent)

                # find the first undiscovered node with the minimum distance
                next_node = self.__pick_next_node(distance, discovered)
                if next_node:
                    stack.append(next_node)

                discovered[current] = True
            
            # Appending Path based on parents array    
            path = []
            temp = target
            while temp is not None:
                path.insert(0, temp)
                temp = parent[temp]
            
            return path, distance[target]    
        
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

    def __pick_next_node(self, distance, visited):
        """Pick the next univisited node at the smallest distance"""
        min_distance = float('inf')
        min_node = None
        for node in range(len(distance)):
            if not visited[node] and distance[node] < min_distance:
                min_node = node
                min_distance = distance[node]
        return min_node
                                  

def djikstra():
    pass


def belman_ford():
    pass


#* === INFORMED SEARCH ALGORITHM === *#
#  -----------------------------------  #
class AStar:
    def __init__(self, heuristic=None):
        pass
