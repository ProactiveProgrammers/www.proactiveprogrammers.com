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

## Object-Oriented Programming

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

> How do I use the concept of a relation and the industrially relevant practice
> of object-oriented programming to correctly implement Python programs that
> are easy to understand and maintain?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **objects**
> and to learn different ways to represent and use objects in Python

</div>

<v-click>

<div class="flex row mt-0 ml-0">

<uim-rocket class="text-6xl ml-5 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-10">
Let's create objects in Python programs!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

# Mathematical Concept of a Relation

-   As first introduced in Chapter 1, a relation is a connection between
    two or more entities (e.g., sets or ordered pairs)

-   Understanding relations in discrete mathematics:

    -   **Binary relation**: set of ordered pairs
    -   **Ternary relation**: set of ordered triples
    -   **Quaternary relation**: set of ordered quadruples
    -   **n-ary relation**: set of ordered n-tuples

-   First, think about the number of related elements

-   Consider the relationship between the elements as well

-   How do I create and use relations in Python? Dictionary? List? Object?

-   How can object-oriented programming express entity relationships?

---

# Using Ordered Pairs in Python

```python
def factorial_iterative(number):
    factorial_list = []
    value = 1
    factorial_value = 1
    values = list(range(1, number + 1))
    for value in values:
        factorial_value = factorial_value * value
        factorial_list.
           append((value, factorial_value))
    return ((value, factorial_value),
           factorial_list)
```

---

# Understanding `factorial_iterative`

- What are the inputs and outputs of this function?

  -   **Input**: `number: int`

  -   **First Output**: `Tuple[int, int]`

  -   **Second Output**: `List[Tuple[int, int]]`

-   The two return values are also combined in a `Tuple`!

-   Recall `Tuple[int, int]` is Pythonic for an ordered pair

-   What is the need for such a complicated return value?

-   What is the best way to represent relationships in Python?

-   The tuple does not offer **semantic meaning** for return value
