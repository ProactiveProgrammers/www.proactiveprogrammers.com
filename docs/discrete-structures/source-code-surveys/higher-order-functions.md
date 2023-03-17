---
tags:
  - Conditional Logic
  - Data Types
  - Functions
  - Iteration Constructs
  - Numerical Computation
---

![Higher-Order Functions](/img/Pro-Discrete-Structures-Higherorder-Functions.svg){loading=lazy}

# Higher-Order Functions

## Project Goals

This assignment invites you to run and observe two Python programs stored in
files called `demonstrate-map-function.py` and `demonstrate-reduce-function.py`.
Both of these programs demonstrate the use of higher-order functions that can
accept as input a callable function and then use that function to perform a
computation. Specifically, the `demonstrate-map-function.py` illustrates the use
of a `map(f, sequence)` function that applies the function `f` to a list of data
values called `sequence`. The `demonstrate-reduce-function.py` shows the use of
a `reduce(f, sequence, initial)` function that starts at an `initial` value and
then applies a function `f` to all of the values in `sequence` and returns a
result. As you run these two programs and study their output you will explore an
alternative approach to programming, called functional programming.

## Project Access

If you are a student enrolled in a Computer Science class at Allegheny College,
you can access this assignment by clicking the link provided to you in Discord.
Once you click this link it will create a GitHub repository that you can clone
to your computer by following the general-purpose instructions in the
description of the [technical
skills](/proactive-skills/introduction-proactive-skills/). Specifically, you
will need to use the `git clone` command to download the project from GitHub to
your computer. Now you are ready to add source code and documentation to the
project!

## Code Survey

If you change into the `source` directory of your GitHub repository, you will
see a Python program called `demonstrate-map-function.py`. Your goal for this
project is to implement both a `map` higher-order function and a `square`
function that can serve as the input to the `map` function. When you run the
command `python demonstrate-map-function.py` after adding the required source
code to the program, it should produce the following output:

```
Squaring all of the numbers in the values tuple
   (4, 9, 25, 49, 121)
Squaring all of the numbers output by range(10)
   (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
```

It is worth noting that the `demonstrate-map-function.py` should contain the
following source code that calls the `map` function to produce the
aforementioned output. Line `1` of this code creates a tuple called `values`
that contains five numbers and line `2` calls the `map` function by providing it
`square` and the `values`. After you have correctly implemented the `map` and
`square` functions the two `print` statements on lines `3` and `4` will produce
the first two lines of output. As shown in the output, the next source code
segment in `demonstrate-map-function.py` performs the same operation while using
`range(10)` instead of the specific numbers in the `values` tuple.

```python linenums="1"
values = (2, 3, 5, 7, 11)
squared = map(square, values)
print("Squaring all of the numbers in the values tuple")
print("   " + str(squared))
```

You should also notice that the `source` directory of your GitHub repository
contains a Python program called `demonstrate-map-function.py`. Your goal for
this project is to implement a `reduce` higher-order function and both a `plus`
and a `multiply` function that perform arithmetic on two input numbers and can
serve as the input to the `map` function. When you run the command `python
` after adding the required source code to the
program, it should produce the following output:

```
Adding all of the numbers together with a reduce function
   15
Multiplying all of the numbers together with a reduce function
   120
```

It is worth noting that the `demonstrate-reduce-function.py` should contain the
following source code that calls the `reduce` function to produce the
aforementioned output. Line `1` of this code creates a list called `numbers`
that contains five numbers and line `2` calls the `reduce` function by providing
it `plus` and the `numbers` list. After you have correctly implemented the
`reduce` and `plus` functions the two `print` statements on lines `3` and `4`
will produce the first two lines of output. As shown in the output, the next
source code segment in `demonstrate-reduce-function.py` performs a similar
computation while calling `reduce(multiply, numbers, 1)` instead of
`reduce(plus, numbers, 0)`. Why it is sensible to specify that the
`initial` parameter for `reduce` should be `1` instead of `0` when using the
`multiply` function instead of `plus`?

```python linenums="1"
numbers = [1, 2, 3, 4, 5]
added_numbers = reduce(plus, numbers, 0)
print("Adding all of the numbers together with a reduce function")
print("   " + str(added_numbers))
```

As you continue this source code survey, make sure to note that the
function signatures in `demonstrate-map-function.py` look like those in
the following list. This list demonstrates that these functions do not
have type annotations. After providing the source code for the `square`
and `map` functions in this file, please determine and add the type
annotations for the formal parameters called `value`, `f`, and
`sequence`. Similarly, there are three functions called `plus`,
`multiply`, and `reduce` in the `demonstrate-reduce-function.py` file
that do not have type annotations. You can study the source code of
these functions and the way that they are called in the
`demonstrate-reduce-function.py` script to learn more about what type
annotations you should add to the formal parameters called `number_one`,
`number_two`, `f`, `sequence`, and `initial`. When you add these type
annotations, you should leverage them to enhance your understanding of
the inputs, outputs, and behavior of a map-reduce computation.

- Functions in the `demonstrate-map-function.py` file:
    - `def square(value)`
    - `def map(f, sequence)`
- Functions in the `demonstrate-reduce-function.py` file:
    - `def plus(number_one, number_two)`
    - `def multiply(number_one, number_two)`
    - `def reduce(f, sequence, initial)`

## Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage
project dependencies and virtual environments, it does not support the use of
commands like `poetry run task test`. However, you can leverage the relevant
instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about this project's two programs.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. Since
this is a source code survey, you should provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is for you to
understand each line of source code needed to implement a simplified version of
the `map` and `reduce` functions. You should also think carefully about the
steps that you would need to take to implement a distributed and/or parallel
computation that uses `map` and `reduce` to improve the efficiency of a
program.

## Project Assessment

Since this project is source code survey, it is aligned with the **remembering**
and **understanding** levels of [Bloom's
taxonomy](/proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet the project's specification.

## Seeking Assistance

Emerging proactive programmers who have questions about this project are invited
to ask them in either the [GitHub discussions
forum](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/discussions)
or the [Proactive Programmers Discord server](https://discord.gg/kjah8MFYbR).
Before you ask your question, please read the advice concerning how to best
participate in the [Proactive Programmers
community](https://proactiveprogrammers.com/proactive-community/community-connections/).
If you find a mistake in this project, please describe it and propose a solution
by creating an issue in the [GitHub Issue
Tracker](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/issues).
