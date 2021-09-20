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

## Python Functions

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

## Key Questions

> How do I use **non-recursive** functions, **recursive** functions, and
> **lambda expressions** to perform mathematical operations such as computing
> the **absolute value** of a number and the **mean** of a sequence of numbers?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some discrete mathematics and Python
> programming concepts, setting the stage for exploring of discrete structures.

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the types of functions in Python!
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

# Investigating Python and Mathematics

<v-clicks>

-   How do you pick between the `for` and `while` loops?

-   Program for the root finding of a quadratic equation:

    -   **Q1**: What does it mean if a number is **imaginary**?

    -   **Q2**: What happens if the **root** of the equation is **imaginary**?

    -   **Q3**: How do **tests** use **assertions** for **floating point** values?

    -   **Q4**: How can you **confirm** that a function **works correctly**?

    -   **Q5**: How do you know when you have **tested enough**?

-   Can you translate the root finding equation into a complete Python program
with a command-line interface? Can you ensure its correctness? Can you follow
industry standards for comments, format, and testing?

</v-clicks>
