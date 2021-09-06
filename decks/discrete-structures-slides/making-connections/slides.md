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

## Making Connections

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

<br>

<div v-click>

## Key Question

> How do I connect **mathematical terminology**  (e.g., *mapping*, *function*,
> *number*, *sequence*, and *set*), to the implementation of **Python
> programs** that declare and call functions and declare and manipulate
> variables?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some discrete mathematics and Python
> programming concepts, setting the stage for exploring of discrete structures.

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Discrete Structures = Math + Code

<v-clicks>

-   **Discrete mathematics**: symbols, character strings, truth values,
objects, and collections of these entities stored in, for instance, sets or
tuples

-   Specifying and designing a **computer program**:

    -   Describe input, output, and internal objects
    -   Use the vocabulary of discrete mathematics
    -   Implement and test the program in a language

- **Our goal**: implement a program $P$ that meets a specification $S$

</v-clicks>

<div v-click>

<div class="flex row -mt-5">

<mdi-help-box class="text-9xl ml-8 mt-4 text-blue-600" />

<div class="text-4xl font-bold mt-13 ml-4">
What is beneficial about combining mathematics and computer programming?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Program that Analyzes Web Pages

-   **Informal specification**: Read two web pages and then find and output
    all of the URLs that appear in them both

-   Different approaches to implementing this program

    -   **Informal** and **intuitive** specification

    -   **Natural language specification** using **discrete structures**

    -   Which one is shorter? \... clearer? \... unambiguous?

-   The language of mathematics helps us to describe and implement a program
that is correct, efficient, clearly documented, and maintainable!

<div v-click>

<div class="flex row -mt-4">

<mdi-help-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="text-4xl font-bold mt-7 ml-4">
What is challenging about this specification?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)


<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is difficult about using discrete structures?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
What is the meaning of the term <code>set</code> ?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
How do you perform <code>set insertion</code> ?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
How do you perform <code>set intersection</code> ?
</div>

</div>

</div>

[//]: # (Slide End }}})
