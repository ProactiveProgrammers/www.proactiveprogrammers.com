---
# try also 'default' to start simple
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: prism
colorSchema: light
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
---

[//]: # (Slide Start {{{)

# Data Abstraction

## Data Structures

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
    @apply text-orange-600 mb-4;
  }
</style>

<div v-click>

## Key Question

> How can I implement, use, and test data structures that support efficient data
> processing with searching and sorting algorithms?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the characteristics of key data structures
> (e.g., a list and a hash table) so that they can serve as the input and output
> for searching and sorting algorithms?

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the topic of data structures!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are some common data structures?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Dynamic arrays that grow (and shrink) in size
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Linked lists that are comprised of nodes and edges
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Hash tables that employ a function and backing list
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Common algorithms for data processing?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Searching algorithms look for data in container
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Sorting algorithms reorder the container's data
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Combine in unique ways to solve novel problems
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<style>
  li {
  font-size: 34px;
  margin-bottom: 1px;
  }
</style>

<div class="flex row">

<uim-vector-square class="text-8xl ml-4 mt-12 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-5">
Data structures
</div>

<div class="text-6xl text-true-gray-600 font-bold mt-16 mr-15">
<ul>
<li>Array</li>
<li>Lists</li>
<li>Dictionary</li>
</ul>
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-flip-v class="text-9xl ml-4 mt-6 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-5">
Processing algorithms
</div>

<div class="text-8xl text-true-gray-600 font-bold -ml-25 mt-16 mr-15">
<ul>
<li>Searching</li>
<li>Sorting</li>
<li>Combine</li>
</ul>
</div>

</div>

</v-clicks>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-5 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Connecting data containers and data processing?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exhaustive Enumeration and Search

<v-clicks>

- Many computations require a **specific value** in order to proceed

- The **exhaustive enumeration** approach "naively" looks through **all
possibilities** until it finds the correct solution

- How does exhaustive enumeration work?
    - List all possible values for a computation
    - Check to see if the current value is correct
    - If not correct, try the next value in the list
    - Continue until the correct value is found

- Easy to implement and understand. Often fast enough for practical purposes!

- Very useful to **start** with exhaustive approaches while proving a concept

- When is it **not efficient** enough to perform exhaustive enumeration? **Big
data!**

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Lifecycle for Algorithms and Data

<v-clicks>

- Quickly implement an algorithm to investigate a hypothesis

- If data and approach look promising, optimize the system further:

    - **Explore** different data containers
    - **Investigate** different algorithms
    - **Combine** searching, sorting, and containers

- Reduce complex problems to aspects of known problems:

    - **Understand**: grasp the inherent complexity of the problem
    - **Decompose**: break the problem into subproblems
    - **Connect**: relate the subproblems and find algorithms

- Make sure to consider the following trade-offs during lifecycle: is the
approach efficient? Is the approach easy to implement, test, and maintain?
Trade-offs?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Linear Search with Indirection

```python
for i in range(len(L)):
    if L[i] == e:
      return True
return false
```

<v-clicks>

- Containment checking for a list `L` uses a `for` loop and is thus $O(n)$

- Of course, it is only linear if each operation in the loop is $O(1)$!

- Consider the cost of running `L[i]` and comparing to `e`

- Python implements **list indexing** through **pointers** and **indirection**

- Indexing can start at the **beginning** of the list and use **pointer arithmetic**

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What if we can assume that the list is sorted?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Ensure that the elements of list are sorted
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Assume that sort occurs for ascending order
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Does it have a better worst-case time complexity?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Recursive Binary Search Algorithm

<v-clicks>

- Improve the worst-case time complexity by applying a **binary search**

- Leverages the ideas that we developed for the **bisection search**

- Steps for performing a **recursive binary search**:

    - Assume that you are searching list `L` for element `e`

    - Pick an index `i` that roughly divides the list `L` in half

    - Determine if `L[i] == e` and return the element `e` if it is

    - If not found `e` then determine if `L[i]` is smaller or bigger than `e`

    - Depending on the answer, search the left or right half of `L` for `e`

- Continue this process recursively until found or searched entire list!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is performance of binary search method?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Remember, assumes that the input list <code>L</code> is sorted!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>math.log(x, base)</code> is key to time complexity
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
The tight bound on the time complexity is log(len(L))
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Sorting Algorithms in Python

<v-clicks>

- Is it **better** to sort and then search? Can that be **faster** that a clever sort?

- Well, may be possible to **amortize** the cost of sorting for many searches!

- With that said, it is **not** possible to sort with a **sub-linear** time complexity!

- Understanding sorting algorithms available or implemented in Python:

    - **Selection sort** operates in $\theta(n^2)$ and is thus **quadratic**

    - **Merge sort** operates in $\theta(n\times\log(n))$ and is thus **linearithmic**

    - Both of these algorithms have time complexities with $n = len(L)$

    - **Timsort** takes advantage of the fact that lists are often partially sorted

    - It has the same worst-case performance but is **better** in the **average case**!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Practical sorting methods for Python?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Built-in <code>list.sort()</code> that modifies list in-place
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
The <code>sorted</code> function can sort any <code>Iterable</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Methods are stable and thus guarantee orderings
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

# Combining Searching and Sorting

<v-clicks>

- What happens if we combine merge sort with a recursive binary search?

  - Merge sort can pre-process the list in $O(n \times log(n))$
  - Binary search can determine an element is in a list at $O(log(n))$
  - When combining two separate algorithms the time complexity is additive
  - So, the overall time complexity of the hybrid algorithm is $O(n \times log(n) + k \times log(n))$
  - This time complexity assumes that you will perform $k$ searches on the sorted list

- Is this the best that we can do for searching? Can we build a better approach?

- What are the requirements for an approach that is better than this one?

    - Avoid the pre-processing step that requires the sorting of a list before searching
    - Searching algorithm that provides either a constant or logarithmic time complexity
    - It is possible to achieve these goals with either trees or hash tables
    - This courses focuses on the hash table because it is likely the fastest!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is the basic idea behind hash tables?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Store key-value pairs inside of a backing list
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Lookup a value based on the provided key
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Hashing function maps the key to value's location
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Fundamentals of Hash Tables

<v-clicks>

- What are the basics of hashing functions?

  - Convert a large space of **keys** to a smaller space of **indices**

  - Implement a **many-to-one** mapping while avoiding collisions

  - Aim to **distribute** the values of keys **uniformly** across the backing list

- How to handle collisions inside of the hash table?

    - Store a list at each index of the backing list

    - When a collision occurs, store next value inside of the list

    - When searching with a key that has collided, linearly search internal list

    - Avoid collisions because they degrade the $O(1)$ lookup cost!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about hash table trade-offs?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alpha-t-box class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Large backing list avoids collisions, takes up space
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alpha-t-box class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Small backing list causes collisions, saves space
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alpha-t-box class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Hashing functions save time/space, hard to design
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Reviewing Data Structures

<v-clicks>

- Picking the correct data structure and algorithm is challenging:

    - Think carefully about your functionality and performance goals
    - Try to combine different data structures to create a hybrid solution
    - Consider ways in which you can effectively trade-off time and space

-   Questions to consider about data structures in Python:

    -   **Q1**: What are the **benefits** of sorting before searching?

    -   **Q2**: What are the fundamental **limitations** of sorting?

    -   **Q3**: How do you conduct a **doubling experiment** to study performance?

    -   **Q4**: How does the built-in **timsort** achieve performance gains?

    -   **Q5**: How can good **hashing functions** avoid collisions in backing list?

</v-clicks>

[//]: # (Slide End }}})
