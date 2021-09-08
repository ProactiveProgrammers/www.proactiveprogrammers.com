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

## Making Connections

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

> How do I connect **mathematical terminology**  (e.g., *mapping*, *function*,
> *number*, *sequence*, and *set*), to the implementation of **Python
> programs** that declare and call functions and declare and manipulate
> variables?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some discrete mathematics and Python
> programming concepts, setting the stage for exploring of discrete structures.

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Discrete Structures = Math + Code

<v-clicks>

-   **Discrete mathematics**: symbols, character strings, truth values,
objects, and collections of these entities stored in, for instance, sets or
tuples

-   Specifying and designing a **computer program**:

    -   Describe input, output, and internal objects
    -   Use the vocabulary of discrete mathematics
    -   Implement and test the program in a language

- **Our goal**: implement a program $P$ that meets a specification $S$

</v-clicks>

<div v-click>

<div class="flex row -mt-5">

<mdi-help-box class="text-9xl ml-8 mt-4 text-blue-600" />

<div class="text-4xl font-bold mt-13 ml-4">
What is beneficial about combining mathematics and computer programming?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Program that Analyzes Web Pages

-   **Informal specification**: Read two web pages and then find and output
    all of the URLs that appear in them both

-   Different approaches to implementing this program

    -   **Informal** and **intuitive** specification

    -   **Natural language specification** using **discrete structures**

    -   Which one is shorter? \... clearer? \... unambiguous?

-   The language of mathematics helps us to describe and implement a program
that is correct, efficient, clearly documented, and maintainable!

<div v-click>

<div class="flex row -mt-4">

<mdi-help-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="text-4xl font-bold mt-7 ml-4">
What is challenging about this specification?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is difficult about discrete structures?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
What is the meaning of the term <code>set</code> ?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
How do you perform <code>set insertion</code> ?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
How do you perform <code>set intersection</code> ?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Programs and Discrete Structures

<v-clicks>

-  **Our goal**: Jump to different levels of abstraction (e.g., high-level
versus low-level or mathematical versus technical) when we create programs

-   What *is* a computer program?

    -   Informal or intuitive specification
    -   Precise discrete mathematical specification
    -   Realization of a specification in Python program
    -   Bits packaged into bytes and words stored on a disk
    -   A process in execution on a CPU and stored in memory

-   It is "natural" (and fun!) to jump from a discrete mathematical
    specification to a Python program and then back to the specification again

- Pick the suitable level of abstraction for the problem you solve!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Discrete Structures with Python

-   Discrete structures support **precise programming**

-   Benefits of using Python to explore discrete structures

    -   Modern language with exceptional **package support**

    -   Clean **syntax** and **semantics** that is easy to learn

    -   **Out-of-the-box support** for many **discrete structures**

    - Language's semantics match those of discrete structures'

-   Download Python and start programming by visiting
    <https://www.python.org/>

<div v-click>

<div class="flex row -mt-2">

<mdi-help-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="text-4xl font-bold mt-7 ml-4">
What are the benefits of using Python?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Why focus on Python programming?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-4;
  }
</style>

<br>

<div v-click>

## Prevalence of Python

> Python is consistently ranked as one of the **top programming languages**
> for web development, data science, machine learning, and general programming

</div>

<br>

<div v-click>

## Programming Opportunities

> Programmers who use Python can use Jupyter notebooks or build command-line
> applications for tools or servers, supporting wide variety of tasks

</div>

<div v-click>

<div class="flex row">

<mdi-help-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
What is exciting about programming in Python?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is great about programming in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Typer: <code>https://typer.tiangolo.com/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-layer-group class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Poetry: <code>https://python-poetry.org/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-grid class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
There are many other great packages and tools!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="ml-8 grid grid-cols-2 gap-19">
<div>

# Typer

<style>
  li {
  font-size: 22px;
  margin-bottom: 10px;
  }
</style>

- *Annotations* : assign types to functions accepting arguments
- *Productivity* : types aid in the creation of the interface
- *Checking* : confirm that inputs match expected types

</div>

<div v-click>

<div>

# Poetry

- *Environments* : manage dependencies in isolation
- *Package* : create a stand-alone executable application
- *Publish* : expedite and simplify the release of program to PyPI

