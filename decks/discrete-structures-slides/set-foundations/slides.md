---
# use the default theme
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# define the highlighter and the colorSchema
highlighter: prism
colorSchema: light
remoteAssets: false
# show line numbers in code blocks
lineNumbers: false
# define the fonts
fonts:
  # define the font for the body text
  sans: 'IBM Plex Sans'
  # define the serif font
  serif: 'IBM Plex Serif'
  # define the code font
  mono: 'IBM Plex Mono'
  # load several font weights
  weights: '200,400,500'
  # support the use of italics
  italic: true
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
# create a set out of a list
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

<v-click>

- Explicit construction of the set crashes due to `list`

- How is this different than using `set` constructor function?

</v-click>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run this code to understand it better!
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
<code>discrete-structures/set-foundations/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run+Study <code>explore-set-foundations.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

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

-   Different programming languages and packages have other restrictions. For
instance, recall that Python programs **cannot** create sets that **contain
mutable elements** like lists! Why do you think that this is the case?

-   So, what are the **benefits** of using sets in Python programs?

-   Importantly, sets come with some **super-useful** default operations!

-   Any questions about sets in mathematics or programming?

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about the set in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Sets do not contain duplicate values
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Sets can only contain data that is hashable
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Sets have practical limitations due to constraints
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using the Set Union Operator in Python

```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
print(a.union(b, c, d))
print(a | b | c | d)
```

<v-click>

- Sets in Python provide useful operations like `union` !

- The `union` method is invoked for a specific set `a`

- The `union` method accepts multiple sets like `b` and `c`

- What do you think is the output of the `print` statements?

</v-click>

---

# Using the Set Intersection Operator

<v-click>

```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
print(a.intersection(b, c, d))
print(a & b & c & d)
```

</v-click>

<v-click>

- Sets in Python provide useful operations like `intersection` !

- The `intersection` method is invoked for a specific set `a`

- The `intersection` method accepts multiple sets like `b` and `c`

- What do you think is the output of the `print` statements?

</v-click>

---

# Using the Set Difference Operator

<v-click>

```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
print(a.difference(b, c))
print(a - b - c)
```

</v-click>

<v-click>

- Sets in Python provide useful operations like `difference` !

- The `difference` method is invoked for a specific set `a`

- The `difference` method accepts multiple sets like `b` and `c`

- What do you think is the output of the `print` statements?

</v-click>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run the set operations source code!
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
<code>discrete-structures/set-foundations/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run+Study <code>explore-set-foundations.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Output of the Set Operators in Python

```
Union of the sets:
  {1, 2, 3, 4, 5, 6, 7}
  {1, 2, 3, 4, 5, 6, 7}

Intersection of the sets:
  {4}
  {4}

Difference of the sets:
  {1}
  {1}
```

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about set operations?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Operations are part of the default implementation
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Intersection finds what sets have in common
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Difference subtracts content of set from another
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Set Comprehensions: Odd Positives

```python
odd_positives = {n for n in range(100)
                 if n % 2 == 1}

for odd_positive in odd_positives:
    print(odd_positive)

print((odd_positives)
```

<v-click>

- Modular arithmetic helps us determine when a number is odd

- `odd_positives` is a set comprehension for odd positive numbers

- How is this similar to and different from one for `list` or `tuple` ?

</v-click>

---

# Set Comprehensions: Even Positives

<v-click>

```python
even_positives = {n for n in range(100)
                  if n % 2 == 0}

for even_positive in even_positives:
    print(even_positive)

print(even_positives)
```

</v-click>

<v-click>

- Modular arithmetic helps us determine when a number is even

- `even_positives` is a set comprehension for odd positive numbers

- How is this different than the `odd_positives` comprehension?

</v-click>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run code with set comprehensions!
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
<code>discrete-structures/set-foundations/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run+Study <code>explore-set-foundations.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of using the set structure?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Storing unique items may reduce storage needs
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Sets support fast containment checking for value
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Sets provide many useful built-in operations
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Practical Applications of Sets?

<v-clicks>

-   Programs frequently need to **input data** and **save** it in memory

-   The programs then take data from memory and **save** it to disk

-   Storing data in a set **supports computations** like the following:

    -   Determining the similarities and differences between organisms

    -   Finding similarities in purchases between different people

    -   Identifying evidence of plagiarism between written documents

    -   Recommendations about new music to which you should listen

    -   Suggestions for new items to purchase based on prior purchases

-  How would you use a set to implement one of the previous applications?

</v-clicks>

---

# Boolean Logic and Sets: Logical Or

```python
odd_positives_two =
        {n for n in range(20)
         if n % 2 == 1 or n == 2}

for value in odd_positives_two:
    print(value)

print(odd_positives_two)
```

<v-click>

<div class="mt-10">

- Logical `or` is `True` when either clause is `True`

- What outputs will the `print` statements produce?

</div>

</v-click>

---

# Program Output from Use of Logical Or

```
1
2
3
5
<...>
19

[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

<v-click>

<div class="mt-10">

- Note that the use of `<...>` elides extra output that could not fit on slide

- Why is the `print` output format differently for same set comprehension?

</div>

</v-click>

---

# Boolean Logic and Sets: Logical And

```python
even_positives_by_four =
     {n for n in range(20)
      if n % 2 == 0 and n % 4 == 0}

for value in even_positives_by_four:
    print(value)

print(even_positives_by_four)
```

<v-click>

<div class="mt-10">

- Logical `and` is `True` when both clauses are `True`

- What outputs will the `print` statements produce?

</div>

</v-click>

---

# Program Output From Logical And

```
0
4
8
12
16

[0, 4, 8, 12, 16]
```

<v-click>

<div class="mt-8">

- Both of the conditions must be true for the logical `and` operator!

- Why do different approaches with `print` make different output?

- How are logical `and` and `or` similar and different?

</div>

</v-click>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's create sets using Boolean logic!
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
<code>discrete-structures/set-foundations/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run+Study <code>explore-set-foundations.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about Boolean logic?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Operators are a part of the Python language
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Boolean logic useful when manipulating sets
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Boolean logic helps conditional statements
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using Sets in Python Programs

<v-clicks>

-   Sets are a discrete structure with many **practical benefits**!

-   Sets have **built-in operations** that make programming easy

-   Using **sets** and **Boolean logic** in Python programs:

    -   **Q1**: What are the characteristics of a set?

    -   **Q2**: What are the built-in operations provided by a set?

    -   **Q3**: How can you connect sets in math and programming?

    -   **Q4**: How does Boolean logic help us describe a set?

    -   **Q5**: How does the `sympy` package support set programming?

-   Refer to <https://realpython.com/python-sets/> for more details about sets!

</v-clicks>
