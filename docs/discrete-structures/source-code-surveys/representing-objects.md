# Representing Objects

## Project Goals

This assignment invites you to enhance, run, and observe three Python programs
called `create-dog-with-class`, `create-dog-with-dictionary`, and
`create-dog-with-list`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a best
practice, this program is a script, without any dependencies on other Python
packages, you can run each of these programs with the Python interpreter. As you
continue to practice a different way to run a Python program, this project
invites you to explore how to use three different approaches to representing an
object in the Python programming language. After completing this source code
survey, you should understand how to express relationships between variables in
three different ways and be able to articulate the trade-offs associated with
each approach.

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
see a Python program called `calculate-fibonacci-lru-cache.py`. Your goal for
this project is to add the source code required by the `TODO` markers so that
the program produces the output that is given below this paragraph.
Specifically, you will need to add an implementation of the following function:
`def fibonacci(number: int) -> int:`. This function should be decorated with the
`@functools.lru_cache(maxsize=128)` annotation so that it leverages a
least-recently-used (LRU) cache to store previously computed values, following
the paradigm of memoization and aiming to make the computation faster. If you
run this program with the command `python calculate-fibonacci-lru-cache.py` then
it should produce following output. Finally, please observe that the output of
this program illustrates that the LRU cache provided by `functools.lru_cache`
keeps track of its size and the number of times a value was and was not found
inside of the cache.

```text
Recursive Fibonacci(35) = 9227465
Binet Fibonacci(35)     = 9227465
LRU cache information: CacheInfo(hits=33, misses=36, maxsize=128, currsize=36)
Recursive Fibonacci(70) = 190392490709135
Binet Fibonacci(70)     = 190392490709135
LRU cache information: CacheInfo(hits=69, misses=71, maxsize=128, currsize=71)
```

It is worth noting that the `calculate-fibonacci-lru-cache` program also
provides a `def fibonacci_binet(n: int) -> int`, as described in the following
source code segment, that can calculate the `n`-th Fibonacci number with
[Binet's
formula](https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula). Even
though this function is only accurate --- as implemented in the Python
programming language --- for small values of `n`, it is an efficient approach
for ensuring that the other implementations work as expected. Notably, as
explained in the article entitled [Fibonacci direct calculation
formula](https://stackoverflow.com/questions/50622088/fibonacci-direct-calculation-formula),
the formula that the following equation implements is "mathematically exact,
but in practice [...] subject to floating point error". Can you explain why this
function will not always compute the correct Fibonacci value?

```python linenums="1"
def fibonacci_binet(n: int) -> int:
    """Calculate a number in the Fibonacci sequence using Binet's formula."""
    square_root_five = math.sqrt(5)
    coefficient = (1 / square_root_five)
    first_term = ((1 + square_root_five) / 2) ** n
    second_term = ((1 - square_root_five) / 2) ** n
    return int(coefficient * (first_term - second_term))
```

You should also notice that the `source` directory contains the Python program
called `calculate-fibonacci-dictionary`. You will need to follow the `TODO`
markers in this file to implement a version of the `def fibonacci(number: int)
-> int:` function that creates and uses a `dict` to explicitly manage a history
of the inputs to the function and the outputs that resulted from those inputs.
After you are finished implementing this version of the function you should run
the program and confirm that it produces the same output as the one that uses
the LRU cache. With that said, please note that, while this program should
produce the same values for numbers in the Fibonacci sequence, it will not
produce any output concerning the LRU cache since it implements the memoization
directly by creating a `dict` and adding to it and then checking it during the
recursive computation. After implementing these two methods, which one do you
prefer? Why?

## Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage
project dependencies and virtual environments, it does not support the use of
commands like `poetry run task test`. However, you can leverage the relevant
instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about this project's program. You are also
encouraged to implement your own test cases for the
`calculate-fibonacci-lru-cache.py` script to ensure that it is working
correctly! This might involve creating different inputs to the function under
test, calling the `def fibonacci(number: int) -> int` function, and then
checking to ensure that it returned the correct ordered pair as its output.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. Since
this is a source code survey, you should provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is for you to
ensure that you can implement and understand two distinct approaches to using
memoization to speed up the computation of a mathematical function. Students who
want to explore this area further are encouraged to experimentally determine how
much slower the Fibonacci computations would be if the LRU cache or the
`dict`-based approach were not used to make the functions faster.

## Project Assessment

Since this project is source code survey, it is aligned with the **remembering**
and **understanding** levels of [Bloom's
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
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