</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-scenery class="text-6xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
New way to manage application dependencies
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-grid class="text-6xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
Adjust to the challenge of adding type annotations
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<uim-repeat class="text-8xl ml-9 mt-8 text-orange-600" />

<div class="text-6xl text-true-gray-600 font-bold mt-8 ml-4">
Easy command-line interface with Typer
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-layer-group class="text-8xl ml-9 mt-8 text-orange-600" />

<div class="text-6xl text-true-gray-600 font-bold mt-8 ml-4">
Manage, package, and release with Poetry
</div>

</div>

<div class="flex row">

<mdi-help-box class="text-8xl ml-9 mt-8 text-blue-600" />

<div class="text-5xl text-true-gray-700 font-bold mt-15 ml-4">
What are Python's features?
</div>

</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# A First Look at the Python Language

<v-clicks>

- Python is a general purpose programming language with support for **variables**,
**conditional logic**, **iteration**, **recursion**, **functions**, and **classes**!

- How can we describe the Python language?
    - High-level language
    - Scripting language
    - Object-oriented language
    - Functional programming language
    - Procedural programming language
    - "Second best" programming language

- VSCode provides support for Python through **syntax highlighting**, **source code
formatting**, **linting**, **testing**, ... and many more tasks!

- What are some of the **tools** that provide the features highlighted in bold?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Python Programming Constructs

- Intuitively read the code segments to grasp their behavior

- Key components of the Python programming segments

    -   Function calls
    -   Assignment statements
    -   Iteration constructs
    -   Conditional logic
    -   Variable creation
    -   Variable computations
    -   Variable output

- Make sure that you can find all of these components in Python source code!

<div class="flex row">

<mdi-code-braces-box class="text-6xl ml-9 mt-0 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-4 ml-4">
Let's study some source code examples!
</div>

</div>

[//]: # (Slide End }}})

---

# Using Python to Find a Name in a File

```python {all|1|2|3-4|all}
file = open("names")
for line in file:
  if line.startswith("John")
    print(line)
```

<v-clicks>

- Can you explain the behavior of this program segment?

- What are the constructs inside of this program segment?

- How is this different than a full-fledged Python program?

- What is the purpose of the `open` function?

- What is the purpose of the `line.startswith` function?

</v-clicks>

---

# Using Python to Find an Email in a File

```python {all|1|2|3-4|all}
file = open("emails")
for line in file:
  name, email = line.split(",")
  if name == "John Davis":
    print(email)
```

<v-clicks>

- Can you explain the behavior of this program segment?

- What are the constructs inside of this program segment?

- How is this different than a full-fledged Python program?

- What is the purpose of the `line.split` function?

</v-clicks>

---

[//]: # (Slide Start {{{)

# Python Script for Average Computation

<div class="ml-1">

```python {all|1-2|3|4-7|8|all}
sum = 0
count = 0
file = open("observations")
for line in file:
  n = int(line)
  sum += n
  count += 1
print(sum/count)
```

</div>

<br>

<v-clicks>

<p class = "bold">
What are the contents of the <code>observations</code> file?
</p>

<p class = "bold">
What is the purpose of the <code>for line in file</code> statement?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

# Useful Mathematical Terminology

-   To be clear and succinct, we use mathematical terminology as a
    vocabulary for talking about Python programs

-   What are mathematical terms that aid programming?

    -   **Set**: an unordered collection of different entities

    -   **Sequence**: an ordered collection of entities

    -   **Relation**: a set that relates pairs of things with each other

    -   **Mapping**: a set of ordered pairs in which no two first
        elements are the same (sometimes called a "function" in
        mathematics)

-   Can you find these mathematical concepts in the Python programs? What is a
file? What does iteration normally process? What are the benefits?

---

# Properties of Integer Addition

-   The average computation program processes integer values that are
    governed by mathematical rules

-   Precisely define the set of observations: $O = \{ o_i : o_i \in
          \mathbb{Z}\}$

-   Two properties of integer addition

    -   **Associative**: $(a + b) + c = a + (b + c), \forall a, b, c \in
                  \mathbb{Z}$

    -   **Commutative**: $a + b = b + a, \forall a, b \in \mathbb{Z}$

-   Wait, is the collection of observations a set? No, not if it
    contained recorded temperature values! It can have repeated items,
    which means it is a **multiset**.

