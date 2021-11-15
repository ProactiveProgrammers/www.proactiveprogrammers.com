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

## Mathematical Mappings

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

> How do I use dictionaries, tuples, and lists to correctly implement efficient
> mathematical functions in Python?


</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **mappings**, as
> implemented with, for instance, a function or a dictionary

</div>

<v-click>

<div class="flex row mt-3 ml-2">

<uim-rocket class="text-6xl ml-10 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-10">
Let's implement mappings in Python!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

# Concept of a Mathematical Mapping

<v-clicks>

-   As first introduced in Chapter 1, a **mapping** is a set of ordered
    pairs in which no two have the same first element

-   Implementing **functions** in the Python language:

    -   Functions can accept zero or more inputs
    -   Functions can produce zero or more outputs
    -   Higher-order functions can accept and produce functions
    -   One function's input can become another function's output
    -   Imperative or declarative specification of functions
    -   Discrete structures normally have a "function interface"

-   It is possible to implement a function in **many different** ways! How do we
decide which approach is the best? Expressiveness? Speed? Other ways?

- Efficient and clear programs needs **multiple** discrete structures and mappings

</v-clicks>

---
