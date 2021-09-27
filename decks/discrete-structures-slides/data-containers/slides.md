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

## Data Containers

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

> How do I use the mathematical concepts of **ordered pairs**, **n-tuples**, and
> **lists** to implement functions with a clearly specified behavior to perform
> tasks like the **input** and **parsing** of a comma separated value (CSV)
> file?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some discrete mathematics and Python
> programming concepts, enabling the investigation of practical applications

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the use of data containers in Python!
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

# Absolute Value of a Number

```python {all}
def abs(n):
    if n >= 0:
        return n
    else:
        return -n
```

- The absolute value of a number is its distance from zero

- What is the meaning of the operator `>=` ?

- What is the output of `print(str(abs(10)))` ?

- What is the output of `print(str(abs(-10)))` ?

- Are there other ways to implement this function?

---

# Absolute Value of a Number

```python {all}
def abs(n):
    if n >= 0:
        return n
    return -n
```

- The absolute value of a number is its distance from zero

- Does this function compute the same value?

- Which implementation of `abs` do you prefer?

- Which implementation of `abs` does `pylint` prefer?

- There are different ways to implement the same function!

---

# Using Newton's Method in a Function

```python {all}
def sqrt(num: int, tol: float):
    guess = 1.0
    while abs(num - guess*guess) > tol:
        guess = guess -
        (guess*guess - num)/(2*guess)
    return guess
```

- The `sqrt` function calculates the square root of `num`

- What is the meaning of `num:int` and `tol:float`?

- What are the benefits of defining this as a function?

- How could we test the `sqrt` function using Pytest?

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

<div class="mt-10">

- The recursive `factorial` function calls itself!

- How does this function ever stop executing? 🤔

- What are the benefits to using recursive functions?

</div>

---

# Recursive Factorial Function

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

- Where is the base case?

- Where is the recursive case?

- How does this function make progress to the base case?

---

[//]: # (Slide Start {{{)

# Higher-Order Functions

<div class="ml-1">

```python {all|1-4|6-8|all}
def square(number: int):
    print(f"Called square({number})")
    print(f"  returning {number*number}")
    return number * number

def call_twice(f, number: int):
    print(f"Calling twice {f} with number {number}")
    return f(f(number))
```

</div>

<div v-click>

<div class="flex row">

<div class="text-3xl font-bold mt-8 ml-4">
Higher-order functions can accept and call functions as their input! What are the benefits of this function type?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Understanding Higher-Order Functions

<v-clicks>

-   You can pass a **function** as an **argument** to a **function**!

-   The behavior of **higher-order** functions in Python:

    -   **Step 1**: `square` is a function that computes and returns
        $x^2$

    -   **Step 2**: `call_twice` is a function that calls a function `f`
        twice

    -   **Step 3**: First, `call_twice` calls `f` with ` number`

    -   **Step 4**: Then, `call_twice` calls `f` with ` f(number)`

    -   **Step 5**: Finally, `call_twice` returns result of
        ` f(f(number))`

-   Can you predict the output of the `call_twice` function? How would
    you test the `call_twice` function? Can you express it differently?

</v-clicks>

---

# How to Call Higher-Order Function

```python {all}
num = 5
result = call_twice(square, num)
print("Calling the square twice with " +
      str(num) + " is " + str(result))

num = 5
result = num ** 4
print("Computation of twice square is "
      + str(num) + " is " + str(result))
```

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-4 mt-0 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-4 ml-4">
The output of the two print statements?
</div>

</div>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of higher-order functions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports general-purpose function creation
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Allows executable functions as function input
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports both code reuse and modularity
</div>

</div>

</div>

[//]: # (Slide End }}})


---

# Lambda Expressions in Python

```python {all}
square = lambda x: x*x
num = 5
result = call_twice(square, num)
print("Calling square lambda twice " +
      "with " +
      str(number) +
      " is " +
      str(result))
```

- Functions are values in the Python programming language

- `square` is an expression that has a function as its value

---

# Understanding Lambda Expressions

<v-clicks>

-   You can define a "function" without an explicit signature!

-   What are benefits of `square = lambda x: x*x` ?

-   What are drawbacks of `square = lambda x: x*x` ?

-  How do decide between function and lambda expression?

- **Use case**: simple-to-implement mathematical function

-   How do you test a lambda function in a Python program?

-   Implement $n! = n \times n-1 \times n-2 \times \ldots \times 1$ as
    lambda?

<div class="flex row">

<mdi-help-box class="text-6xl ml-4 mt-0 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-4 ml-4">
Questions about using lambda expressions?
</div>

</div>

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of lambda expressions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Lightweight way to specify a computation
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Compared to the function, often faster to create
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Useful for small functions input to other functions
</div>

</div>

</div>

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

<div class="mt-8">

- How do we compute the **mean** of a list of numbers?

- How do we compute **summary statistics** of a list of numbers?

- What type of function? Recursive? Iterative? Lambda?

</div>

---

# Type Hints for Function Parameters

```python
from typing import List

def compute_mean(numbers: List):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean
```

- How is this function different from the previous one?

- What are the benefits of adding type hints to parameters?

- What is currently left out of this function signature?

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of type annotations?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Specifies the types of function inputs and outputs
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports type checking with tools like <code>mypy</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Helps <code>pylance</code> offer feedback in VS Code
</div>

</div>

</div>

---

[//]: # (Slide End }}})


# Implementing and Testing Functions

<v-clicks>

-   How do you pick between the **different types** of **functions**?

-   Python functions to perform **statistical analysis** of data:

    -   **Q1**: How do you compute the **median** of a list of numbers?

    -   **Q2**: How do you compute the **mode** of a list of numbers?

    -   **Q3**: How do you compute a **frequency table** of a list of
        numbers?

    -   **Q4**: How do you compute the **range** of a list of numbers?

    -   **Q5**: How do you compute the **variance** and **standard deviation**?

-   Can you **translate the mathematical descriptions** of these summary statistics
to **Python programs**? Can you ensure their correctness with testing?

</v-clicks>
