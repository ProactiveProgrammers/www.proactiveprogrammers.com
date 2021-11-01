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

<div class="flex row mt-3">

<uim-rocket class="text-6xl ml-9 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-8">
Let's investigate sets in Sympy!
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

-   Investigate probability after an alternative approach to sets

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


