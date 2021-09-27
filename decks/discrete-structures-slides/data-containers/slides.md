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

## Data Containers

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

> How do I use the mathematical concepts of **ordered pairs**, **n-tuples**, and
> **lists** to implement functions with a clearly specified behavior to perform
> tasks like the **input** and **parsing** of a comma separated value (CSV)
> file?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some discrete mathematics and Python
> programming concepts, enabling the investigation of practical applications

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the use of data containers in Python!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Understanding Ordered Pairs

<v-clicks>

-   Mathematical concepts yield predictable programs

-   Understanding the concept of an **ordered pair**:

    -   **Pair**: grouping of two entities

    -   **Ordered**: order of entities matters

    -   **Ordered Pair**: grouping of two entities for which order
        matters

    -   **Coordinate on Earth**: latitude and longitude are an ordered
        pair

    -   **Complex Numbers**: real and imaginary parts are an ordered
        pair

    -   An ordered pair is not the same as a set of two elements! Why?

-   Can we generalize to an ordered grouping beyond two entities? How?

</v-clicks>

[//]: # (Slide End }}})

---

# Practical Applications of Ordered Pairs

<v-clicks>

```
🔍 Times Square
  (40.7580° N, 73.9855° W)
  (40.7580, -73.9855)
🔍 Helsinki, Finland
  (60.1699° N, 24.9384° E)
  (60.1699, 24.9384)
```

- Specified according to the standard `(Latitude, Longitude)`

- Latitude and longitude provide a "global address" for a location

- Why does the order matter for these pairs of location data?

- How do you interpret the **positive** and **negative** numbers?

</v-clicks>

---

# Generalizing Ordered Pairs to n-Tuples

<v-clicks>

-   We could have an "ordered triple" or "ordered quadruple"

-   The n-tuple is the generic name for "tuples" of any size
    -   A 2-tuple is the same as an **ordered pair**
    -   A 3-tuple is the same as an **ordered triple**
    -   A 4-tuple is the same as an **ordered quadruple**
    -   n-tuples contain a **finite** number of entities

-   Write n-tuples with notation like $(1,2)$ or $(x,y,z)$

-   n-tuples enable the **creation of new mathematical objects**

-   While the type of entity in an n-tuple may be different, not every
    entity in the n-tuple must be different. This means that **duplicates are possible**!

</v-clicks>

---

# Defining n-Tuples in Python Programs

```python
pair = 3, 4
quadruple = "Story number", 3,
              "is", true

pair = (3, 4)
quadruple = ("Story number", 3,
              "is", true)
```

- The **same data type** is **not** a **requirement** for a tuple

- What are the **data types** of the values in these tuples?

- Which way is the **best** approach to **describing** these tuples?

---

# Special Tuples in the Python Language

```python
empty_tuple = ()
single_story = ("Story",)
single_number = (3,)
number = (3)
```

- Some tuples may not (yet) contain any data in them!

- Singleton tuples must use the comma notation

- What is the **difference** between a **tuple** and a **number**?
  - Conceptual difference
  - Syntactic difference

- How do we **put data into** and **take data out** of a tuple?

---

# Packing and Unpacking Tuples

```python
# pack a tuple into a variable
pair = (3,4)

# unpack the contents of a tuple
x, y = pair
(x, y) = pair

# unpack and perform simultaneous assignment
x, y = y, x
(x, y) = (y, x)
```

<div class="mt-7">

Wait, what is the purpose of the last two statements? 🤔

</div>

---

# Files in Directories Can Store n-Tuples

<div class="border-2 rounded-2xl border-gray-700 bg-true-gray-300 p-5">

<pre>
tylernelson@gmail.com,Careers adviser
gregory02@medina-mayer.com,"Accountant, management"
jonesmiguel@hotmail.com,Health and safety inspector
rsanchez@yahoo.com,"Surveyor, planning and development"
hillfrank@ward-wood.com,"Scientist, physiological"
aaronhunter@gmail.com,"Surveyor, insurance"
kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer
</pre>

</div>

- Comma separate value (CSV) are frequently used in business!

- Input this file of n-tuples into Python? Lists versus tuples?

---

# Data Storage Containers

<v-clicks>

-   How do you pick between the **different types** of **functions**?

-   Python functions to perform **statistical analysis** of data:

    -   **Q1**: How do you compute the **median** of a list of numbers?

    -   **Q2**: How do you compute the **mode** of a list of numbers?

    -   **Q3**: How do you compute a **frequency table** of a list of
        numbers?

    -   **Q4**: How do you compute the **range** of a list of numbers?

    -   **Q5**: How do you compute the **variance** and **standard deviation**?

-   Can you **translate the mathematical descriptions** of these summary statistics
to **Python programs**? Can you ensure their correctness with testing?

</v-clicks>
