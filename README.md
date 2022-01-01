# Search Strategies

> **Author: Satwik Srivastava**
>
> **Profiles:**
>
> - LinkedIn : <https://www.linkedin.com/in/satwiksrivastava/>
> - Twitter : [@Satwik_9](https://twitter.com/Satwik_9)
> - Github : <https://github.com/Satwik-S9>

#### **<u>Release</u>:** `alpha-stable`

<br/>

#### **<u>Version</u>:** `0.50`

<br/>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Satwik-S9/Search-Strategies/master)

**Description:** <br/>
In this script I have created all the basic search strategies employed in Artificial Intelligence.
These include but are not limited to the following:

1. Uninformed Search Strategies:   
   1. BFS
   2. DFS
   3. Uniform Cost Search
2. Informed Search Strategies:
   1. A Star Search 
3. Game Search Strategies: 
   1. Alpha-Beta Search
4. Backtracking Search

## 1. Table Of Contents

- [Search Strategies](#search-strategies)
      - [**<u>Release</u>:** `alpha-stable`](#ureleaseu-alpha-stable)
      - [**<u>Version</u>:** `0.50`](#uversionu-050)
  - [1. Table Of Contents](#1-table-of-contents)
  - [2. Introduction](#2-introduction)
    - [2.1 Uninformed Search](#21-uninformed-search)
    - [2.2 Informed Search](#22-informed-search)
    - [2.3 Game Search](#23-game-search)
  - [3. Installation and Usage](#3-installation-and-usage)
  - [4. ChangeLog](#4-changelog)
    - [4.1 Version 0.50](#41-version-050)
    - [4.2 Version 0.49](#42-version-049)
    - [4.3 Version 0.45](#43-version-045)
    - [4.4 Version 0.40](#44-version-040)
    - [4.4 Version 0.38](#44-version-038)
- [5. Documentation](#5-documentation)
  - [5.1 Tree](#51-tree)
    - [5.1.1 Binary Tree](#511-binary-tree)
- [6. Further Plans](#6-further-plans)

## 2. Introduction

### 2.1 Uninformed Search

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Uniform Cost Search

### 2.2 Informed Search

1. A Star Search

### 2.3 Game Search

1. Alpha-Beta Search

All These algorithms are implemented on the tree and the graph data-structures and are used to solve the shortest path problem.

## 3. Installation and Usage

!NOTE! : Currently I have not packaged this as a module so you have to clone it directly into your working directory.

Just [`clone`](#search-strategies) or [`download`](https://github.com/Satwik-S9/Search-Strategies/archive/refs/heads/master.zip) the _`SearchStrategies.py`_ file and import it as shown below.

```python
import SearchStrategies as ss
print(ss.__version__)
```

This should print the current [version](#uversionu-040) of the module. If not it is either not downloaded or not placed in your working directory.

## 4. ChangeLog

### 4.1 Version 0.50

- `BFS` and `DFS` classes are now fully available and all the methods required are now completed. Some handy functions have been added too.
- The `find` function is added to find a value in a Binary Tree.
- Added `create_adjacency_list` for trees to convert them into graphs for interoperability.
- All shortest path methods are now available and return `path, cost` as there return parameters and across the board a little homogeniety has been introduced. 

### 4.2 Version 0.49

- Added `create_adjacency_list` for trees to convert them into graphs for interoperability.
- Creating a tree can now initialize the keys and the parents (uses `initialize_parents` and `initialize_keys`)
- The `DFS` class now supports the shortest path calculation for trees.

### 4.3 Version 0.45

- Changed the verbose functionality across `BFS` class to introduce more homogeniety between outputs.
- `DFS` Class has been added to the module with the `traverse()` method for both _`trees`_ and _`graphs`_.
- NOTE: The traverse method for tree currently does preorder traversal.
- Fixed some bugs in the implementation of `BFS`.

### 4.4 Version 0.40

- The `BFS` Class has been added into the module along with relevant supporting data-structures such as `Graph` and `Tree`. This class supports methods for traversal of the data structure and to find the shortest path given a source and a target.

### 4.4 Version 0.38

- Added Basic Data Structures such as `Tree` and `Graphs` and added traversal Methods for the same to the `BFS` Class.

# 5. Documentation

## 5.1 Tree

The Tree Data Structure is a fundamental datastructure for proper and efficient storage and organisation of data.

### 5.1.1 Binary Tree

![Binary Tree](https://www.geeksforgeeks.org/wp-content/uploads/binary-tree-to-DLL.png)
<br>
Source: [GeeksForGeeks](https://www.geeksforgeeks.org/binary-tree-data-structure/)
<br>
A binary tree is a data-structure that in which each node has atmost two children. It can be represented as [`tuple`]() (L, S, R)
The binary tree can be created using this module as follows:

```python
import SearchStrategies as ss

root_single = ss.TreeNode(4)
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

root = ss.create_tree(tree_tuple)
```

**NOTE:** Currently Working on Documentation. Please refer to the `test.ipynb` for an onhande demo.

# 6. Further Plans

1. Package the file into a python Module.
2. Add BSTs to the project.
3. Add Informed Search Strategies such as `Astar` search.