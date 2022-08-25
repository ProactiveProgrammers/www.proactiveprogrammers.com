---
# define the theme
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# define the highlighter and the colorSchema
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

## Function Scope

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

> How can I use Python's **scoping** rules and principle of **abstraction** to create
> **modularized** and/or **higher-order** functions that are easy to understand,
> implement, test, and maintain?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** some design principles associated with
> building Python programs that are easy to test and maintain

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is a function in the Python language?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Accepts input, does computation, produces output
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Testing improves correctness and confidence
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Modular design enables code reuse across projects
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the scoping rules of Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Variables declared in function have local scope
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Variables declared in module have global scope
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Formal and actual parameters for a function
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How does abstraction aid a program's design?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Enhances programmer productivity
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Minimizes conceptual complexity
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Improves ability to build complex systems
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of a good software design?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Enable code reuse
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-layer-group class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Support software quality
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<div class="text-3xl font-bold mt-8 ml-4">
It is often possible to build a program with a poor design! Improving it often
enhances other program characteristics.
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the trade-offs of a good design?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Obvious designs may take less time to implement
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Thoughtful designs take extra time to conceive
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Strategic versus tactical software design
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Design with Programming Constructs

<v-clicks>

- Leverage Python's constructs to achieve a good software design!

- Key components of Python programming language for design:

    - Formal parameter
    - Actual parameter
    - Default parameters
    - Function calls
    - Local and global variables
    - Lambda expressions
    - Higher-order function

- Make sure that you can find and use these components in Python source code!

<div class="flex row">

<mdi-help-box class="text-6xl ml-4 mt-0 text-blue-600" />

<div class="text-4xl text-true-gray-700 font-bold mt-4 ml-4">
Questions about Python features for design?
</div>

</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exhaustive Primality Testing

<div class="ml-1">

```python {all|1|8,10|all}
x = int(input("Enter integer greater than 2: "))
sm_div = None
for guess in range(2, x):
    if x % guess == 0:
        sm_div = guess
        break
if sm_div != None:
    print(f"Smallest divisor of {x} is {sm_div}")
else:
    print(f"Wow, {x} is a prime number!")
```

</div>

<br>

<v-clicks>

<div class = "bold -mt-3">
What are the <b>downsides</b> of this approach to primality testing?
</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Comparison to the engineering effort?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Not defined in a reusable and annotated function
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Not accompanied by executable test suite
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-alert-octagram class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Does not separate the program's operations
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Exhaustive Primality Testing ♻

<div class="ml-1">

```python {all|1-2|9,11|all}
def primality_test_exhaustive(x: int)
              -> Tuple[bool, List[int]]:
    smallest_divisor = None
    for guess in range(2, x):
        if x % guess == 0:
            smallest_divisor = guess
            break
    if smallest_divisor is not None:
        return (False, [smallest_divisor])
    else:
        return (True, [1, x])
```

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's explore this function with Python!
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
Go to the <code>function-scope/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
<code>perform-exhaustive-primality-testing</code>
</div>

</div>

</div>

