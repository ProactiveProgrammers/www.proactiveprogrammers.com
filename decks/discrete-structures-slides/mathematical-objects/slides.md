---
# try also 'default' to start simple
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: prism
colorSchema: light
remoteAssets: false
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
---

[//]: # (Slide Start {{{)

# Discrete Structures

## Mathematical Objects

<div class="container my-5">
  &nbsp;
</div>

### Gregory M. Kapfhammer

### www.proactiveprogrammers.com

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# <em>Okay</em>, what is this about?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-2;
  }
</style>

<br>

<div v-click>

## Key Question

> How do I use the concepts associated with object-oriented programming to
> create and use objects for the purposes of performing mathematical
>  computations like the moving average?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **objects**
> and to learn different ways to use them in mathematical computations

</div>

<v-click>

<div class="flex row mt-0 ml-0">

<uim-rocket class="text-6xl ml-5 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-10">
Let's create objects to aid mathematics!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Foundations of object-oriented programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-package class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Classes are templates for objects
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-package class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Objects contain state in variables
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-package class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Objects feature behavior with methods
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Inheritance and Encapsulation

<v-clicks>

- Inheritance enables creation of **parent-child** relationships

- Inheritance forms an **"is a"** relationship between two classes

- Benefits of inheritance in object-oriented programming:

    - Define **specialized behaviors** in the sub-classes

    - Promote **code reuse** since child can access parent's methods

    - Promote **data sharing** since child can access parent's variables

    - Model object-oriented relationships that **mirror reality**

- Encapsulation **protects** the **state** of an object, well sorta 😉

- What are the **benefits** and **drawbacks** of object-oriented programming?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Benefits of inheritance and encapsulation?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Inheritance supports code reuse and data sharing
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Inheritance allows modelling of real-world entities
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Encapsulation calls for state change with methods
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Methods in object-oriented programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Methods define a behavior for instances of class
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Methods accept input and produce output
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
The <code>self</code> parameter is always a method's input
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Key benefits of object-oriented programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Combines behavior with the storage of state
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports the modelling of real-world entities
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
But, it sometimes feels more "complex" in Python!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Case Study: Moving Average of Values

<v-clicks>

- Many streaming systems produce a never-ending sequence of values

- **Challenge**: how to average these values in space-efficient fashion?

- Approach to computing the **moving average** of a list of values:

    - Define the `__init__` method as the constructor

    - Define the `append` method to add data to `MovingAverage`

    - Define the `value` method to compute a running total

    - Define a `smooth` function for a `window` of data

- **Question**: what are the trade-offs associated with `window` ?

- What are the **benefits** and **drawbacks** of this mathematical object?

</v-clicks>

[//]: # (Slide End }}})

---

# Define the `MovingAverage` Class

```python
class MovingAverage:

    def __init__(self, num_points):
        self.__points = []
        self.__length = 0
        self.__num_points = num_points
```

<v-clicks>

- The `__init__` method defines the constructor for the class

- The `MovingAverage` will keep track of a total of `num_points`

- The `__points` list will actually contain the tracked values

- Let's add the other methods to the `MovingAverage` !

</v-clicks>

---

# Define the `append` Method

```python
def append(self, new_value):
    points = self.__points
    if self.__length == self.__num_points:
        points.pop(0)
    else:
        self.__length += 1
    points.append(new_value)
```

<v-clicks>

- Responsible for storing the `new_value` inside of `points`

- Must ensure that no more than `__num_points` values are stored

- Uses the `pop` method for a list to remove value at the list's start

</v-clicks>

---

# Define the `value` Method

```python
def value(self):
    points = self.__points
    length = self.__length
    if length > 0:
        return sum(points) / length
    return None
```

<v-clicks>

- The `self` parameter provides access to the current object

- Must compute the current moving average of the data values

- As long as data is available, compute the arithmetic mean

- If no data is available, then return the value of `None`

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's use objects for a moving average!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Visit the <a href = "https://proactiveprogrammers.com/live">Proactive Programmers Live</a> site!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the <code>mathematical-objects/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-mathematical-objects.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the properties of the tree structure?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-content-copy class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Hierarchical (i.e., non-linear) in their structure
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-content-copy class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Support the traversal of nodes to collect data
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-content-copy class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Ordered nodes enable fast searching for data
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Case Study: Recursively Defined Trees

<v-clicks>

- Create a `Node` object that will connect to two other `Node` s

- When two `Node` objects are connected, we say that they share an edge

- Require the tree to have a root (or starting point) with no edges leading to it

- Require that all other `Node` s in the tree have only one edge leading to it

- Recursively traverse the contents of a `Tree`:

    - **In-order Traversal**: Left, Node, Right

    - **Pre-order Traversal**: Node, Left, Right

    - **Post-order Traversal**: Left, Right, Node

- What are the **benefits** and **drawbacks** of using the `Tree`  structure?

</v-clicks>

[//]: # (Slide End }}})

---

# Define the Constructors for a `Tree`

```python
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
```

<v-clicks>

- The `Node` is the building block for the recursively defined `Tree`

- An `insert` method will call `createNode` to build up a `Tree`

</v-clicks>

---

# Define the `insert` Method for a `Tree`

```python
def insert(self, node, data):
    if node is None:
        return self.createNode(data)
    if data < node.data:
        node.left = self.insert(node.left, data)
    elif data > node.data:
        node.right = self.insert(node.right, data)
    return node
```

<div class="mt-10">

<v-clicks>

- The `node` parameter is the "starting point" for the new `data` value

- Organizes the data in the `Tree` instance so that there is a searchable order

</v-clicks>

</div>

---

# Create a `search` Method for a `Tree`

```python
def search(self, node, data):
  if node is None or node.data == data:
      return node
  if node.data > data:
      return self.search(node.right, data)
  else:
      return self.search(node.left, data)
```

<div class="mt-5">

<v-clicks>

- The `node` parameter is the "starting point" for the search for `data`

- Recursively search "to the left" or "to the right" depending on `data`

- What are the performance characteristics of the `search` method?

</v-clicks>

</div>

---

# Perform an In-order Traversal of a `Tree`

```python
def traverseInorder(self, root):
    if root is not None:
        self.traverseInorder(root.left)
        print(root.data)
        self.traverseInorder(root.right)
```

<div class="mt-10">

<v-clicks>

- Perform the traversal in the order of "**left**, **node**, **right**"

- The `root` parameter defines where the traversal starts

- Traversal occurs through recursive calls to the `traverseInorder`

- What is the output of in-order traversal for the provided sample tree?

</v-clicks>

</div>

---

# Perform an Pre-order Traversal of a `Tree`

```python
def traversePreorder(self, root):
    if root is not None:
        print (root.data)
        self.traversePreorder(root.left)
        self.traversePreorder(root.right)
```

<div class="mt-10">

<v-clicks>

- Perform the traversal in the order of "**node**, **left**, **right**"

- The `root` parameter defines where the traversal starts

- Traversal occurs through recursive calls to the `traversePreorder`

- What is the output of in-order traversal for the provided sample tree?

</v-clicks>

</div>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's use objects to traverse & search trees!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Visit the <a href = "https://proactiveprogrammers.com/live">Proactive Programmers Live</a> site!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the <code>mathematical-objects/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-tree-structures.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

