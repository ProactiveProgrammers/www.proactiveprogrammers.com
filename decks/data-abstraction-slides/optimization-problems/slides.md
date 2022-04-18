---
# use the default theme
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# define the colorSchema and the highlighter
highlighter: prism
colorSchema: light
remoteAssets: false
# show line numbers in code blocks
lineNumbers: false
# define the fonts and their weights
fonts:
  # define the font for the body text
  sans: 'IBM Plex Sans'
  # define the serif font
  serif: 'IBM Plex Serif'
  # define the code font
  mono: 'IBM Plex Mono'
  # load several font weights
  weights: '200,400,500'
  # support the use of italics
  italic: true
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

</v-clicks>

<br>

<v-clicks>

- If you were a thief what would you steal? Why?
- What are different strategies for stealing items?
- Can you tell if one strategy was better than another?
- How would you execute a stealing strategy?

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

<v-clicks>

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

</v-clicks>

<div class="mt-5">
</div>

<v-clicks>

- Can you explain **why** the program produced this output?
- How does **sorting** play a role in solving a knapsack instance?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Implementing a Greedy Algorithm

<v-clicks>

- Store the table itself as a **CSV file** that can be **input** and **parsed**

- Each row of the table is an `Item` with a value, weight, and density

- After the input and parsing of the table, create a `List` of `Item` s

- Use Python's built-in `sorted` function to sort this `List`:

  - Use the `reverse = True` flag so that we have biggest values first

  - Use the `key` parameter to specify how the sorting happen

  - Remember, we will sorting according to value, weight, or density!

- After sorting, iteratively pick values from list until reaching maximum
weight

- The worst-case time complexity is $O(n + n \times log_2 n)$ or $O(n \times
log_2n)$

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Benefits of greedy optimization methods?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Easy to represent the problem
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Easy to implement the solution
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Good worst-case time complexity
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Drawbacks of greedy optimization methods?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Does not yield provably optimal solution
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram  class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Heuristics produce results of varying quality
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Always makes decisions that are locally optimal
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Alternatives to Greedy Algorithms

<v-clicks>

- Genetic algorithms **evolve** a solution to an optimization problem:

  - Representation of an individual in a population
  - Fitness function that describes quality of solution
  - Crossover operator that combines individuals
  - Mutation operator that modify individuals
  - Iteration approach that runs the genetic algorithm

- Genetic algorithms perform a **global** optimization but are also **heuristic**

- Is there an algorithm that will guarantee the correct answer? Yes!

- **Exhaustive enumeration** will **always** find the **correct** solution to knapsack:

  - Generate all subsets of the set of items in the set $I$
  - Remove all combinations with a weight above the maximum
  - Chose the combination with the maximum weight from those that remain

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Optimal Knapsack Solving

<v-clicks>

- Generating all subsets of a set is an **expensive** algorithm for large sets

- Process involves listing all singleton sets like {Clock} and {Painting}

- Then algorithm must generate all sets with two elements like {Vase, Book}

- This process will continue for all possible subsets of items

- The algorithm then removes all subsets with a weight greater than $M$

- Among those subsets that remain, it must evaluate its overall quality

- What is the worst-case time complexity of this approach?

  - For a set $S$ with $|S| = n$, the powerset contains $2^n$ subsets
  - In the worst case it must calculate the quality of each of these subsets
  - Overall, the algorithm has a worst-case time complexity of $O(n \times 2 ^n)$

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Drawbacks of the exhaustive algorithm?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Powerset contains exponential number of elements
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram  class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Every subset must be checked in the worst case
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Extreme costs limits the feasible problem size
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Output from Exhaustive Solver

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

<v-clicks>

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5 mb-5">

<pre>
Use exhaustive enumeration to fill a knapsack of size 20:
Total value of items taken is 275.0
  (clock, 175, 10)
  (painting, 90, 9)
  (book, 10, 1)
</pre>

</div>

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5">

<pre>
Use greedy-by-value to fill a knapsack of size 20:
Total value of items taken is 200.0

Use greedy-by-weight to fill a knapsack of size 20:
Total value of items taken is 170.0

Use greedy-by-density to fill a knapsack of size 20:
Total value of items taken is 255.0
</pre>

</div>

</v-clicks>

<div class="mt-5">
</div>

<v-clicks>

- Exhaustive enumeration produces the **highest quality** solution!
- For large-scale problem instances exhaustive solving is **infeasible**

</v-clicks>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What about fractional knapsack problem?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Allows for items to be infinitely divisible
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Take as much of an item according to density
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Greedy algorithm is guaranteed to be optimal
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Intuitions about Dynamic Programming

<v-clicks>

- Dynamic programming efficiently solves problems when they have:

  - **Optimal substructure**: globally optimal solutions can be found by
  combining optimal solutions to subproblems, suggesting break down

  - **Overlapping subproblems**: creating an optimal solution involves solving
  the same problem many times, suggesting to store solutions

- Instance of the 0/1 Knapsack problem exhibit **both** of these characteristics!

- There are two main implementation strategies for dynamic programming:

  - **Memoization** solves the original problem in a **top-down** fashion,
  storing the solution to each subproblem in a table and looking there first
  next time is solves a subproblem
  - **Tabular** solves the problem in a **bottom-up** fashion, starting
  with small problems and storing their solution in a table, combining them
  when solving next smallest problems

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How can we implement memoization in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-archive-search class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Table stores previously computed values
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-archive-search class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Return previously computed value if available
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-archive-search class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Use the <code>@functools.lru_cache</code> decorator!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using an LRU Cache for Memoization

```python
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

<v-clicks>

- LRU cache has a `maxsize` that defines how many mappings it will store

- It discards the least recently used mapping after reaching `maxsize`

- This approach **improves time** efficiency while accepting **increased storage**

</v-clicks>

---

[//]: # (Slide Start {{{)

# Knapsack with Dynamic Programming

<v-clicks>

- Use a `memo` variable to keep track of previous solutions to subproblems

- Explores subproblems systematically but always first checks the `memo`

- Every time a new subproblem is solved, the `memo` stores a record of it

- Declare the `memo` variable to be a dictionary:

  - The key for the dictionary is the current subproblem
  - The value for the dictionary is the subproblem's solution
  - Storing and searching the dictionary is done efficiently

- Refer to Figure 15-8 for a table of performance results for dynamic
programming! Note that the **number of calls** does not grow exponentially!

- Dynamic programming is **faster** than exponential but requires **large** tables

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Trade-offs for dynamic programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-swap-horizontal-variant class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
More effective solver than greedy algorithms
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-swap-horizontal-variant class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Significantly faster than exhaustive enumeration
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-swap-horizontal-variant class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Requires extra memory for the memoization table
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Solving Optimization Problems

- Solving an optimization problem requires finding a solution that **maximizes**
or **minimizes** and objective while meeting all solution **constraints**

- Different strategies for solving an optimization problem like 0/1 knapsack

- Trade-offs in terms of effectiveness and both time and space efficiency

- Strategies for solving the 0/1 knapsack problem:

    -   **Q1**: What are three different greedy strategies and how do they work?
    -   **Q2**: What are the benefits and drawbacks of exhaustive enumeration?
    -   **Q3**: Can a greedy algorithm solve the fractional knapsack problem?
    Why?
    -   **Q4**: How does dynamic programming solve the 0/1 knapsack problem?
    -   **Q5**: How would you conduct an experiment to evaluate different solvers?

- We will explore an **implementation** of a solution in an upcoming session!
