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
# define the fonts and their weights
fonts:
  # define the font for the body text
  sans: "IBM Plex Sans"
  # define the serif font
  serif: "IBM Plex Serif"
  # define the code font
  mono: "IBM Plex Mono"
  # load several font weights
  weights: "200,400,500"
  # support the use of italics
  italic: true
---

[//]: # (Slide Start {{{)

# Data Abstraction

## Structured Types

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

<br>

<div v-click>

## Key Question

> How can I use Python's structured types (e.g., `str`, `list`, `range`, and
> `dict`) to implement programs that efficiently store and retrieve data?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of data containers so as to
> avoid common pitfalls associated with storing data

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the use of structured types in Python!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the structured types in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Tuple: immutable container for all data types
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
List: mutable container for all data types
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Dict: container storing values associated with keys
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Defining n-Tuples in Python Programs

```python
pair = 3, 4
quadruple = "Story number", 3,
              "is", true

pair = (3, 4)
quadruple = ("Story number", 3,
              "is", true)
```

- The **same data type** is **not** a **requirement** for a tuple

- What are the **data types** of the values in these tuples?

- Which way is the **best** approach to **describing** these tuples?

---

# Special Tuples in the Python Language

```python
empty_tuple = ()
single_story = ("Story",)
single_number = (3,)
number = (3)
```

- Some tuples may not (yet) contain any data in them!

- Singleton tuples must use the comma notation

- What is the **difference** between a **tuple** and a **number**?
  - Conceptual difference
  - Syntactic difference

- How do we **put data into** and **take data out** of a tuple?

---

# Packing and Unpacking Tuples

```python
# pack a tuple into a variable
pair = (3,4)

# unpack the contents of a tuple
x, y = pair
(x, y) = pair

# unpack and perform simultaneous assignment
x, y = y, x
(x, y) = (y, x)
```

<div class="mt-7">

Wait, what is the purpose of the last two statements? 🤔

</div>

---

# Computing Tuple Intersection

```python {all|1-6|7-8|9-10|11-12|all}
def intersect(tuple_one, tuple_two):
    result = ()
    for element in tuple_one:
        if element in tuple_two:
            result += (element,)
    return result
first_tuple = (1, "a", 2)
second_tuple = ("b", 2, "a")
intersection_tuple_one =
            intersect(first_tuple, second_tuple)
intersection_tuple_two =
            intersect(second_tuple, first_tuple)
```

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run this function to understand it better!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the file in <a href = "https://proactiveprogrammers.com/live">Jupyter Lite</a> or
<a href = "https://githubtocolab.com/ProactiveProgrammers/www.proactiveprogrammers.com">Google Colab</a>!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Go to the <code>structured-types</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-structured-types.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the challenges of using lists and tuples?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Understanding data container aliasing
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Determining when containers are equal
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
List append method has side effect
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using List Comprehensions

```python
L = [(x, y)
      for x in range(6) if x % 2 == 0
      for y in range(6) if y % 3 == 0
    ]

print(L)
```

- "Compact" way to define the contents of a list

- Collects the even and odd values from `range(6)`

- Is there another way to write this source code?

- What are the **trade-offs** with list comprehensions?

---

# Alternative to List Comprehensions

```python
L = []
for x in range(6):
    if x % 2 == 0:
        for y in range(6):
            if y % 3 == 0:
                L.append((x, y))
print(L)
```

- Less "compact" way to define the contents of a list

- Which approach is easier to **test** and **maintain**? Why?

- Which approach do you prefer for defining a list? Why?

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's try these list manipulation methods!
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
<code>data-abstraction/structured-types/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-structured-types.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Higher-Order List Operations

```python {all|1-3|5-6|7-8|9-10|11-12|all}
def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

values = [1, -2, 3.33]
print("values =", values)
apply_to_each(values, abs)
print("abs(values) =", values)
apply_to_each(values, int)
print("int(values) =", values)
apply_to_each(values, lambda x: x**2)
print("square(values) =", values)
```

---

# Using the `apply_to_each` Function

