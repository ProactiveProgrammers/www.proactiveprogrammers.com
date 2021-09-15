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

## Programming Constructs

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

## Key Questions

> How do I use **iteration** and **conditional logic** in a Python program to perform
> computational tasks like processing a file's contents and mathematical tasks
> like using Newton's method to approximate the square root of a number?

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
Let's see how to use iteration and conditional logic!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Python Programming Retrospective

<v-clicks>

-   Intuitively read the code segments to grasp their behavior

-   Key components of Python programming segments:

    -   Function calls
    -   Assignment statements
    -   Iteration constructs
    -   Conditional logic
    -   Variable creation
    -   Variable computations
    -   Variable output

-   Investigate the **syntax** and **semantics** of these components!

- Understand how to **connect** these components together in a program!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Programs are Sequences of Statements

<v-clicks>

```python
file = open("emails")
for line in file:
  name, email = line.split(",")
  if name == "John Davis":
    print(email)
```

- A Python program is a sequence of statements

- Programs contain both **simple** and **compound** statements

- Why might some developers say that this is not a "Python program"?

- We will adopt more full-featured approaches in projects!

</v-clicks>

[//]: # (Slide End }}})

---

# Simple and Compound Statements

<v-clicks>

```python
sum = 0
count = 0
file = open("observations")
for line in file:
  n = int(line)
  sum += n
  count += 1
print(sum/count)
```

- Programs contain both **simple** and **compound** statements

- Which of these statements are simple?

- Which of these statements are compound?

</v-clicks>

---

[//]: # (Slide End }}})

# Industry-Standard Python

<v-clicks>

-   Please use Python 3 for all of your programs!

-   Add **docstring** comments to your Python programs

    -   Module
    -   Class
    -   Function

-   Add **comments** for **important blocks** of your program

-   Use **descriptive**  variable and function **names**

- Create **command-line** interfaces using **Typer** and **Poetry**

-   The book does not always adhere to industry standards! 😉

</v-clicks>

[//]: # (Slide End }}})

---

# Quadratic Root Calculation

```python {all|1-3|4-7|8-10|11-12|all}
def main(
    a: float = typer.Option(1), [...]
):
    console.print(f"Calculating roots with:")
    console.print(f"   a = {a}")
    console.print(f"   b = {b}")
    console.print(f"   c = {c}")
    x_one, x_two =
           rootfind.
    calculate_quadratic_equation_roots(a, b, c)
    console.print(f"   x_one = {x_one}")
    console.print(f"   x_two = {x_two}")
```

---

# Roots of a Quadratic Function

<v-clicks>

<div class = "-ml-15">

```python
def calc_quad_eqn_roots(a: float, b: float, c: float):
    """Calculate roots of quadratic equation."""
    D = (b * b - 4 * a * c) ** 0.5
    x_one = (-b + D) / (2 * a)
    x_two = (-b - D) / (2 * a)
    return x_one, x_two
```

</div>

- Three floating-point inputs called `a`, `b`, and `c` are inputs

- Two floating-point outputs called `x_one` and `x_two` are outputs

- How does it calculate the roots of a quadratic equation?

- How could we test this function to ensure its correctness?

</v-clicks>

---

# Testing a Root Finding Function

<v-clicks>

```python
def test_calculate_x_values_non_imaginary():
    """Check calculation of x values."""
    a = 1
    b = 2
    c = 1
    x_one, x_two =
           rootfind.
           calc_quad_eqn_roots(a, b, c)
    assert x_one == -1.0
    assert x_two == -1.0
```

What does this tell us about the function's expected output?

</v-clicks>

---

<v-clicks>

# Equations for Root Finding

$$
x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}
$$

$$
x_2=\frac{-b-\sqrt{b^2-4ac}}{2a}
$$

- What is the meaning of the **root** of a quadratic equation?

- For a quadratic equation $f(x)= a \times x^2 + b \times x +c$, the
variables $x_1$ and $x_2$ are the points where the **equation's output are
the same**

- Can you see the **connection** between the **source code** and the **equations**?

- What are the **trade-offs** of using either Python code or an equation?

</v-clicks>

---

# Using `for` Loops in Python Programs

<v-clicks>

```python
for i in range(20):
    print("2 to the " + str(i)
          + " power is " + str(2**i))
```

- **Iteration constructs** enable a program to **repeat computations**

- The `for` loop displays the powers of 2 from 0 to 19

- The `range` function returns the values from 0 to 19

- The `2**i` performs the computation of $2^i$

- The `str` function converts an integer to a string

- Any questions about this iteration construct?

</v-clicks>

---

# Using `while` Loops in Python Programs

<v-clicks>

```python
i = 0
while i < 20:
    print("2 to the " + str(i)
          + " power is " + str(2**i))
    i += 1
```

- **Iteration constructs** enable a program to **repeat computations**

- The `for` loop and the `while` loop are equivalent

- The `print` statement is the same for both of the loops

- The purpose of `i += 1` is to increment the loop counter

- Any questions about this iteration construct?

</v-clicks>

---

# Output of Both Iteration Constructs

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
    2 to the 0 power is 1
    2 to the 1 power is 2
    2 to the 2 power is 4
    2 to the 3 power is 8
    2 to the 4 power is 16
    2 to the 5 power is 32
    2 to the 6 power is 64
    2 to the 7 power is 128
    2 to the 8 power is 256
    2 to the 9 power is 512
    2 to the 10 power is 1024
    2 to the 11 power is 2048
    2 to the 12 power is 4096
    2 to the 13 power is 8192
    2 to the 14 power is 16384
    2 to the 15 power is 32768
    2 to the 16 power is 65536
    2 to the 17 power is 131072
    2 to the 18 power is 262144
    2 to the 19 power is 524288
</pre>

</div>


[//]: # (Slide End }}})


