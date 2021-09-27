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

# Investigating Structured Types

<div class = "mt-10">
</div>

<v-clicks>

-   Creating Python programs with "good" designs:

    -   **Q1**: What are the benefits of **good design**?

    -   **Q2**: What **language features** support good design?

    -   **Q3**: How does a **higher-order** function improve design?

    -   **Q4**: How does a **lambda** function improve design?

    -   **Q5**: How can we compare the **quality** of two designs?

-   We will always aim to create good designs in **upcoming projects**!

-   Balance the **trade-offs** associated with designing quality software

</v-clicks>

[//]: # (Slide End }}})
