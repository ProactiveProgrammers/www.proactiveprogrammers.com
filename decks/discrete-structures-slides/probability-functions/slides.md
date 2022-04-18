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

## Probability Functions

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

> How do I use the implementation of a finite set in `Sympy` to create
> Python programs that calculate and use probabilities?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **set**, as
> implemented in `Sympy`, supporting the calculation of probabilities

</div>

<v-click>

<div class="flex row mt-3 ml-2">

<uim-rocket class="text-6xl ml-0 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-8">
Let's study sets and probability in Sympy!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

# Mathematical Sets in Python Programs

<v-clicks>

-   Set theory is useful in mathematics and computer science

-   The `Sympy` package gives an implementation of finite sets

    -   Remember, sets are "containers" for other elements

    -   The sets in Sympy are finite sets, called `FiniteSet`

    -   These sets have the same properties as built-in sets

    -   `FiniteSet` has a few features not provided by `set`

    -   A probability is the likelihood that an event will occur

    -   We can use either `set` or `FiniteSet` to study probabilities

-   Investigate probability after exploring an alternative approach to sets

</v-clicks>

---

# Using Python to Create a Finite Set

```python
empty_set = FiniteSet()
print(empty_set)

finite_set = FiniteSet(2, 4, 6, 8, 10)
print(finite_set)
```

<v-clicks>

- Only works in you have installed and imported `sympy` !

- What is the output of this `print` statements in this program?

- Are there other ways to create a `FiniteSet` ?

- What operations can we perform with a `FiniteSet` ?

</v-clicks>

---

# Creating a Set from a List or Tuple

```python
list = [2, 4, 6, 8, 10]
finite_set = FiniteSet(*list)
print(finite_set)

tuple = (2, 4, 6, 8, 10)
finite_set = FiniteSet(*tuple)
print(finite_set)
```

<v-clicks>

- All approaches call the `FiniteSet` constructor

- Can construct a `FiniteSet` out of a list or a tuple

- What is the purpose of the `*` in this program?

</v-clicks>

---

# Output of Finite Set Creation Program

```python
# Explicit FiniteSet:
FiniteSet(2, 4, 6, 8, 10)

# Empty FiniteSet:
EmptySet

# FiniteSet from Tuple:
FiniteSet(2, 4, 6, 8, 10)

# FiniteSet Containing Tuple:
FiniteSet((2, 4, 6, 8, 10))
```

---

# Math and Programming Differences

<v-clicks>

-   Programmers **cannot** use sets like mathematicians do!

-   Python programs **cannot** store an infinite set

-   Finite sets must **fit** into a computer's **finite** memory

-   Programs need a **procedure** for **constructing** the set

-   Different programming languages and packages have other restrictions. For
instance, recall that Python programs **cannot** create sets that **contain
mutable elements** like lists! Why do you think that this is the case?

-   So, what are the **benefits** of using sets in Python programs?

-   Importantly, sets come with some **super-useful** default operations!

-   Thankfully, `sympy` contains even more basic operations! 👍

</v-clicks>

---

# Using Finite Sets in Sympy

```python
from sympy import FiniteSet

list = [1, 2, 3, 2]
finite_set = FiniteSet(*list)
print(finite_set)

for element in finite_set:
    print(element)
```

<v-clicks>

- What is the output of `print(finite_set)` ?

- What is the output of `print(element)` in the `for` loop?

- How do these two output segments differ?

</v-clicks>

---

# Subset Relationships with Finite Sets

```python
one = FiniteSet(1, 2, 3)
two = FiniteSet(1, 2, 3)

subset = one.is_proper_subset(two)
print(subset)
subset = two.is_proper_subset(one)
print(subset)
```

<v-clicks>

- What is the mathematical definition of a **proper subset**?

- What is the purpose of the `is_proper_subset` function?

- What is the output of the `print(subset)` function calls?

</v-clicks>

---

# Subsets with Finite Sets ♻

```python
one = FiniteSet(1, 2, 3)
three = FiniteSet(1, 2, 3, 4)

subset = one.is_proper_subset(three)
print(subset)
subset = three.is_proper_subset(one)
print(subset)
```

<v-clicks>

- Is `one` a proper subset of `three` ?

- Is `three` a proper subset of `one` ?

- What is the output of the `print(subset)` ?

</v-clicks>

---

# Program Output for Subset in Sympy

```python
# Set one proper subset set two:
False

# Set two proper subset set one:
False

# Set one proper subset set three:
True

# Set three proper subset set one:
False
```

---

# Union and Intersection with Finite Sets

```python
one = FiniteSet(1, 2, 3)
two = FiniteSet(1, 2, 3, 4)

union = one.union(two)
print(union)

intersection = one.intersection(two)
print(intersection)
```

<v-clicks>

- What is the meaning of `one.union(two)` ?

- What is the meaning of `one.intersection(two)` ?


</v-clicks>

---

# Output of a Set Intersection Program

```python
# Union:
FiniteSet(1, 2, 3, 4)

# Intersection:
FiniteSet(1, 2, 3)
```

