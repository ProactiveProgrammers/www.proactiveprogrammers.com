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

## Program Components

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

> How can I use different types of program components, such as recursive
> functions and modules to make efficient programs with effective designs?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of program components so as
> to implement programs that use recursive functions, global variables, program
> modules, external libraries, and files.

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the use of program components!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are foundations of Python functions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Input: accepts one or more variables as input
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Output: return one or more variables as output
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Behavior: computation with or without side-effects
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Python Programming with Functions

<v-clicks>

-   Intuitively read the functions to grasp their behavior

-   Key components of the Python functions

    -   Definition of the function

    -   Parameter(s) that serve as the input

    -   Body that performs a computation

    -   Function return value(s) that produce output

    -   Invocation of the function

    -   Collecting the output of the function

-   Investigate the ways to **define** and **call** Python functions!

</v-clicks>

[//]: # (Slide End }}})

---

# Computing the Arithmetic Mean

```python
def compute_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean
numbers = [5,1,7,99,4]
print(str(compute_mean(numbers)))
```

<div-clicks>

<div class="mt-8">

- How do we compute the **mean** of a list of numbers?

- How do we compute **summary statistics** of a list of numbers?

- Non-recursive function definition

</div>

</div-clicks>

---

# Type Hints for Function Parameters

```python
from typing import List

def compute_mean(numbers: List) -> int:
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean
```

- How is this function different from the previous one?

- What are the benefits of adding type hints to parameters?

- What are the downsides of adding type hints to parameters?

---

# Recursive Functions in Python

```python
def factorial(number: int):
    if number == 1:
        return 1
    return number * factorial(number - 1)
num = 5
print("The factorial of " + str(num) +
        " is " + str(factorial(num)))
```

<v-clicks>

<div class="mt-10">

- The recursive `factorial` function calls itself!

- How does this function ever stop executing? 🤔

- What are the benefits to using recursive functions?

</div>

</v-clicks>

---

# Recursive Factorial Function

<v-clicks>

-   As an equation:
    $n! = n \times n-1 \times n-2 \times \ldots \times 1$

-   What are the **parts** of a recursive function in Python?

    -   Defined by **cases** using conditional logic

    -   A function definition that **calls itself**

    -   A recursive call that makes progress to a **base case**

    -   A **base case** that **stops** the **recursive function calls**

-   Repeatedly perform an operation through function calls

-   What would happen if you input a **negative number**?

-   How could you write this function with **iteration**?

</v-clicks>

---

# Finding Parts of Recursive Functions

```python
def factorial(number: int):
    if number == 1:
        return 1
    return number * factorial(number - 1)

num = 5
print("The factorial of " + str(num) +
        " is " + str(factorial(num)))
```

<v-clicks>

- Where is the **base case**?

- Where is the **recursive case**?

- How does this function **make progress** to the **base case**?

</v-clicks>

---

[//]: # (Slide Start {{{)

# Investigating Program Components

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
