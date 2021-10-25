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

## Object-Oriented Programming

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

> How can I use the principles and primitives of object-oriented programming to
> implement Python programs with easy-to-understand designs?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of object-oriented
> programming and the exception handling features provided by Python
> to implement high-quality programs.

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore object-oriented programming!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What can go wrong when using a program?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Division by zero or index out of range
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Networking error or file system problems
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Use does not match programmer expectations!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exception Handling in Python

<v-clicks>

- Program implementation may not match its actual use

- Exception handling provides elegant way handle problems

- `try` and `except` are basic building blocks

- Python allows to you try running "risky code" and then handle problems:

    - `try` block contains code that may throw an exception

    - `except` block handles case when a specific exception arises

    - It is possible to have one or more `except` blocks overall

- What should the program do when the exception is caught?

- Well, it depends on the type of the exception and what happened!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Exception Handling for Ratios

<div class="-ml-5">

```python {all|1-3|4|5|6-7|8-9|10-11|12|all}
from typing import List

def get_ratios(one: List, two: List) -> List[float]:
    ratios = []
    for index in range(len(one)):
        try:
            ratios.append(one[index] / two[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError("Incorrect arguments")
    return ratios
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Use Function with Exception Handling

<div class="-ml-5">

```python {all|1-2|1,3|1,4|1,5|6-7|all}
try:
    print(get_ratios([1, 2, 7, 6], [1, 2, 0, 3]))
    print(get_ratios([], []))
    print(get_ratios([1, 2, 7], [1, 2, 10, 3]))
    print(get_ratios([1, 2, 7, 6], [1, 2, 10]))
except ValueError as message:
    print(message)
```

</div>

<br>

<v-clicks>

<p class = "bold">
What is the <b>output</b> from running these function calls?
</p>

<p class = "bold">
Why do certain <b>inputs</b> cause an exception to be thrown?
</p>

<p class = "bold">
What is there <b>was not</b> a <code>try</code> and a <code>except</code> ?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Investigating Software Testing

<v-clicks>

- Software testing can **accomplish** these **goals**:

    - Find bugs in a Python program by running it
    - Establish a confidence in a Python program's correctness
    - Support confident refactoring of a Python program

-   Importance of software testing for Python programs:

    -   **Q1**: What are the **benefits** of software testing?

    -   **Q2**: What are the **limitations** of software testing?

    -   **Q3**: What are the **trade-offs** associated with software testing?

    -   **Q4**: How do you write a test suite using **Pytest**?

    -   **Q5**: How do you know when you are **finished** testing software?

</v-clicks>

[//]: # (Slide End }}})
