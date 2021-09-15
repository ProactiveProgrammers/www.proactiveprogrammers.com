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

## Numerical Computation

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

> How can I use **functions**, **floating-point variables**, **conditional
> logic**, and **iteration constructs** to implement both **exhaustive** and
> **approximate** approaches to compute (i) the square root of a number, (ii) the
> logarithm of a number, and (iii) the roots of a polynomial function?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some algorithmic, numerical, and Python
> programming foundations, setting the stage for exploring data abstraction.

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are key constructs in Python programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Conditional logic let's programs make decisions
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Iteration constructs support repeated operations
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Variables support the storage of data values
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are two key algorithmic strategies?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Exhaustive enumeration
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-layer-group class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Bisection search
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<div class="text-3xl font-bold mt-8 ml-4">
Both approaches can compute approximate solutions to numerical computations
like primality testing
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the trade-offs of these approaches?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Exhaustive enumeration is easier to implement
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Bisection search tends to be faster than exhaustive
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Bisection search is often harder to implement
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# A First Look at Exhaustive Enumeration

<v-clicks>

- Many numerical computations require a specific output value for an input,
often achieved by iteration with a **decrementation approach**

- The **exhaustive enumeration** approach "naively" looks through **all
possibilities** until it finds the correct solution

- How does exhaustive enumeration work?
    - List all possible values for a computation
    - Check to see if the current value is correct
    - If not correct, try the next value in the list
    - Continue until the correct value is found

- Easy to implement and understand. Often fast enough for practical purposes!

- When is it not efficient enough to perform exhaustive enumeration?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exhaustive Primality Testing

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

# Is a Number Even or Odd?

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
What do we know about program variables?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Store a value received during assignment
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Have an associated type restricting values
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Serve as input and output of a function
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Variables in Python Programs

<v-clicks>

-   Variables in Python have values, types, and names

-   A function can manipulate a variable using operators

    -   The `+` symbol denotes addition and concatenation

    -   The `-,*,/` symbols denotes have standard meanings

    -   The `+=` symbol denotes addition and assignment

    -   The `%` symbol denotes modular arithmetic for a remainder

-   **Variable Types**: The `type(a)` returns the type of `a`

-   **Type Changing**: `int(a)` transforms variable `a` into an integer type

</v-clicks>

[//]: # (Slide End }}})

---

# Practical Variable Limitations in Python

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
Python 3.8.5 (default, Jul 23 2020, 21:35:10)
[GCC 10.1.0] on linux
>>> 2**2**8
115792089237316195423570985008687907853269984665640564039457584007913129639936
>>> 2**2**10
1797693134862315907729305190789024733617976978942306572734300811577326758055009
6313270847732240753602112011387987139335765878976881441662249284743063947412437
7767893424865485276302219601246094119453082952085005768838150682342462881473913
110540827237163350510684586298239947245938479716304835356329624224137216
>>> 2**2**100
^CTraceback (most recent call last):
  File "stdin", line 1, in module
KeyboardInterrupt
</pre>

</div>

- Can you explain the **output** of the computations one and two?

- Why did the third computation **crash**, not terminate, and not produce output?

- How do these **limitations** influence the tasks of programmers?

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Comparing Variables in Python

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
>>> 1.0 == 1.1
False
>>> 1.0 == 1
True
>>> 'h' + 'i' + '!'
'hi!'
>>> .33333 + .33333 + .33333 == 1
False
>>> .33333333333 + .33333333333 + .3333333333 == 1
False
>>> 1/3
0.3333333333333333
>>> 1/3 + 1/3 + 1/3 == 1
True
>>> count = 0
>>> count += 1
>>> count
1
</pre>

</div>

<div class="mt-5">
</div>

- How does this **match** and **diverge** from your intuition?

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

<v-clicks>

-   Implementing programs in the Python language:

    -   **Q1**: What is the **syntax** of a programming language?

    -   **Q2**: What are the **semantics** of a programming language?

    -   **Q3**: What are some **best practices** for Python programming?

    -   **Q4**: What is a **reserved word** in the Python language?

    -   **Q5**: How does the Python language perform **type checking**?

-   How do you pick between the `for` and `while` loop?

-   Don't forget to find the defect in the `compute_square` function!

</v-clicks>

[//]: # (Slide End }}})
