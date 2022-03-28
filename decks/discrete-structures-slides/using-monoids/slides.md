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

# Discrete Structures

## Using Monoids

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

> How do I employ the mathematical concepts of **sequences**, **monoids**, and
> **lists** to implement efficient Python programs that use functions with a
> **clearly specified behavior** to perform tasks like finding a name in a
> file or computing the arithmetic mean of data values?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some the concept of a **monoid**, seeing
> how it connects to **practical applications** with strings and sequences

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Examples of Sequences in Python

<v-clicks>

-   Sequences are commonly found in Python programs!

-   Examples of the **sequence discrete structure** in Python:

    -   A string is a sequence of individual characters

    -   The `range(20)` function returns a sequence of numbers

    -   Files are sequences of lines containing content

    -   Each line in a file is a sequence of individual characters

    -   Each individual character is a sequence of numbers

    -   Each individual number is a sequence of binary digits

-   Do these sequences all have properties in common? Can we **generalize**?

</v-clicks>

---

# Comparing Sequences and n-Tuples

<v-clicks>

-   Are sequences and n-tuples the same? Are they different?

-   Understanding the properties of n-tuples and sequences:

    -   Both n-tuples and sequences are **ordered collections**
    -   Sequences are normally composed of the same type of data
    -   n-tuples are not required to contain the same type of data
    -   Sequences are not "theoretically bounded" in their size
    -   n-tuples are "theoretically bounded" in their size
    -   Both sequences and n-tuples are **practically bounded** in size

-   Do different types of sequences have common properties and behavior?

-   Can we more generally understand these discrete structures?

-   Generalization aids in understanding different discrete structures!

</v-clicks>

---

# String Concatenation in Python

```python
hello = "hello"
world = "world"
space = " "
message = hello + space + world
print(f"The message is: {message}")
```

- You can concatenate or "glue together" strings

- What would happen if you picked a different order?

    -   `hello + space + world`

    -   `space + hello + world`

    -   `world + space + hello`

---

# Reversed String Concatenation

```python
hello = "hello"
world = "world"
space = " "
message = world + space + hello
print(f"The message is: {message}")
```

<v-clicks>

- What is the **output** of this program segment?

- How does Python **represent** a string in memory?

- What are the different **types** of strings?

- What is an **empty string** in Python?

- How is an empty string different from `" "` ?

</v-clicks>

---

# Empty String Concatenation in Python

```python
world = "world"
empty = ""
message = empty + world
print(f"The message is: {message}")
```

<v-clicks>

- The `empty` variable is an identity string

- What is the output of this program segment?

- What if we switched the order of the concatenation?

- How is the `empty` variable different from `" "` ?

- What is an "identity content" for other data types and operators?

</v-clicks>

---

# Reversed Empty String Concatenation

```python
world = "world"
empty = ""
message = world + empty
print(f"The message is: {message}")
```

<v-clicks>

- What is the output of this program segment?

- Why does the order of operations not matter in this case?

- Can we generalize these observations about strings?

- Can we define a general discrete structure with predictable properties?

- If you get confused, revisit what you know about `str` in Python!

</v-clicks>

---

# Characterizing String Concatenation

<v-clicks>

-   Define $S$ to be the set of all possible strings

-   What properties of $S$ are always true?

    -   For $s_1, s_2 \in S$ and the concatenation operator "$+$", $s_1
                  + s_2 \in S$

    -   For $s_1, s_2, s_3 \in S$, "$+$" is associative: $(s_1 + s_2) +
                  s_3 = s_1 + (s_2 + s_3)$

    -   For $s_1, s_2, \in S$, "$+$" is not commutative: $(s_1 + s_2)
                  \neq s_2 + s_1$

    -   For $s_1, s_2, \in S$, if $s_1 = s_2$ or either
        $s_1 = \epsilon$, then "$+$" is commutative

-   These properties of strings help us to **generalize** and **understand**
    their behavior! Let's this concept explore further!

-   The **monoid** discrete structure generalizes data that "behaves like
strings"

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are characteristics of strings in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Concatenation through the use of the <code>+</code> operator
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Identity element exists in the <code>""</code> string
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Concatenation is associative but <em>is not</em> commutative
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Motivating the Monoid

