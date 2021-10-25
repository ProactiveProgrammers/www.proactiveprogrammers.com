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

# Discrete Structures

## Set Foundations

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

> How do I use the mathematical concepts of **sets** and **Boolean logic** to
> design Python programs that are easier to implement and understand?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **set**,
> exploring how its use can simplify the implementation of programs

</div>

<v-click>

<div class="flex row mt-3">

<uim-rocket class="text-6xl ml-9 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-8">
Let's investigate the set structure!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

# Mathematical Sets in Python

<v-clicks>

-   Set theory is **important** to many areas of mathematics

-   Concentrate on the set theory useful for programming:

    -   Sets are **containers** for other elements
    -   Sets do **not** contain **duplicate** values
    -   Set elements are **not stored** in a specific order
    -   The **universal** set is the set of all elements
    -   Sets can contain other objects like **sets** and **tuples**
    -   A **subset** of a set contains a portion of the set

-   How do these properties of sets make it easier to implement Python
    programs? How are they different than lists or tuples or generator
    expressions? What are the limitations of sets in Python?

- How do sets differ in **programming** and **mathematics**?

</v-clicks>

---

# Creating a Set from a List

```python
# creat a set out of a list
x = set(['pencil', 'paper', 'pen',
         'pencil', 'wallet', 'pen'])

# display the contents of the set
print("Set defined with a list:")
print(x)
```

<v-click>

- What is the **output** of this program?

- What are the **properties** of a set in Python?

- Can we **implicitly** define the **order** of the set's elements?

</v-click>

---

# Creating a Set from a Tuple

```python
# create a set out of a tuple
x = set(('pencil', 'paper', 'pen',
         'pencil', 'wallet', 'pen'))

# display the contents of the set
print("Set defined with a tuple:")
print(x)
```

<v-click>

- What is the **output** of this program?

- Does the use of a set or a tuple **influence** the container?

- What **types** of elements can we store in a set?

</v-click>

---

# Output of a Program that Creates Sets

```python
# Output from a set defined with a list:
  {'paper', 'pencil', 'pen', 'wallet'}

# Output from a set defined with a tuple:
  {'paper', 'pencil', 'pen', 'wallet'}
```

<v-click>

- The sets do not store duplicate values

- Creation from either a set or a tuple is the same

- The contents of a set are displayed in arbitrary order

- Note the use of `{` and `}` for start and end of a set

- Any questions about the basics associated with sets?

</v-click>

---

# Python's Sets Store Immutable Content

```python
x = {53, 'pencil',
     (1, 1, 2, 3, 5), 3.14159}

print("Set with multiple types:")
print(x)
```

<v-click>

- Note the **explicit** approach to set creation

- The data types in this set are **different**

- All of the variables in this set are **immutable**

- How will this program **display** the elements of the set?

- Note that Python **can** store a **tuple** in a set!

</v-click>

---

# Sets Cannot Store Mutable Containers

```python
list = [53, 'pencil',
        (1, 1, 2, 3, 5), 3.14159]
x = {list}
```

<div class="mt-8">

```python
Traceback (most recent call last):
  File "set-element-types.py", line 11,
       in <module>
    x = {list}
TypeError: unhashable type: 'list'
```

</div>

- Explicit construction of the set crashes due to `list`

- How is this different than using `set` constructor function?

---

# Sets with Mathematical Notation

<v-clicks>

-   Explicit definition of a set: $S = \{1, 2, 3\}$

-   Definition of a set with a property:\
    $\{ n \; | \; 0 < n < 100
          \;\land\; n \;\%\; 2 = 0 \}$

-   $\mathbb{N}$ is the set of natural numbers

-   $\mathbb{Z}$ is the set of integer numbers

-   $\mathbb{R}$ is the set of real numbers

-   $\mathbb{C}$ is the set of complex numbers

-   You can also define sets by using different set **operators**!

-   Any questions about these examples of a set definition?

</v-clicks>

---

# Mathematical Operations with Sets

<v-clicks>

-   Set membership: $S = \{1, 2, 3\}$ such that $1 \in S$ and
    $5 \notin S$

-   Proper subset: $S = \{1, 2, 3\}$ and thus $\{1\} \subset S$

-   Subset: $S = \{1, 2, 3\}$ and thus $\{1\} \subseteq S$ and
    $\{1, 2, 3\} \subseteq S$

-   Set union: $S_1 \cup S_2$ contains elements in either $S_1$ or $S_2$

-   Set intersection: $S_1 \cap S_2$ is the elements in both $S_1$ and
    $S_2$

-   Set difference: $S_1 - S_2$ is the elements in $S_1$ but not in
    $S_2$

-   Union and intersection are **associative** and **commutative**!

-   Any questions about these operations for the set?

</v-clicks>

---

# Math and Programming Differences

<v-clicks>

-   Programmers **cannot** use sets like mathematicians do!

-   Python programs **cannot** store an infinite set

-   Finite sets must **fit** into a computer's **finite** memory

-   Programs need a **procedure** for **constructing** the set

-   Different programming languages and packages have other
    restrictions. For instance, recall that Python programs cannot
    create sets that contain mutable elements like lists! Why do you think that
    this is the case?

-   So, what are the benefits of using sets in Python programs?

-   Importantly, sets come with some **super-useful** default operations!

-   Any questions about sets in mathematics or programming?

</v-clicks>