<v-clicks>

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5">

<pre>
values = [1, -2, 3.33]
abs(values) = [1, 2, 3.33]
int(values) = [1, 2, 3]
square(values) = [1, 4, 9]
</pre>

</div>

- Each call to `apply_to_each` modifies the list

- This means that the function has a side effect

- Alternative to defining a bespoke function:

    - Python provides a `map` function

    - `map` is more general than `apply_to_each`

    - Both functions implement the same idea!

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run this function to understand it better!
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
<code>data-abstraction/structured-types/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>demonstrate-higher-order-lists.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Summary of These Structured Types

<v-clicks>

- `str` structured type:

  - All elements are characters

  - Examples: `''` or `'a'` or `'abc'`

- `tuple` structured type:

  - Examples: `()` or `(3,)` or `('abc', 4)`

- `list` structured type:

  - Examples: `[]` or `[3]` or `['abc', 4]`

- Both **lists** and **tuples** can store **any type** of data!

- Also possible to create a **range** for storing a **sequence of integers**

</v-clicks>

---

# Sets Store Immutable Elements

```python
x = {53, 'pencil', (1, 1, 2, 3, 5), 3.14159}

print("Set defined with a multiple types:")
print(x)

print()

list = [53, 'pencil', (1, 1, 2, 3, 5), 3.14159]
x = {list}
```

- The last two lines cause this Python program to crash! Why?

- Sets can only store immutable elements, which  `list` is not!

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's learn why these statements crash!
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
<code>data-abstraction/structured-types/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-structured-types.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using Dictionaries in Python

<v-clicks>

-   Python's dictionary is a **fast** way to support data lookup:

    -   Create a mapping between keys and values
    -   Store key-value pairs inside of the structure
    -   You "lookup" the key to "find" the value
    -   Dictionary keys must be an immutable object
    -   The value connected to the key can be of any data type
    -   Integers and strings are common types for the key
    -   Often called hashtables or hashmaps in other languages!

-   What are the **benefits** of dictionaries over lists or tuples?

-   How can you **create** and **use** a **dictionary** in Python?

-   How does a dictionary **internally store** the key-value pairs?

</v-clicks>

---

# Creating and Using Dictionaries

```python
bosco = {}
bosco["Name"] = "Bosco"
bosco["Age"] = 6
bosco["Breed"] = "Havanese"

faith = {}
faith["Name"] = "Faith"
faith["Age"] = 14
faith["Breed"] = "Havanese"
```

- Dictionaries store **key-value pairs**, making an **associative map**

- How can you access a specific **value** stored with a **key** in `bosco` ?

---

# Creating a Dictionary in Python

```python
mlb_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers'
}
```

<v-clicks>

- Reference: <https://realpython.com/python-dicts/>

- The use of `{` and `}` designates a dictionary

- Can you identify the **key** and the **value**?

- How would you lookup a **value** given a **key**?

</v-clicks>

---

# Alternative Way to Create a Dictionary

```python
mlb_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers')
])
```

<v-clicks>

- Here is an alternative way to create key-value pairs!

- Each of the key-value pairs is expressed as a tuple

- The tuples are stored in a list, one tuple for each pairing

- The `dict` constructor accepts a list of tuples!

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's create and use some dictionaries!
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
<code>data-abstraction/structured-types/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-structured-types.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How to decide which structured type to use?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Does the container need to store duplicates?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Should the contents of the container change?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
What performance characteristics are needed?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Investigating Structured Types

<div class = "mt-10">
</div>

<v-clicks>

-   Correct use of structured types in Python programs:

    -   **Q1**: What does it mean if a type is **mutable**?

    -   **Q2**: What does it mean if a type is **immutable**?

    -   **Q3**: How can a **higher-order** function process lists?

    -   **Q4**: What does it mean if a container has an **alias**?

    -   **Q5**: How can you pick the correct container **type**?

-   You will use structured types throughout this course!

-   Balance the **trade-offs** associated with different data containers!

</v-clicks>

[//]: # (Slide End }}})
