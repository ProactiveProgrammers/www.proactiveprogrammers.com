---
# use the default theme
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# define the highlighter and the colorSchema
highlighter: prism
colorSchema: light
remoteAssets: false
# show line numbers in code blocks
lineNumbers: false
# define the fonts and their weights
fonts:
  # define the font for the body text
  sans: 'IBM Plex Sans'
  # define the serif font
  serif: 'IBM Plex Serif'
  # define the code font
  mono: 'IBM Plex Mono'
  # load several font weights
  weights: '200,400,500'
  # support the use of italics
  italic: true
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
    @apply text-orange-600 mb-2;
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

-   Investigate the **syntax** and **semantics** of these components

-   Understand how to **connect** these components together in a program

-   **Implement** Python functions to **understand** mathematical functions

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

-   All course projects will enforce these standards in GitHub Actions

</v-clicks>

[//]: # (Slide End }}})

---

# Quadratic Root Calculation

<div class="-mt-4">

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

</div>

---

# Roots of a Quadratic Function

<v-clicks>

<div class = "-ml-15 -mb-3">

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

# Calling a Root Finding Function


<v-clicks>

<div class = "-mt-4 -mb-5">

```python
a = 1
b = 2
c = 1
x_one, x_two = calc_quad_eqn_roots(a, b, c)
print(f"✨ The first root of the equation is
           {x_one}")
print(f"✨ The second root of the equation is
           {x_two}")
```

</div>

- What is the input provided to this function?

- What is the output produced by this function?

- What is the purpose of the notation `{x_two}` ?

</v-clicks>

---

# Testing a Root Finding Function

<v-clicks>

<div class = "-ml-5 -mb-3">

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

</div>

What does this tell us about the function's **expected output**?

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What the benefits of defining a function?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Repeatedly call function with different inputs
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Avoid having to re-define function body
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Effectively supports testing and debugging
</div>

</div>

</div>

[//]: # (Slide End }}})

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
the same** on x-axis

- Can you see the **connection** between the **source code** and the **equations**?

- What are the **trade-offs** of using either Python code or an equation?

</v-clicks>

---

[//]: # (Slide Start {{{)

# Visualizing a Quadratic Function

<style>
  .constraint {
    width: 100%;
  }
</style>

<br>

<div class="constraint -mt-7">

![Quadratic Function](/quadratic-graph-one-two-one.svg)

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Visualizing a Quadratic Function

<style>
  .constraint {
    width: 100%;
  }
</style>

<br>

<div class="constraint -mt-7">

![Quadratic Function](/quadratic-graph-one-negativeseven-ten.svg)

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about quadratic root finding?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Only applies to quadratic equations
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Finds inputs where the outputs are the same
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
A single function can perform the computation
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's use Python to understand the math!
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

<div class="text-3xl font-bold mt-10 ml-1">
Go to the <code>programming-constructs/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>calculate-quadratic-roots.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

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

---

# Loops for Square Root Approximation

<v-clicks>

```python
n = 4
guess = 1.0
while abs(n - guess*guess) > 0.0001:
    guess = guess - (guess*guess - n)/(2*guess)
root = guess
```

- Iteratively **guesses** the square root until **within tolerance**

- The `while` loop uses `abs` for computing an absolute value

- This loop computes the root as 2.0000000929222947

- The `math.sqrt(n)` function confirms this approximation!

- Any questions about this way to approximate a square root?

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about square root calculation?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Iteratively computes a guess for the function
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Continues until the guess is within a tolerance
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Uses floating-point variables to store guesses
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's use Python to understand the math!
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

<div class="text-3xl font-bold mt-10 ml-1">
Go to the <code>programming-constructs/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>calculate-approximate-square-root.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

# Mathematics with Python

<v-clicks>

-   Try to see how an equation connects to the source code!

-   Use a Python function to explore a mathematical function

-   Key components of Python programming segments:

    -   Function calls
    -   Assignment statements
    -   Iteration constructs
    -   Conditional logic
    -   Variable creation
    -   Variable computations
    -   Variable output

-   Programs must **correctly implement** the **mathematical equation**

-   Programs must have **industry-standard** comments, code layout, and tests

</v-clicks>

[//]: # (Slide End }}})

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

-   Can you **translate** the root finding equation into a complete Python program
with a command-line interface? Can you **ensure** its correctness? Can you **follow**
industry standards for comments, code layout, and testing?

</v-clicks>
