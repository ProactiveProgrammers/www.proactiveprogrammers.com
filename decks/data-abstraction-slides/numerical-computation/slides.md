---
# try also 'default' to start simple
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: prism
colorSchema: light
remoteAssets: false
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

# Python Programming Constructs

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

```python {all|1|2|3-6|7-8|9-10|all}
x = int(input("Enter integer greater than 2: "))
sm_div = None
for guess in range(2, x):
    if x % guess == 0:
        sm_div = guess
        break
if sm_div != None:
    print(f"Smallest divisor of {x} is {sm_div}")
else:
    print(f"Wow, {x} is a prime number!")
```

</div>

<br>

<v-clicks>

<p class = "bold">
What is the purpose of the <code>range(2, x)</code> function call?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Efficient Primality Testing

<div class="ml-1">

```python {all|1|2|3-4|5-6|7-9|all}
x = int(input("Enter integer greater than 2: "))
sm_div = None
if x % 2 == 0:
    sm_div = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            sm_div = guess
            break
```

</div>

<br>

<v-clicks>

<p class = "bold">
What is the purpose of the <code>range(3, x, 2)</code> function call?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Table of Prime Numbers

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
      2      3      5      7     11     13     17     19     23     29
     31     37     41     43     47     53     59     61     67     71
     73     79     83     89     97    101    103    107    109    113
    127    131    137    139    149    151    157    163    167    173
    179    181    191    193    197    199    211    223    227    229
    233    239    241    251    257    263    269    271    277    281
    283    293    307    311    313    317    331    337    347    349
    353    359    367    373    379    383    389    397    401    409
    419    421    431    433    439    443    449    457    461    463
    467    479    487    491    499    503    509    521    523    541
    547    557    563    569    571    577    587    593    599    601
    607    613    617    619    631    641    643    647    653    659
    661    673    677    683    691    701    709    719    727    733
    739    743    751    757    761    769    773    787    797    809
    811    821    823    827    829    839    853    857    859    863
    877    881    883    887    907    911    919    929    937    941
    947    953    967    971    977    983    991    997   1009   1013
</pre>

</div>

<div class="mt-5">
</div>

- Do these programs correctly detect prime numbers?

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What do we know about primality testing?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Both methods compute the same answer
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Efficient approach disregards even numbers
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Exhaustive approach is a good starting point
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exhaustive Square Root Computation

<div class="ml-1">

```python {all|1|2|3-4|5-7|8|9-11|all}
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1
print(f"Guessed {num_guesses} times")
if abs(ans**2 - x) >= epsilon:
    print(f"Could not find sqrt of {x}")
else:
    print(f"{ans} is close to sqrt of {x}")
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Can we improve this algorithm? Yes, we can!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Numbers are totally ordered, use pair comparison
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Repeatedly move to "left" or "right" on number line
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Repeat process until have an approximate solution
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Bisection Square Root Computation

<div class="ml-1">

```python {all|1-3|4-5|6-7|8-9|10-11|12|all}
epsilon = 0.01
step = epsilon**2
num_guesses, low = 0, 0
high = max(1,x)
answer = (high + low)/2
while abs(answer**2 - x) >= epsilon:
    num_guesses += 1
    if answer**2 < x:
        low = answer
    else:
        high = answer
    answer = (high + low)/2
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Other types of numerical computations in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Compute summary statistics of data set
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Compute dispersion measurements for data
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Helps analyzing data from algorithm experiments
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

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

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Type Hints for Function Parameters

```python
from typing import List

def compute_mean(numbers: List) -> float:
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean
```

- How is this function different from the previous one?

- What are the benefits of adding type hints to parameters?

- Why is this not a complete implementation of `compute_mean` ?

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Insights for numerical computation?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Performance trade-offs with algorithmic approach
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Express computation with a script or a function
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Data analysis is commonly needed for experiments
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

# Investigating Numerical Computation

<div class = "mt-10">
</div>

<v-clicks>

-   Different forms of numerical computation:

    -   **Q1**: What are the benefits of **exhaustive** enumeration?

    -   **Q2**: Why is **exhaustive** enumeration not always efficient?

    -   **Q3**: How does **bisection search** improve algorithms?

    -   **Q4**: How can bisection search **help** other algorithms?

    -   **Q5**: How can we compare the **performance** of two algorithms?

-   We will investigate these algorithms in **upcoming projects**!

-   Guess and check and divide and conquer are **general purpose** strategies

</v-clicks>

[//]: # (Slide End }}})
