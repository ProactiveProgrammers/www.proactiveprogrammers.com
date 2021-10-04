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
> clearly specified behavior to perform tasks like finding a name in a
> file or computing the arithmetic mean of data values?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some the concept of a **monoid**, seeing
> how it connects to practical applications with strings and sequences

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

# Motivating the Monoid

<v-clicks>

-   Wow, **strings** and **integers** have **similar** properties!

-   The integers and the mathematical operation of "$+$":

    -   Adding two integers results in another integer

    -   Addition of integers adheres to the associative property

    -   Addition has an identity of $0$ because $0 + n = n + 0$

    -   Key question: are integers and strings of the same general type?

-   **Monoid**: A set that has an **associative binary operator** and an
    **identity element**. Can we explain this more formally?

-   If we know that a discrete structure used in a Python program is a
    monoid then we can understand, predict, and test its behavior!

</v-clicks>

---

# Using n-Tuples and Lists in Python

<v-clicks>

-   **n-tuples** and **lists** are frequently used in Python programs

-   Python programs can use **CSV files** and **databases**

-   Using n-tuples inside of a Python program:

    -   **Q1**: What is the difference between a **list** and a **tuple**?

    -   **Q2**: How do you **read** a CSV file from the file system?

    -   **Q3**: How do you **parse** a CSV file encoded in a string?

    -   **Q4**: How do you handle the **intricacies** of real-world CSV
        files?

    -   **Q5**: How can a Python program **use** a **relational database**?

-   Connections for n-tuple and applications in computing, business, and
science?

</v-clicks>
