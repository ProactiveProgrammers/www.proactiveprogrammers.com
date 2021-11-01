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

## Algorithmic Complexity

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

> How can I implement more efficient Python programs by conducting both an
> analytical and an empirical evaluation of the performance of an algorithm?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of the analytical and
> empirical evaluation of an algorithm, helping you characterize, understand,
> and improve the performance of a Python program

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the topic of algorithmic complexity!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Benefits of performance and correctness?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Correctness is of paramount importance
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Fast programs are not helpful if broken
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Program performance is critically important
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

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-4">
Analytical Evaluation
</div>

<div class="text-6xl text-true-gray-600 font-bold mt-16 mr-15">
<ul>
<li> Algorithm </li>
<li> Constructs </li>
<li> Growth </li>
</ul>
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-microscope class="text-9xl ml-4 mt-6 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-1">
Experimental Evaluation
</div>

<div class="text-8xl text-true-gray-600 font-bold mt-16 mr-14">
<ul>
<li> Program </li>
<li> Benchmark </li>
<li> Study </li>
</ul>
</div>

</div>

</v-clicks>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-4 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
What are the trade-offs of these two approaches?
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

<div class="ml-8 grid grid-cols-2 gap-19 mt-3">
<div>

# Analytical

<style>
  li {
  font-size: 22px;
  margin-bottom: 10px;
  }
</style>

- Provides a clear means by which to compare programs
- Does not depend on the hardware or software configuration
- Yet, often requires precise mathematical reasoning skills

</div>

<div v-click>

<div>

# Experimental

- Must generate inputs to the program subject to experiments
- Must repeatedly run a program and collect performance data
- Only generally accessible to programmers if good tools exist

</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-scenery class="text-6xl ml-2 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
Analysis characterizes an algorithm as, say, O(n)
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-grid class="text-6xl ml-2 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
Experiments run program to collect performance data
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How to analytically evaluate a program's performance?
</div>

</div>

<div v-click>

<div class="flex row -ml-4">

<uim-repeat class="text-6xl ml-4 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Commonly used growth functions
</div>

</div>

</div>

<div v-click>

<div class="flex row -ml-4">

<uim-layer-group class="text-6xl ml-4 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Study program's code constructs
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# "Fast" Order of Growth Functions

<style>
  .constraint {
    width: 100%;
  }
</style>

<br>

<div class="constraint -mt-17">

![Fast Order of Growth Functions](/fast-growth-functions.png)

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# "Slow" Order of Growth Functions

<style>
  .constraint {
    width: 100%;
  }
</style>

<br>

<div class="constraint -mt-17">

![Slow Order of Growth Functions](/slow-growth-functions.png)

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Relationship between growth function and program's performance?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Slow growth functions → fast programs
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-exclamation-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Fast growth functions → slow programs
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Which type of algorithm and computer pairing would you prefer?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-help-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Slow growth functions + slow computer
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-help-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Fast growth functions + fast computer
</div>

</div>

</div>

[//]: # (Slide End }}})
