# Search Strategies

> **Author: Satwik Srivastava**
>
> **Profiles:**
>
> - LinkedIn : <https://www.linkedin.com/in/satwiksrivastava/>
> - Twitter : [@Satwik_9](https://twitter.com/Satwik_9)
> - Github : <https://github.com/Satwik-S9>

#### **<u>Release</u>:** `alpha`

<br/>

#### **<u>Version</u>:** `0.45`

<br/>

**Description:** <br/>
In this script I have created all the basic search strategies employed in Artificial Intelligence.
These include but are not limited to the following:

## 1. Table Of Contents

- [Search Strategies](#search-strategies)<br>
      - [**<u>Release</u>:** `alpha`](#ureleaseu-alpha)
      - [**<u>Version</u>:** `0.45`](#uversionu-045)
  - [1. Table Of Contents](#1-table-of-contents)
  - [2. Introduction](#2-introduction)
    - [2.1 Uninformed Search](#21-uninformed-search)
    - [2.2 Informed Search](#22-informed-search)
    - [2.3 Game Search](#23-game-search)
  - [3. Installation and Usage](#3-installation-and-usage)
  - [4. ChangeLog](#4-changelog)
    - [4.1 Version 0.45](#41-version-045)
    - [4.2 Version 0.40](#42-version-040)
    - [4.3 Version 0.38](#43-version-038)
  - [5. Documentation](#5-documentation)
    - [5.1 Tree](#51-tree)
      - [**5.1.1 Binary Tree**](#511-binary-tree)

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

Just [`clone`](#search-strategies) or [`download`](#search-strategies) the _`SearchStrategies.py`_ file and import it as shown below.

```python
import SearchStrategies as ss
print(ss.__version__)
```

This should print the current [version](#uversionu-040) of the module. If not it is either not downloaded or not placed in your working directory.

## 4. ChangeLog

### 4.1 Version 0.45

- Changed the verbose functionality across `BFS` class to introduce more homogeniety between outputs.
- `DFS` Class has been added to the module with the `traverse()` method for both _`trees`_ and _`graphs`_.
- NOTE: The traverse method for tree currently does preorder traversal.
- Fixed some bugs in the implementation of `BFS`.

### 4.2 Version 0.40

 - The `BFS` Class has been added into the module along with relevant supporting data-structures such as `Graph` and `Tree`. This class supports methods for traversal of the data structure and to find the shortest path given a source and a target.

### 4.3 Version 0.38

- Added Basic Data Structures such as `Tree` and `Graphs` and added traversal Methods for the same to the `BFS` Class.

# 5. Documentation

## 5.1 Tree

The Tree Data Structure is a fundamental datastructure for proper and efficient storage and organisation of data.

### 5.1.1 Binary Tree

![Binary Tree](https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_tree.svg)
<br>
Source: [Wikipedia](https://en.wikipedia.org/wiki/Binary_tree)
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