<v-clicks>

-   Wow, **strings** and **integers** have **similar** properties!

-   The integers and the mathematical operation of "$+$":

    -   Adding two integers results in another integer

    -   Addition of integers adheres to the associative property

    -   Addition has an identity of $0$ because $0 + n = n + 0$

    -   Key question: are integers and strings of the same general type?

-   **Monoid**: A set that has an **associative binary operator** and an
    **identity element**. How can we explain this more formally?

-   If we know that a discrete structure used in a Python program is a
    monoid then we can understand, predict, and test its behavior!

</v-clicks>

---

# Understanding Monoids

<v-clicks>

-   A monoid is an ordered pair $(S, \otimes)$ for a set $S$ and any
    binary operator $\otimes$ that satisfies the following conditions:

    -   **Type Preservation**: $\forall s_1, s_2 \in S$, $s_1 \otimes
                  s_2 \in S$

    -   **Associative Property**: $\forall s_1, s_2, s_3 \in S$, $(s_1
                  \otimes s_2) \otimes s_3 = s_1 \otimes (s_2 \otimes s_3)$

    -   **Identity Element**: $\exists \epsilon \in S$, such that
        $\forall s \in S, \epsilon \otimes s = s$ and
        $s \otimes \epsilon = s$

-   We often say that "$S$ is a monoid under $\otimes$ with identity
    $\epsilon$"

-   If this is confusing, remember that the discrete structure called a
    monoid is a generalization of strings and integers!

-   If you know how strings behave then you understand the monoid;
    the word "monoid" describes "string-like" structures

</v-clicks>

---

# Applying the Monoid Discrete Structure

-   Monoids **frequently exist** inside of our Python programs!

-   Monoids give a **vocabulary** for describing discrete structures

-   Saying that a structure "is a monoid under a specific identity"
    gives us a **precise understanding** of its behavior

-   Knowing that a discrete structure is a monoid means that we can
    confidently assume that **associativity holds** for its operator

-   That is why, for integers, we can have "big operators" like $\sum$
    for adding numbers and $\prod$ for multiplying numbers as in

    -   $\sum_{i=1}^{n} i$

    -   $\prod_{i=1}^{n} i$

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of the monoid concept?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Generalizes the behavior of structures
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Offers an archetype for understanding
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Enables practical parallel computations
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Sums of Lists in Python

```python
standard_list = [1, 2, 3, 4, 5]
reversed_list = [5, 4, 3, 2, 1]

sum_list = sum(standard_list)
sum_reversed_list = sum(reversed_list)
```

<v-clicks>

- `sum` is a built-in function provided by Python

- What is the output of this program segment?

- This code demonstrates the behavior of the $\sum$ operator

- You can sum numbers in any order and get the same answer!

- Any questions about the use of the `sum` function?

</v-clicks>

---

# Products of Lists in Python

```python
import math
standard_list = [1, 2, 3, 4, 5]
reversed_list = [5, 4, 3, 2, 1]
product_list = math.prod(standard_list)
product_reversed_list =
    math.prod(reversed_list)
```

<v-clicks>

- `math.prod` is a function in the `math` module

- This code demonstrates the behavior of the $\prod$ operator

- Multiplying numbers in any order gets the same answer!

- Any questions about the use of the `prod` function?

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run this code to understand it better!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Visit the <a href = "https://proactiveprogrammers.com/live">Proactive Programmers Live</a> site!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Go to <code>discrete-structures/using-monoids/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-list-manipulation.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# CSV File Containing Population Data

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
1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
1975-01-01,87.000
1976-01-01,87.600
1977-01-01,87.600
1978-01-01,88.000
</pre>

</div>


- CSV file stores ordered pairs of **dates** and **population counts**

- Both lists and tuples are examples of **sequences**

- A tuple is an **immutable** data container

- A list is a **mutable** data container

- What are the **trade-offs** when using these containers?

