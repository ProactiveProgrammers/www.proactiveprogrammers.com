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

- What are the **benefits** of adding type hints to parameters?

- What are the **downsides** of adding type hints to parameters?

---

# Recursive Functions in Python

```python
def factorial(number: int) -> int:
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
def factorial(number: int) -> int:
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

# Iterative Fibonacci with Tuples

```python {all|1|2-4|5-7|8|10-11|all}
def fibonacci_tuple(n: int) -> Tuple[int]:
    result = ( )
    a = 1
    b = 1
    for i in range(n):
        result += (a,)
        a, b = b, a + b
    return result

for fibonacci_value in fibonacci_tuple(10):
    print(fibonacci_value, end=" ")
```

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Iterative Fibonacci with Lists

```python {all|1|2-4|5-7|8|10-11|all}
def fibonacci_list(n: int) -> List[int]:
    result = [  ]
    a = 1
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

for fibonacci_value in fibonacci_list(10):
    print(fibonacci_value, end=" ")
```

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Iterative Fibonacci with Generator

```python {all|1|2-3|4-6|8-9|all}
def fibonacci_generator(n: int) -> Iterator[int]:
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for fibonacci_value in fibonacci_generator(10):
    print(fibonacci_value, end=" ")
```

<v-clicks>

- The generator function uses `yield` to operate incrementally

- Each function performs the same computation ... differently! How? Trade-offs?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Recursive Fibonacci Implementation

```python {all|1|2-3|4-6|8-9|all}
def fibonacci_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) +
             fibonacci_recursive(n-2)

for i in range(10):
    print(f"fib of {i} = ")
    print(f"{fibonacci_recursive(i)}")
```

[//]: # (Slide End }}})

---

# Output of the Recursive Fibonacci

<style>
  h2 {
    font-size: 42px;
    @apply text-orange-600 mb-4;
  }
  li {
    font-size: 28px;
    margin-top: 4px;
    margin-bottom: 9px;
  }
</style>

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5">

<pre>
fib of 0 is 1
fib of 1 is 1
fib of 2 is 2
fib of 3 is 3
fib of 4 is 5
fib of 5 is 8
fib of 6 is 13
fib of 7 is 21
fib of 8 is 34
fib of 9 is 55
</pre>

</div>

[//]: # (Slide End }}})

- Output shows that the 10th Fibonacci number is 55

- Do the iterative algorithms produce the same output?

- How many times is `fibonacci_recursive` called? Why important?

- Could add a tracking global variable called `num_fib_calls`

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are foundations of recursive functions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Base case: stop the execution of function
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Recursive case: call the function again
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Progress: move towards the base case
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Using Modules and Files in Python

<v-clicks>

-   Modules are individual `.py` files with definitions and statements

-   Key insights about the use of modules:

    -   **Standard library** packages are a part of the Python language

    -   Examples of packages: `Pathlib` and `os` and `system`

    -   **External** packages are available through Python Packing Index (PyPI)

    -   Learn more about PyPI by visiting `https://pypi.org/`

    -   Need to manage **virtual environments** and **package dependencies**

    -   **Tool support**: Poetry, Pipenv, pip, venv, virtualenv-wrapper, ... !

-   What are the **challenges** associated with using external packages?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Using Predefined Packages in Python

<v-clicks>

-   Leverage the source code provided by existing projects!

-   Key insights about the use of modules

    -   **Organize** modules around their **functionality**

    -   Have a **test suite** for each module in the system

    -   Write **test cases** for each function in the module

    -   Provide a **docstring** for each module and each function

    -   When necessary **import** one module into another module

    -   Use the **fully qualified** name of a module

-   What are the **benefits** associated with organizing code into modules?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Using `Typer` and `Pathlib` for File Input

```python {all|1-5|6|7|8-12|all}
@cli.command()
def launch(
  rocket_dir: Path = typer.Option(None),
  rocket_file: Path = typer.Option(None)
):
  rocket_file = rocket_dir / rocket_file
  if confirm_valid_file(rocket_file):
  rocket_contents_text =
      rocket_file.read_text()
      print(rocket_contents_text)
  else:
      print(f"{rocket_file} was not valid")
```

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Determining if a File is Valid

```python {all|1-5|6|7|8-12|all}
def confirm_valid_file(file: Path) -> bool:
    if file is not None:
        if file.is_file():
            return True
    return False
```

[//]: # (Slide End }}})

<v-clicks>

- **Typer** and **Pathlib** are beneficially **integrated** together

- Pathlib is often **preferable** to standard approaches

- Why is it important to determine if a file is **valid**?

- What happens if the program receives an **invalid** file as input?

- What can **go wrong** when performing file input and output?

</v-clicks>

---

[//]: # (Slide Start {{{)

# Investigating Program Components

<div class = "mt-10">
</div>

<v-clicks>

-   Correct use of program components in Python programs:

    -   **Q1**: What are the benefits of **recursive** functions?

    -   **Q2**: What are the different ways to implement **Fibonacci**?

    -   **Q3**: What are the **trade-offs** of function choices?

    -   **Q4**: What the benefits of using program **modules**?

    -   **Q5**: How to external **packages** aid Python programmers?

-   Balance the **trade-offs** associated with different functions!

-   Judiciously use **external** program modules when programming

</v-clicks>

[//]: # (Slide End }}})
