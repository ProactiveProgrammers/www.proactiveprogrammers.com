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

## Python Foundations

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

> How can I use **functions**, **variables**, **conditional logic**, and
> **iteration constructs**, as provided by the Python programming language, to
> implement programs that, for instance, determine if a number is even or odd,
> compute a number's square or determine if a number is divisible by another
> number?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some computer science and Python
> programming foundations, setting the stage for exploring data abstraction.

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
What is challenging about programming in Python?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is difficult about (Python) programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Halting problem and algorithmic undecidability
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Syntax and semantics of the Python language
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Testing, debugging, and program correctness
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
Sure, but what can go wrong?
</div>

</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What if semantics do not match our intentions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Program crash and/or obviously incorrect output
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Program continues to run and seems to not halt
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Runs to completion and produces (correct?) output
</div>

</div>

</div>

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

[//]: # (Slide Start {{{)

# Python Function without Annotations

<div class="-ml-0">

```python {all|1|3|4-5|6-7|8|all}
def extract_urls(df):
    """Extract a list of urls."""
    urls = []
    if "Url" in df.columns:
        urlc = df["Url"]
        if urlc is not None:
            urls = urlc.tolist()
    return urls
```

</div>

<br>

<v-clicks>

<p class = "bold">
What is the type of <code>df</code> ? The terrible docstring does not say!
</p>

<p class = "bold">
What is the behavior of <code>return urls</code> in this function?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Python Function with Annotations

<div class="-ml-9">

```python {all|1}
def extract_urls(df: pandas.DataFrame) -> List[str]:
    """Extract a list of urls."""
    urls = []
    if "Url" in df.columns:
        urlc = df["Url"]
        if urlc is not None:
            urls = urlc.tolist()
    return urls
```

</div>

<br>

<v-clicks>

<p class = "bold">
What is the purpose of <code>df: pandas.DataFrame</code> ?
</p>

<p class = "bold">
How does <code>List[str]</code> describe output of <code>extract_urls</code> ?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Determining if a Number Even or Odd

<div class="ml-1">

```python {all|1|2|3-4|5-6|8-10|all}
def determine_even_odd(value: int) -> str:
    """Determine if a number is even or odd."""
    if value % 2 == 0:
        return "even"
    else:
        return "odd"

number = 10
response = determine_even_odd(number)
print(f"The number of {number} is {response}!")
```

</div>

<br>

<v-clicks>

<div class = "bold mt-2">
How is this <b>different</b> than the code segment in the book?
</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Squaring an Integer &mdash; Well, Kinda! 😉

<div class="ml-1">

```python {all|1-2|3-4|5-7|8|9-11|all}
def compute_square(value: int) -> int:
    """Square a number through iteration."""
    num_iterations = 0
    answer = 0
    while num_iterations < value:
        answer = answer + value
        num_iterations = num_iterations + 1
    return answer

value = 3
value_squared = compute_square(value)
print(f"{value} * {value} = {value_squared}")
```

</div>

[//]: # (Slide End }}})

---

# Squaring an Integer &mdash; Much Better! 😂

<div class="ml-1">

```python {all|1-2|3-4|5-7|8|9-11|all}
def compute_square_for(value: int) -> int:
    """Square a number through iteration."""
    answer = 0
    for _ in range(abs(value)):
        answer = answer + abs(value)
    return answer

value = -3
value_squared = compute_square_while(value)
print()
print(f"{value} * {value} = {value_squared}")
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Python Programming Constructs ♻

- Reminder: intuitively read the code segments to grasp their behavior

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

<mdi-help-box class="text-6xl ml-4 mt-0 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-4 ml-4">
Questions about the Python source code?
</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Take home points about Python programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Implement with correct syntax and semantics
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Try to create reusable and testable functions
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Avoid program defects and follow conventions
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Investigating Foundations of Python

<div class = "mt-10">
</div>

-   Implementing programs in the Python language:

    -   **Q1**: What is the **syntax** of a programming language?

    -   **Q2**: What are the **semantics** of a programming language?

    -   **Q3**: What are some **best practices** for Python programming?

    -   **Q4**: What is a **reserved word** in the Python language?

    -   **Q5**: How does the Python language perform **type checking**?

-   How do you pick between the `for` and `while` loop?

-   Don't forget to find the defect in the `compute_square` function!

[//]: # (Slide End }}})
