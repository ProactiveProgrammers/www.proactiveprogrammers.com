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

## Mathematical Objects

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

> How do I use the concepts associated with object-oriented programming to
> create and use objects for the purposes of performing mathematical
>  computations like the moving average?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **objects**
> and to learn different ways to use them in mathematical computations

</div>

<v-click>

<div class="flex row mt-0 ml-0">

<uim-rocket class="text-6xl ml-5 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-10">
Let's create objects to aid mathematics!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Foundations of object-oriented programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-package class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Classes are templates for objects
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-package class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Objects contain state in variables
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-package class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Objects feature behavior with methods
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Inheritance and Encapsulation

<v-clicks>

- Inheritance enables creation of **parent-child** relationships

- Inheritance forms an **"is a"** relationship between two classes

- Benefits of inheritance in object-oriented programming:

    - Define **specialized behaviors** in the sub-classes

    - Promote **code reuse** since child can access parent's methods

    - Promote **data sharing** since child can access parent's variables

    - Model object-oriented relationships that **mirror reality**

- Encapsulation **protects** the **state** of an object, well sorta 😉

- What are the **benefits** and **drawbacks** of object-oriented programming?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Benefits of inheritance and encapsulation?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Inheritance supports code reuse and data sharing
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Inheritance allows modelling of real-world entities
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Encapsulation calls for state change with methods
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Methods in object-oriented programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Methods define a behavior for instances of class
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Methods accept input and produce output
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
The <code>self</code> parameter is always a method's input
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Key benefits of object-oriented programming?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Combines behavior with the storage of state
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports the modelling of real-world entities
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
But, it sometimes feels more "complex" in Python!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Case Study: Moving Average of Values

<v-clicks>

- Many streaming systems produce a never-ending sequence of values

- **Challenge**: how to average these values in space-efficient fashion?

- Approach to computing the **moving average** of a list of values:

    - Define the `__init__` method as the constructor

    - Define the `append` method to add data to `MovingAverage`

    - Define the `value` method to compute a running total

    - Define a `smooth` function for a `window` of data

- **Question**: what are the trade-offs associated with `window` ?

- What are the **benefits** and **drawbacks** of this mathematical object?

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's use objects for mathematics!
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
Find the <code>mathematical-objects/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-mathematical-objects.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})
