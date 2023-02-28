---
# use the default theme
default: theme
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# define the highlighter and the colorSchema
highlighter: prism
colorSchema: light
remoteAssets: false
# do not show line numbers in code blocks
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
    @apply text-orange-600 mb-4;
  }
</style>

<div v-click>

## Key Question

> How can I use the principles and primitives of object-oriented programming to
> implement Python programs with easy-to-understand designs?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of object-oriented
> programming and the exception handling features provided by Python
> to implement high-quality and easy-to-understand programs.

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore object-oriented programming!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What can go wrong when using a program?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Division by zero or index out of range
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Networking error or file system problems
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Use does not match programmer expectations!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exception Handling in Python

<v-clicks>

- Program implementation may not match its actual use

- Exception handling provides elegant way handle problems

- `try` and `except` are basic building blocks

- Python allows to you try running "risky code" and then handle problems:

    - `try` block contains code that may throw an exception

    - `except` block handles case when a specific exception arises

    - It is possible to have one or more `except` blocks overall

- What should the program do when the exception is caught?

- Well, it depends on the type of the exception and what happened!

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Exception Handling for Ratios

<div class="-ml-5 -mt-1">

```python {all|1-3|4|5|6-7|8-9|10-11|12|all}
from typing import List
def get_ratios(one: List, two: List) -> List[float]:
    ratios = []
    for index in range(len(one)):
        try:
            ratios.append(one[index] / two[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError("Incorrect arguments")
    return ratios
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Use Function with Exception Handling

<div class="-ml-5 -mb-7">

```python {all|1-2|1,3|1,4|1,5|6-7|all}
try:
    print(get_ratios([1, 2, 7, 6], [1, 2, 0, 3]))
    print(get_ratios([], []))
    print(get_ratios([1, 2, 7], [1, 2, 10, 3]))
    print(get_ratios([1, 2, 7, 6], [1, 2, 10]))
except ValueError as message:
    print(message)
```

</div>

<br>

<v-clicks>

<p class = "bold">
What is the <b>output</b> from running these function calls?
</p>

<p class = "bold">
Why do certain <b>inputs</b> cause an exception to be thrown?
</p>

<p class = "bold">
What is there <b>was not</b> a <code>try</code> and a <code>except</code> ?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Use Exception Handling Program

<div class="-mt-4 -mb-4 -ml-2">

```text {all|1|2|3|4|all}
[1.0, 1.0, nan, 2.0]
[]
[1.0, 1.0, 0.7]
Incorrect arguments
```

</div>

<v-clicks>

<p class = "bold">
Which exception handling blocks produced this <b>output</b>?
</p>

<p class = "bold">
Was any of this output produced <b>without</b> exception handling?
</p>

<p class = "bold">
Why no <b>crash</b> when using <code>try</code> and a <code>except</code> block?
</p>

<p class = "bold">
What happens if call function <b>without</b> <code>try</code> and  <code>except</code> ?
</p>

<div class="flex row">

<mdi-alert-octagon class="text-5xl ml-6 mt-2 text-blue-600"/>

<div class="text-3xl font-bold mt-4 ml-4">
Let's call <code>get_ratios</code> without exception handling!
</div>

</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Use Exception Handling Program 🤦

<div class="-ml-0 -mt-2 -mb-2">

```text {all|1|3-4|5|6-7|8-9|10|all}
print(get_ratios([1, 2, 7], [1, 2, 10, 3]))

During handling of the above exception,
  another exception occurred:
Traceback (most recent call last):
File "get-ratios-exceptions.py", line 24
  print(get_ratios([1, 2, 7, 6], [1, 2, 10]))
File "get-ratios-exceptions.py", line 11
  raise ValueError("Incorrect arguments")
ValueError: Incorrect arguments
```

</div>

<v-clicks>

<p class = "bold">
Why does program <b>crash</b> when no <code>try</code> and a <code>except</code> block?
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of exception handling?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Principled way to avoid crashes
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Explicitly handles error conditions
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Useful flow of control mechanism
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's try to use exception handling in Python!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the file in <a href = "https://proactiveprogrammers.com/live">Jupyter Lite</a> or
<a href = "https://githubtocolab.com/ProactiveProgrammers/www.proactiveprogrammers.com">Google Colab</a>!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>data-abstraction/object-oriented/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-exception-handling.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

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

[//]: # (Slide Begin {{{)

# Constructor for the `Person` Class

<div class="mt-8 -ml-5">

```python {all|1|3-5|6|7-11|all}
class Person:

    def __init__(
        self, name: str, country: str, [...]
    ) -> None:
        """Define the constructor for a person."""
        self.name = name
        self.country = country
        self.phone_number = phone_number
        self.job = job
        self.email = email
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Defining a Textual Representation

