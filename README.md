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

#### **<u>Version</u>:** `0.40`

<br/>

**Description:** <br/>
In this script I have created all the basic search strategies employed in Artificial Intelligence.
These include but are not limited to the following:

## Table Of Contents


  - [**<u>Release</u>:** `alpha`](#ureleaseu-alpha)
  - [**<u>Version</u>:** `0.40`](#uversionu-040)
  - [Table Of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Uninformed Search](#uninformed-search)
    - [Informed Search](#informed-search)
    - [Game Search](#game-search)
  - [Installation and Usage](#installation-and-usage)
  - [ChangeLog](#changelog)
    - [Version 0.40](#version-040)
  - [Documentation](#documentation)

## Introduction

### Uninformed Search

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Uniform Cost Search

### Informed Search

1. A Star Search

### Game Search

1. Alpha-Beta Search

All These algorithms are implemented on the tree and the graph data-structures and are used to solve the shortest path problem.

## Installation and Usage

!NOTE! : Currently I have not packaged this as a module so you have to clone it directly into your working directory.

Just [`clone`](#search-strategies) or [`download`](#search-strategies) the _`SearchStrategies.py`_ file and import it as shown below.

```python
import SearchStrategies as ss
print(ss.__version__)
```

This should print the current [version](#uversionu-040) of the module. If not it is either not downloaded or not placed in your working directory.

## ChangeLog

### Version 0.40
The `BFS` Class has been added into the module along with relevant supporting data-structures such as `Graph` and `Tree`. This class supports methods for traversal of the data structure and to find the shortest path given a source and a target.

### Version 0.38
Added Basic Data Structures such as `Tree` and `Graphs` and added traversal Methods for the same to the `BFS` Class.

## Documentation