<div class="mt-10">

<v-clicks>

- Would `set` produce the same output?

- Any questions about operations with `FiniteSet` ?

- A **probability** is the likelihood of an event's occurrence

- How can we use `FiniteSet` s for probability?

</v-clicks>

</div>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of using Sympy's sets?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Offer the same operations as the built-in sets
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Provide additional set-theoretic operations
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>FiniteSet</code> is immutable and <code>set</code> is not
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Using Set Theory to Explore Probability

<v-clicks>

-   Often it is difficult to calculate the **probability** of an event!

-   Sets help us reason about the basic concepts of probability

-   Fundamental definitions in the context of probability:

    -   **Experiment**: the check that we want to perform and understand
    -   **Sample Space**: all possible outputs of the chosen experiment
    -   **Event**: the set of outcomes for which we calculate a
        probability
    -   **Probability**: the likelihood that a specified event will
        occur
    -   **Uniform Distribution**: all outcomes are equally likely to
        occur

-   The **probability** of an event $E$ is $P(E) = |E| / |S| \in [0,1]$

-   The notation $|E|$ denotes the **cardinality** of the event set

-   For all events $E$ a greater $P(E)$ means that $E$ is more likely

</v-clicks>

---

# Probability Calculation with `FiniteSet`

```python
def probability(space, event):
    return len(event) / len(space)

six_sided = {*[1, 2, 3, 4, 5, 6]}
three = {*[3]}

roll_three = probability(six_sided,
                         three)
```

- The `probability` function calculates event likelihood

- Would the built-in `set` produce the same output? Yes!

---

# Probability of Event A or Event B

```python
six_sided = FiniteSet(1, 2, 3, 4, 5, 6)
roll_one = FiniteSet(2, 3, 5)
roll_two = FiniteSet(1, 3, 5)

event = roll_one.union(roll_two)
prob = len(event) / len(six_sided)
print(prob)
```

<v-clicks>

- The `union` function connects to a logical `or` operation

- The output of this program is ` 0.6666666666666666`. Why?

- Could also make a direct call to the `probability` function!

</v-clicks>

---

# Probability of Event A and Event B

```python
six_sided = FiniteSet(1, 2, 3, 4, 5, 6)
roll_one = FiniteSet(2, 3, 5)
roll_two = FiniteSet(1, 3, 5)

event = roll_one.intersect(roll_two)
prob = len(event) / len(six_sided)
print(prob)
```

<v-clicks>

- The `intersect` function connects to a logical `and` operation

- The output of this program is ` 0.3333333333333333`. Why?

- Could also make a direct call to the `probability` function!

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's use functions to compute probabilities!
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
<code>discrete-structures/probability-functions/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-probability-with-sets.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How to calculate a probability with sets?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Create a set for the entire sample space
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Create a set for the specific event
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Calculate ratio <code>len(event) / len(sample)</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Practical applications of probability functions?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-chart-pie class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Estimate the likelihood of house price increasing
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-chart-pie class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Estimate the likelihood of the spread of disease
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-chart-pie class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Determine likelihood of winning an online game
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

# Logical `and` in Square Root

<div class="ml-1">

```python {all|1|2|3-4|5-7|8|9-11|all}
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1
print(f"Guessed {num_guesses} times")
if abs(ans**2 - x) >= epsilon:
    print(f"Could not find sqrt of {x}")
else:
    print(f"{ans} is close to sqrt of {x}")
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How to understand logical operators?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Each operator accepts two or more operands
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Logical <code>and</code> requires both <code>True</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Logical <code>or</code> requires at least one <code>True</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Truth Tables for Logical Operators

```
+-------+-------+-----------+----------+
|   p   |   q   |  p and q  |  p or q  |
|-------+-------+-----------+----------+
| True  | True  |   True    |   True   |
| True  | False |   False   |   True   |
| False | True  |   False   |   True   |
| False | False |   False   |  False   |
+-------+-------+-----------+----------+
```

<v-clicks>

- The `p` and `q` are logical clauses with a distinct truth value

- The table includes all possible combinations of `True` and `False`

- Shows possible outcomes for both logical operators

</v-clicks>

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of using logical operators?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Control the behavior of a program
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Influence the calculation of a probability
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Truth tables summarize all possible outcomes
</div>

</div>

</div>

[//]: # (Slide End }}})

---

# Finite Sets in Programs with Sympy

-   Sets are a discrete structure with many practical benefits!

-   Options: `set` and `FrozenSet` and `FiniteSet` in sympy

-   Using finite sets and probability in Python programs:

    -   **Q1**: What are the **characteristics** of an infinite set? Finite
        set?

    -   **Q2**: What are the **built-in operations** provided by a finite
        set?

    -   **Q3**: How does the `sympy` package support set programming?

    -   **Q4**: How does the use of sets support **probability**
        calculations?

    -   **Q5**: How can **Venn diagrams** help to visualize set
        relationships?

-   See <https://doingmathwithpython.github.io/> for more details