[//]: # (Slide End }}})
---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What is a function specification in Python?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Defines a contract between creator and caller
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Offers both assumptions and guarantees
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Ideally specified in type annotations for a function
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Higher-order Functions in Python

<div class="ml-1">

```python {all|1-4|6-8|all}
def square(number: int):
    print(f"Called square({number})")
    print(f"  returning {number*number}")
    return number * number

def call_twice(f, number: int):
    print(f"Calling twice {f} with number {number}")
    return f(f(number))
```

</div>

<div v-click>

<div class="flex row">

<div class="text-3xl font-bold mt-8 ml-4">
Higher-order functions can accept and call functions as their input! What is the benefit of this design approach?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # "Slide Start {{{"

# Programming Warmup

<iframe
  src="https://proactiveprogrammers.com/live/repl/index.html?kernel=python&code=%64%65%66+%73%71%75%61%72%65%28%6e%75%6d%62%65%72%3a+%69%6e%74%29%3a%0a++++%70%72%69%6e%74%28%66%22%43%61%6c%6c%65%64+%73%71%75%61%72%65%28%7b%6e%75%6d%62%65%72%7d%29%22%29%0a++++%70%72%69%6e%74%28%66%22++%72%65%74%75%72%6e%69%6e%67+%7b%6e%75%6d%62%65%72%2a%6e%75%6d%62%65%72%7d%22%29%0a++++%72%65%74%75%72%6e+%6e%75%6d%62%65%72+%2a+%6e%75%6d%62%65%72%0a%0a%64%65%66+%63%61%6c%6c%5f%74%77%69%63%65%28%66%2c+%6e%75%6d%62%65%72%3a+%69%6e%74%29%3a%0a++++%70%72%69%6e%74%28%66%22%43%61%6c%6c%69%6e%67+%74%77%69%63%65+%7b%66%7d+%77%69%74%68+%6e%75%6d%62%65%72+%7b%6e%75%6d%62%65%72%7d%22%29%0a++++%72%65%74%75%72%6e+%66%28%66%28%6e%75%6d%62%65%72%29%29%0a"
  width="100%"
  height="90%"
  style="border: 1px solid darkgrey;"
></iframe>

[//]: # "Slide End }}}"

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of higher-order functions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports general-purpose function creation
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Allows executable functions as function input
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Supports both code reuse and modularity
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's run higher-order functions in Python!
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
Go to the <code>function-scope/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Use <code>explore-higher-order-functions.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Lambda Expressions in Python

<div class="ml-1">

```python {all|1|3-4|6-8|all}
square_lambda = lambda x: x*x

number = 5
result = call_twice(square_lambda, number)

print("Calling the square lambda twice with " +
        str(number) + " is " + str(result))
print()
```

</div>

<div v-click>

<div class="flex row">

<div class="text-3xl font-bold mt-8 ml-4">
Lambda expressions support the storage of simple computations inside a variable.
What is the benefit?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # "Slide Start {{{"

# Programming Warmup

<iframe
  src="https://proactiveprogrammers.com/live/repl/index.html?kernel=python&code=%64%65%66+%63%61%6c%6c%5f%74%77%69%63%65%28%66%2c+%6e%75%6d%62%65%72%3a+%69%6e%74%29%3a%0a++++%70%72%69%6e%74%28%66%22%43%61%6c%6c%69%6e%67+%74%77%69%63%65+%7b%66%7d+%77%69%74%68+%6e%75%6d%62%65%72+%7b%6e%75%6d%62%65%72%7d%22%29%0a++++%72%65%74%75%72%6e+%66%28%66%28%6e%75%6d%62%65%72%29%29%0a%0a%73%71%75%61%72%65%5f%6c%61%6d%62%64%61+%3d+%6c%61%6d%62%64%61+%78%3a+%78%2a%78%0a%0a%6e%75%6d%62%65%72+%3d+%35%0a%72%65%73%75%6c%74+%3d+%63%61%6c%6c%5f%74%77%69%63%65%28%73%71%75%61%72%65%5f%6c%61%6d%62%64%61%2c+%6e%75%6d%62%65%72%29%0a%0a%70%72%69%6e%74%28%22%43%61%6c%6c%69%6e%67+%74%68%65+%73%71%75%61%72%65+%6c%61%6d%62%64%61+%74%77%69%63%65+%77%69%74%68+%22+%2b%0a++++++++%73%74%72%28%6e%75%6d%62%65%72%29+%2b+%22+%69%73+%22+%2b+%73%74%72%28%72%65%73%75%6c%74%29%29%0a%70%72%69%6e%74%28%29%0a"
  width="100%"
  height="90%"
  style="border: 1px solid darkgrey;"
></iframe>

[//]: # "Slide End }}}"


---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are the benefits of lambda expressions?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Lightweight way to specify a computation
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Compared to the function, often faster to create
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Useful for small functions input to other functions
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Let's explore lambda expressions in Python!
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
Go to the <code>function-scope/</code> directory
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Explore <code>explore-lambda-expressions.ipynb</code>
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Investigating Function Scope

<div class = "mt-10">
</div>

<v-clicks>

-   Creating Python programs with "good" designs:

    -   **Q1**: What are the benefits of **good design**?

    -   **Q2**: What **language features** support good design?

    -   **Q3**: How does a **higher-order** function improve design?

    -   **Q4**: How does a **lambda** function improve design?

    -   **Q5**: How can we compare the **quality** of two designs?

-   We will always aim to create good designs in **upcoming projects**!

-   Balance the **trade-offs** associated with designing quality software

</v-clicks>

[//]: # (Slide End }}})