[//]: # (Slide End }}})

---

# Using Mutable Lists in Python

```python
  data_number_list = []
  for line in data_text.splitlines():
      ordered_pair = line.split(",")
      data_number_list.append(float(
              ordered_pair[1]))
  return data_number_list
```

<v-clicks>

- This source code parses the CSV file and extracts content

- What is the purpose of `ordered_pair[1]` ?

- Does this source code use a tuple or a list?

- Again, what are the differences between lists and tuples?

</v-clicks>

---

# Higher-Order Sequence Functions

<v-clicks>

-   Define **higher-order** functions that work for **any sequence**

-   These functions should work for lists, ordered pairs, tuples:

    -   `map`: Apply a function to every element of a sequence

    -   `filter`: Apply a boolean function to every element of a
        sequence, returning only those matching the filter's rules

    -   `reduce`: Apply a function that acts like a binary operator to a
        sequence of values, combining them to a single value

-   These three operators give a **vocabulary** for implementing complex
    programs in a functional programming style

-   These functions are **higher-order** because they accept function as input

</v-clicks>

---

# Map Function with a Literal Tuple

```python {all|1-2|4-8|10-11|all}
def square(value):
    return value * value

def map(f, sequence):
    result = (  )
    for element in sequence:
        result += ( f(element), )
    return result

squared = map(square, (2, 3, 5, 7, 11))
print(squared)
```

---

# Map Function with a Range Sequence

```python {all|1-2|4-8|10-11|all}
def square(value):
    return value * value

def map(f, sequence):
    result = (  )
    for element in sequence:
        result += ( f(element), )
    return result

squared_range = map(square, range(10))
print(squared_range)
```

---

# Filtering Even Numbers from a Tuple

```python {all|1-4|6-8|all}
def is_even(value):
    if value % 2 == 0:
        return True
    return False

filtered_even = filter(is_even,
    (2, 3, 5, 7, 11))
print(list(filtered_even))
```

<v-clicks>

- Which of these functions is a higher-order function?

- What is the purpose of the `is_even` function?

- What are the benefits of this approach? Why?

</v-clicks>

---

# Filtering Odd Numbers from a Tuple

```python {all|1-4|6-8|all}
def is_odd(value):
    if value % 2 == 1:
        return True
    return False

filtered_odd = filter(is_odd,
    (2, 3, 5, 7, 11))
print(list(filtered_odd))
```

<v-clicks>

- Which of these functions is a higher-order function?

- What is the purpose of the `is_odd` function?

- What are the benefits of this approach? Why?

</v-clicks>

---

# Summations By Using Reduce

```python {all|1-2|4-8|10-11|all}
def plus(number_one, number_two):
    return number_one + number_two

def reduce(f, sequence, initial):
    result = initial
    for value in sequence:
        result = f(result, value)
    return result

numbers = [1, 2, 3, 4, 5]
added_numbers = reduce(plus, numbers, 0)
```

---

# Monoids and Map-Filter-Reduce

<v-clicks>

-   These **higher-order sequence functions** are **independent** and free of
    "side effects" and thus can be **parallelized**

-   Since a **monoid** has the associativity property, can use ` map`, `filter`,
    and `reduce` operators in **parallel** and then combine the solution, often
    achieving a **speedup**. This makes the program more efficient!

-   These three operators give a **vocabulary** for implementing complex
    programs in a **functional** programming style

-   **Parallel** computation is important given the **diminishing** returns
    associated with sequential computation

-   If you can prove that a structure and operation is a **monoid** then you can
    use **map**, **reduce**, and **filter** to **parallelize**  its computations

</v-clicks>

---

# Applying Monoids in Python Programs

<v-clicks>

-   Monoids are frequently used in Python programs

-   Python programs can use higher-order sequence functions

-   Using **monoids** and **higher-order** sequence functions:

    -   **Q1**: What is the difference between a list and a tuple?
    -   **Q2**: How does a monoid generalize strings and integers?
    -   **Q3**: How do higher-order sequence functions use monoids?
    -   **Q4**: How can map-filter-reduce support parallel programming?
    -   **Q5**: What type of speedup will a parallel program achieve?

-   What are the ways in which the mathematical concept of a monoid connects to
a wide variety of **practical applications** in the area of **parallel computing**?

-   How does the concept of a **monoid** create an **archetype** in our minds?

</v-clicks>
