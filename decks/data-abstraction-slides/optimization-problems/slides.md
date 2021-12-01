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

## Optimization Problems

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

> How can I use algorithms to efficiently solve an optimization problem
> characterized by an objective function and a set of constraints?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the algorithmic strategies (e.g., greedy
> and dynamic programming) for solving optimization problems that maximize or
> minimize an objective function subject to constraints.

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the topic of optimization problems!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Characteristics of optimization problems?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
An objective function to maximize or minimize
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Set of constraints that any solution must satisfy
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-columns class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Solving with efficiency and effectiveness trade-offs
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Optimization for Knapsack Problems

<v-clicks>

- Imagine you are a thief who wants to steal items in the following fashion:

  - Pick items so that you maximize the value of all stolen items
  - Ensure that you do not steal more items that you can carry
  - Don't get caught ... but, we won't model this in the algorithm! 😉

- An instance of the **knapsack problem** can be described as:

  - The set of items: $I = \{I_1, \ldots, I_n\}$
  - The set of weights for each item: $W = \{W_1, \ldots, W_n\}$
  - The set of benefits for each item: $B = \{B_1, \ldots, B_n\}$
  - The maximum weight for storing items: $M$

- The thief wants to maximize the benefit without taking more items than will
fit in their "knapsack". How can the thief **efficiently** and **effectively** pick
items?

</v-clicks>

[//]: # (Slide End }}})

---

# Instance of the Knapsack Problem

<v-clicks>

| **Item** | **Value** | **Weight** | **Value/Weight** |
|------ |-------|--------|--------------|
| Clock | 175   | 10     | 17.5         |
| Painting | 90 | 9      | 10           |
| Radio | 20 | 4      | 5           |
| Vase | 50 | 2      | 25           |
| Book | 10 | 1      | 10           |
| Computer | 200 | 20      | 10           |

- If you were a thief what would you steal? Why?

- What are different strategies for stealing items?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Greedy Algorithms for Knapsack

<v-clicks>

- Greedy algorithms find an **approximate** solution to the knapsack problem:

  - Pick an **objective function** that will guide what you steal

  - There are many objective functions to consider! Let's start with:

    - **Benefit-driven**: Best item according to the **value**
    - **Cost-driven**: Best item according to the **weight**
    - **Density-driven**: Best item according to the **value/weight**
    - Continue to select items until reaching the knapsack's limit

- Which of these objective functions yields the highest **payout**? Why?

- Are these objective functions **guaranteed** to produce the best result? **No**!

- What are the **benefits** and **limitations** of greedy algorithms for
knapsack?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Strategies for optimizing the knapsack problem?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Pick items with the biggest payout
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Pick items with the least weight
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Pick items with best value for their weight
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Output from a Greedy Knapsack Solver

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
Use greedy-by-value to fill a knapsack of size 20:
Total value of items taken is 200.0
  (computer, 200, 20)

Use greedy-by-weight to fill a knapsack of size 20:
Total value of items taken is 170.0
  (book, 10, 1)
  (vase, 50, 2)
  (radio, 20, 4)
  (painting, 90, 9)

Use greedy-by-density to fill a knapsack of size 20:
Total value of items taken is 255.0
  (vase, 50, 2)
  (clock, 175, 10)
  (book, 10, 1)
  (radio, 20, 4)
</pre>

</div>

<div class="mt-5">
</div>

- Can you explain **why** the program produced this output?
- How does **sorting** play a role in solving a Knapsack problem?

[//]: # (Slide End }}})
