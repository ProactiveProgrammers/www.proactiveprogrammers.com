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

## Mathematical Mappings

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

> How do I use dictionaries, tuples, and lists to correctly implement efficient
> mathematical functions in Python?


</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **mappings**, as
> implemented with, for instance, a function or a dictionary

</div>

<v-click>

<div class="flex row mt-3 ml-2">

<uim-rocket class="text-6xl ml-10 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-10">
Let's implement mappings in Python!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

# Concept of a Mathematical Mapping

<v-clicks>

-   As first introduced in Chapter 1, a **mapping** is a set of ordered
    pairs in which no two have the same first element

-   Implementing **functions** in the Python language:

    -   Functions can accept zero or more inputs
    -   Functions can produce zero or more outputs
    -   Higher-order functions can accept and produce functions
    -   One function's input can become another function's output
    -   Imperative or declarative specification of functions
    -   Discrete structures normally have a "function interface"

-   It is possible to implement a function in **many different** ways! How do we
decide which approach is the best? Expressiveness? Speed? Other ways?

- Efficient and clear programs needs **multiple** discrete structures and mappings

</v-clicks>

---

# Understanding the Fibonacci Function

```python
def fibonacci(number: int) -> Tuple[int]:
    result = ()
    a = 1
    b = 1
    for i in range(number):
        result += (a,)
        a, b = b, a + b
    return result
```

<v-clicks>

- What are the inputs and outputs of this function?

- What is the data type returned by this function?

- What is the purpose of the `range(number)` function call?

</v-clicks>

---

# Understanding the Factorial Function

```python
def factorial(number):
    factorial_value = 1
    values = list(range(1, number + 1))
    for value in values:
        factorial_value = factorial_value * value
    return factorial_value
```

<v-clicks>

- How would you write the function's type signature?

- What are the inputs and outputs of this function?

- Are there other ways to implement this function?

- What is the purpose of the `range(1, number + 1)` function call?

</v-clicks>

---

# Inputs and Outputs of Collatz Function

```python
def collatz(number: int) -> Iterator[int]:
    yield number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        yield number
```

- What is the output of this function?

- What is the pattern in the output of `collatz` ?

- Does this function ever stop running? **Actually, we don't yet know!**

---

# Using Dictionaries to Create Mappings

<v-clicks>

-   Static sequences like a tuple or a list create a mapping!

-   Python's dictionary is a discrete structure with a mapping:

    -   Create a mapping between **keys** and **values**
    -   Store **key-value pairs** inside of the structure
    -   You **lookup** the key to **find** the value
    -   Dictionary keys must be an **immutable** object
    -   The value connected to the key can be of **any** data type
    -   **Integers** and **strings** are common types for the key
    -   Often called **hashtables** or **hashmaps** in other languages!

-   Functions **compute** input and output while dictionaries **store** and **return** them

-   What are benefits to **pre-computing** values and **storing** and **returning** them?

-   How can you **create** and **use** a dictionary for a mapping in Python?

</v-clicks>

---

# Creating a Dictionary in Python

```python
mlb_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers'
}
```

<v-clicks>

- Reference: <https://realpython.com/python-dicts/>

- The use of `{` and `}` designates a dictionary

- Can you identify the **key** and the **value**?

- How would you lookup a **value** given a **key**?

</v-clicks>

---

# Alternative Way to Create a Dictionary

```python
mlb_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers')
])
```

<v-clicks>

- Here is an alternative way to create key-value pairs!

- Each of the key-value pairs is expressed as a tuple

- The tuples are stored in a list, one tuple for each pairing

- The `dict` constructor accepts a list of tuples!

</v-clicks>

---

# Another Way to Create a Dictionary

```python
mlb_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)
```

<v-clicks>

- Here is another way to create key-value pairs!

- Makes an explicit call to the `dict` constructor

- The keys and values are associated with `=` operator

</v-clicks>

---

# Using Dictionaries in a Python Program

```python
# display the address
print(type(mlb_team))

# display the contents
print(mlb_team)

# lookup specific values using a key
print(mlb_team['Minnesota'])
print(mlb_team['Colorado'])

# add a new value to the dictionary
mlb_team['Kansas City'] = 'Royals'
```

---

# Output Excerpt from Using a Dictionary

```python
<class 'dict'>
{'Colorado': 'Rockies', 'Boston': 'Red Sox',
 'Minnesota': 'Twins', 'Milwaukee': 'Brewers',
 'Seattle': 'Mariners'}

<class 'dict'>
{'Colorado': 'Rockies', 'Boston': 'Red Sox',
 'Minnesota': 'Twins', 'Milwaukee': 'Brewers',
 'Seattle': 'Mariners', 'Kansas City': 'Royals'}
```

- All construction methods produce **same** dictionary

- What happens if you access data that **does not exist**?

---

# Non-Existent Key in a Dictionary

```python
print(mlb_team['Toronto'])

Traceback (most recent call last):
File "dictionary-example.py", line 32,
    in <module>
    print(mlb_team['Toronto'])
KeyError: 'Toronto'
```

- Why did this program crash? What does the `KeyError` mean?

- Is there a way in which we can avoid the `KeyError` ?

- What functions help us to determine if a key-value pair exists?

---

# Using a Tuple as a Dictionary Key

```python
# create a dictionary that maps
# a tuple to a character
d = {(1, 1): 'a', (1, 2): 'b',
     (2, 1): 'c', (2, 2): 'd'}

# lookup a specific value based on a key
print(d[(1,1)])

# lookup a different value vased on a key
print(d[(2,1)])
```

<div class="bold text-5xl">

Since tuples are **immutable**, a dictionary can use it as a key!

</div>

---

# Using a List as a Dictionary Key

```python
d = {[1, 1]: 'a', [1, 2]: 'b',
     [2, 1]: 'c', [2, 2]: 'd'}

Traceback (most recent call last):
File "dictionary-differences.py", line 7,
    in <module>
    d = {[1, 1]: 'a', [1, 2]: 'b',
TypeError: unhashable type: 'list'
```

- Since lists are mutable, a dictionary cannot use it as a key!

- A dictionary's hashing function must be able to process the key

- How does the hashing function map input to the backing array?
