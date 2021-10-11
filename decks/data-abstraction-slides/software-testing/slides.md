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

## Software Testing

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

> How can I use the processes of software testing and debugging to establish a
> confidence in the correctness of a Python program?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of software testing and
> debugging so as to implement test suites, using Pytest, for programs that find
> bugs and establish a confidence in correctness.


</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the practice of software testing!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are foundations of testing and debugging?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Testing: run a program to try to see if it works
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Debugging: fix a program that is currently broken
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Design for testability ensures testing is possible
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Software Testing in Python

<v-clicks>

-   Python program must be in an **executable state**!

-   Python source code must be **free** of **syntactical errors**

-   Python source code must be **free** of **static semantic errors**

- Key insights about software testing in Python:

    - Purpose of testing is to show that **bugs exists**

    - Testing **cannot prove** the **absence of defects**

    - **Exhaustive testing** of trivial functions is **not possible**

    - A **test suite** is a collection of useful program inputs

    - **Partition testing** divides the input space into groups

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are key strategies for software testing?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Keys: What is the focus? <em>and</em> What is the scope?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Closed-box testing focuses on the specification
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Glass-box testing focuses on the source code
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

# Investigating Software Testing

<div class = "mt-10">
</div>

<v-clicks>

-   Correct use of program components in Python programs:

    -   **Q1**: What are the benefits of **recursive** functions?

    -   **Q2**: What are the different ways to implement **Fibonacci**?

    -   **Q3**: What are the **trade-offs** of function choices?

    -   **Q4**: What the benefits of using program **modules**?

    -   **Q5**: How to external **packages** aid Python programmers?

-   Balance the **trade-offs** associated with different functions!

-   Judiciously use **external** program modules when programming

</v-clicks>

[//]: # (Slide End }}})
