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

# Understanding Ordered Pairs

<v-clicks>

-   Mathematical concepts yield predictable programs

-   Understanding the concept of an **ordered pair**:

    -   **Pair**: grouping of two entities

    -   **Ordered**: order of entities matters

    -   **Ordered Pair**: grouping of two entities for which order
        matters

    -   **Coordinate on Earth**: latitude and longitude are an ordered
        pair

    -   **Complex Numbers**: real and imaginary parts are an ordered
        pair

    -   An ordered pair is not the same as a set of two elements! Why?

-   Can we generalize to an ordered grouping beyond two entities? How?

</v-clicks>

[//]: # (Slide End }}})

---

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
