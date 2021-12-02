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

## Object-Oriented Programming

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

> How do I use the concept of a relation and the industrially relevant practice
> of object-oriented programming to correctly implement Python programs that
> are easy to understand and maintain?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some concepts about the **objects**
> and to learn different ways to represent and use objects in Python

</div>

<v-click>

<div class="flex row mt-0 ml-0">

<uim-rocket class="text-6xl ml-5 mt-4 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-6 ml-10">
Let's create objects in Python programs!
</div>

</div>

</v-click>

[//]: # (Slide End }}})

---

# Mathematical Concept of a Relation

-   As first introduced in Chapter 1, a relation is a connection between
    two or more entities (e.g., sets or ordered pairs)

-   Understanding relations in discrete mathematics:

    -   **Binary relation**: set of ordered pairs
    -   **Ternary relation**: set of ordered triples
    -   **Quaternary relation**: set of ordered quadruples
    -   **n-ary relation**: set of ordered n-tuples

-   First, think about the number of related elements

-   Consider the relationship between the elements as well

-   How do I create and use relations in Python? Dictionary? List? Object?

-   How can object-oriented programming express entity relationships?

---

# Using Ordered Pairs in Python

```python
def factorial_iterative(number):
    factorial_list = []
    value = 1
    factorial_value = 1
    values = list(range(1, number + 1))
    for value in values:
        factorial_value = factorial_value * value
        factorial_list.
           append((value, factorial_value))
    return ((value, factorial_value),
           factorial_list)
```

---

# Understanding `factorial_iterative`

- What are the inputs and outputs of this function?

  -   **Input**: `number: int`

  -   **First Output**: `Tuple[int, int]`

  -   **Second Output**: `List[Tuple[int, int]]`

-   The two return values are also combined in a `Tuple`!

-   Recall `Tuple[int, int]` is Pythonic for an ordered pair

-   What is the need for such a complicated return value?

-   What is the best way to represent relationships in Python?

-   The tuple does not offer **semantic meaning** for return value

---

# Lists to Represent Objects in Python

```python
bosco = ["Bosco", 6, "Havanese"]
faith = ["Faith", 14, "Havanese"]

print(f"The name of the dog is: {bosco[0]}")
print(f"The age of the dog is: {bosco[1]}")
print(f"The breed of the dog is: {bosco[2]}")

print(f"The name of the dog is: {faith[0]}")
print(f"The age of the dog is: {faith[1]}")
print(f"The breed of the dog is: {faith[2]}")
```

<br>

<v-clicks>

<p class = "bold">
Leverages a built-in discrete structure! But, drawbacks?
</p>

</v-clicks>

---

# Output from List Representing Objects

```text
The name of the dog is: Bosco
The age of the dog is: 6
The breed of the dog is: Havanese

The name of the dog is: Faith
The age of the dog is: 14
The breed of the dog is: Havanese
```

- Questions about the **list-based** approach:

  - What are the **benefits** of this approach?
  - How can this approach lead to **defects**?
  - Can this approach ensure **object uniformity**?
  - Are there **other approaches** to creating objects?

---

# Dictionaries to Represent Objects

```python
bosco = {}
bosco["Name"] = "Bosco"
bosco["Age"] = 6
bosco["Breed"] = "Havanese"

faith = {}
faith["Name"] = "Faith"
faith["Age"] = 14
faith["Breed"] = "Havanese"
```

<br>

<v-clicks>

<p class = "bold">
Leverages a built-in discrete structure! But, drawbacks?
</p>

<p class = "bold">
Which approach is better? Using a list or a dictionary?
</p>

</v-clicks>

---

# Accessing a Dictionary Representation

```python
print(f"The dog's name is: {bosco['Name']}")
print(f"The dog's age is: {bosco['Age']}")
print(f"The dog's breed is: {bosco['Breed']}")

print(f"The dog's name is: {faith['Name']}")
print(f"The dog's age is: {faith['Age']}")
print(f"The dog's breed is: {faith['Breed']}")
```

- What is the output of this program?

- What is better `bosco[0]` or `bosco['name']` ? Why?

- Does this approach ensure object uniformity? No!

---

# Output from Using a Dictionary

```text
The dog's name is: Bosco
The dog's age is: 6
The dog's breed is: Havanese

The dog's name is: Faith
The dog's age is: 14
The dog's breed is: Havanese
```

- Note that the program produces the **same output**!

- How can this approach lead to **defects**?

- Are there other approaches to creating objects?

---

[//]: # (Slide Start {{{)

# Object-Oriented Programming

<v-clicks>

- Python supports both the **procedural** and **functional** programming

- It also supports the **object-oriented** programming model

- Features of the object-oriented programming approach:

    - A class defines a **template** for the **state** and **behavior** of an object

    - Classes create **new types** in the Python program

    - These new types can be used as **type annotations** for functions

    - Classes can be **defined** in a module and **accessed** by other models

- Python's object-oriented features are more **limited** than other languages

- What are the **benefits** and **drawbacks** of object-oriented programming?

</v-clicks>

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

# Representing an Object with a Class

```python
class Dog:
  # constructor for the Dog class
  def __init__(self, name, age, breed):
      self.name = name
      self.age = age
      self.breed = breed
```

- What are the components of the `Dog` class?

- How do you create an instance of the `Dog` class?

- How is this better than using a list or a dictionary?

- What are the drawbacks associated with using objects?

---

# Constructing an Instance of `Dog`

```python
bosco = Dog("Bosco", 6, "Havanese")

print(bosco)

print(f"The dog's name is: {bosco.name}")
print(f"The dog's age is: {bosco.age}")
print(f"The dog's breed is: {bosco.breed}")
```

<br>

- How is this **different** than using a list or a dictionary?

- The `Dog` class defines a new type recognized by Python

- Ensures the uniformity of all instance of `Dog` class

---

# Constructing Another Instance of `Dog`

```python
faith = Dog("Faith", 14, "Havanese")

print(faith)

print(f"The dog's name is: {faith.name}")
print(f"The dog's age is: {faith.age}")
print(f"The dog's breed is: {faith.breed}")
```

- This program produces **same** output a list-based and dictionary-based!

- Which approach is easier to **implement**? Easier to **understand**? Why?

- What is the **location** of `bosco` and `faith` in computer's memory?

---

# Output from Using Objects in Python

```text
<__main__.Dog object at 0x7f6090b44a90>

The dog's name is: Bosco
The dog's age is: 6
The dog's breed is: Havanese
```

<div class="mt-10">

- `bosco.name` accesses the dog's name

- `bosco.age` accesses the dog's age

- `bosco.breed` accesses the dog's breed

- What about **displaying** details for the `faith` object?

</div>

---

# Output from Using Objects in Python

```text
<__main__.Dog object at 0x7f6090b44af0>

The dog's name is: Faith
The dog's age is: 14
The dog's breed is: Havanese
```

<div class="mt-10">

- `faith.name` accesses the dog's name

- `faith.age` accesses the dog's age

- `faith.breed` accesses the dog's breed

- Note that `bosco` and `faith` are **distinct** instances in memory!

</div>

---

# Defining Methods for Python Objects

```python
# define a class to represent a Dog entity
class Dog:

    # define a description method for the dog
    def description(self):
        return f"{self.name} is a {self.age}
                 years old {self.breed}"

    # define an action method for the dog
    def action(self, action):
        return f"Hey, {self.name} {action}!"
```

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