<div class="-ml-2 -mb-5">

```python
def __repr__(self) -> str:
    return f"{self.name} is a
      {self.job} who lives in
      {self.country}. You can
      call this person at
      {self.phone_number} and
      email them at {self.email}"
```

</div>

<br>

<v-clicks>

<p class = "bold">
Classes in Python have "dunder methods" like <code>__repr__</code>
</p>

<p class = "bold">
The <code>self</code> parameter indicates object is parameter to method
</p>

<p class = "bold">
Methods can access the state of an object with <code>self.email</code>
</p>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Defining a Method for the `Person` Class

<div class="mt-8 -ml-5">

```python
def create_list(self) -> List[str]:
    details = []
    details.append(self.name)
    details.append(self.country)
    details.append(self.phone_number)
    details.append(self.job)
    details.append(self.email)
    return details
```

<v-clicks>

<p class = "bold">
Methods like <code>create_list</code> process and return object state
</p>

<p class = "bold">
<b>Key Principles</b>: encapsulation, inheritance, polymorphism
</p>

</v-clicks>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's explore object-oriented programming!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the file in <a href = "https://proactiveprogrammers.com/live">Jupyter Lite</a> or
<a href = "https://githubtocolab.com/ProactiveProgrammers/www.proactiveprogrammers.com">Google Colab</a>!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>data-abstraction/object-oriented/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-exception-handling.ipynb</code>
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

[//]: # (Slide Begin {{{)

# Importing and Using the `Person` Class

<div class="mt-8 -ml-3">

```python
from objectprocessor import person

def create_display(person_list:
                   List[person.Person]) -> str:
    person_list_text = ""
    for current_person in person_list:
      person_list_text +=
        "- " + str(current_person) + "\n"
    return person_list_text
```

</div>

<div class="mt-10">

<v-clicks>

<p class = "bold">
<code>str</code> function calls the <code>__repr__</code> method in <code>Person</code>
</p>

</v-clicks>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Searching for a Matching `Person` Object

<div class="mt-0 -ml-3">

```python {all|1-5|6|7-11|12|all}
def find_matching_people(
  attribute: str,
  match: str,
  person_data: List[person.Person]
) -> List[person.Person]:
    matching_people_list = []
    for current_person in person_data:
      if is_matching_person(attribute,
            match, current_person):
            matching_people_list.
               append(current_person)
    return matching_people_list
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Define a class and construct instances
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Define a class with both state and a constructor
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Ensure that the constructor initializes the state
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Create class instances by calling constructor
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Begin {{{)

# Modelling a Dog as an Object

<div class="mt-0 -ml-3 mb-10">

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

miles = Dog("Miles", 4)
bosco = Dog("Bosco", 8)
```

</div>

<v-click>

<p class = "bold">
Define a <code>Dog</code> class and then create two instances of it!
</p>

</v-click>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's construct new instances of a class!
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Find the file in <a href = "https://proactiveprogrammers.com/live">Jupyter Lite</a> or
<a href = "https://githubtocolab.com/ProactiveProgrammers/www.proactiveprogrammers.com">Google Colab</a>!
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>data-abstraction/object-oriented/</code>
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Run <code>explore-exception-handling.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Object-Oriented Programming

<v-clicks>

- Object-oriented programming accomplishes these goals:

    - Creates a component with both **state** and **behavior**
    - Organizes a program into **classes** and their **instances**
    - Supports **structured** programming that may lack otherwise

-   Importance of object-oriented programming in Python:

    -   **Q1**: What are the **foundations** of the object-oriented paradigm?

    -   **Q2**: What are the **benefits** of object-oriented paradigm?

    -   **Q3**: What are the **trade-offs** of object-oriented programming?

    -   **Q4**: How do you use **Pytest** to test an object-oriented program?

    -   **Q5**: How is object-oriented programming in Python **unique**?

</v-clicks>

[//]: # (Slide End }}})
