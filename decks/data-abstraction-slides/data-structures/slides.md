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

## Data Structures

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

<div v-click>

## Key Question

> How can I implement, use, and test data structures that support efficient data
> processing with searching and sorting algorithms?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the characteristics of key data structures
> (e.g., a list and a hash table) so that they can serve as the input and output
> for searching and sorting algorithms?

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the topic of data structures!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are some common data structures?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Dynamic arrays that grow (and shrink) in size
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Linked lists that are comprised of nodes and edges
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Hash tables that employ a function and backing list
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<style>
  li {
  font-size: 34px;
  margin-bottom: 1px;
  }
</style>

<div class="flex row">

<uim-vector-square class="text-8xl ml-4 mt-12 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-5">
Data structures
</div>

<div class="text-6xl text-true-gray-600 font-bold mt-16 mr-15">
<ul>
<li>Array</li>
<li>Lists</li>
<li>Dictionary</li>
</ul>
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-flip-v class="text-9xl ml-4 mt-6 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-5">
Processing algorithms
</div>

<div class="text-8xl text-true-gray-600 font-bold mt-16 mr-15">
<ul>
<li>Searching</li>
<li>Sorting</li>
<li>Storage</li>
</ul>
</div>

</div>

</v-clicks>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-0 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Connecting data containers and data processing?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Understanding Algorithmic Complexity

<v-clicks>

- Empirical evaluation of an algorithm depends on:

    - The speed of the computer on which it is run
    - The efficiency of the Python implementation on the computer
    - The chosen values for the input to the algorithm

- **Random access machine** model of computation assumes that steps are run
sequentially, one at a time. Why is this not realistic? Acceptable?

- Characterize the performance of an algorithm as input size increases:

    - **Best-Case**: minimum running time over all possible inputs
      of a given size
    - **Worst-Case**: minimum running time over all possible inputs
      of a given size
    - **Average-Case**: average (or, expected) running time over
      all possible inputs of a given size

- **Asymptotic Notation**: relationship between the
   running time of an algorithm and the size of its inputs, focusing on
   situation when input is large

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Reviewing Algorithmic Complexity

<v-clicks>

- Computer program performance is very important:

    - If a program is too slow in may not met our goals
    - Slow computer programs also present security concerns
    - Sometimes a computation may prove to be infeasible

-   Understanding algorithmic complexity:

    -   **Q1**: What are the **benefits** of empirical studies?

    -   **Q2**: What are the **limitations** of empirical studies?

    -   **Q3**: What are the **trade-offs** associated with analytical evaluation?

    -   **Q4**: How do you conduct a **doubling experiment** to study performance?

    -   **Q5**: What are the **trade-offs** between time and space overhead?

</v-clicks>

[//]: # (Slide End }}})
