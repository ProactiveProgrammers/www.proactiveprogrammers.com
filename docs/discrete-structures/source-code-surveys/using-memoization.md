# Using Memoization

## Project Goals

This assignment invites you to run and observe one Python program called
`calculate-fibonacci-lru-cache`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a
best practice, this program is a script, without any dependencies on
other Python packages, that you can run through the Python interpreter.
The main reason that you can run the `calculate-fibonacci-lru-cache` as
a script is because it does not have any external package dependencies,
instead only using packages that are a part of the Python language. As
you continue to practice a different way to run a Python program, this
project invites you to explore how to (i) implement memoization for a
mathematical computation using a `dict`, (ii) how to adopt memoization
using the `functools.lru_cache`, and (iii) how to calculate a number in
the Fibonacci sequence using Binet's formula.

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
`@functools.lru_cache(maxsize=128)` annotation so that it leverages a least
recently used (LRU) cache to store previously computed values, following the
paradigm of memoization, to make the computation faster. If you run this program
with the command `python calculate-fibonacci-lru-cache.py` then it should
produce following output. It is worth noting that the
`calculate-fibonacci-lru-cache` program also provides a `def fibonacci_binet(n:
int) -> int`, as described in the following source code segment, that can
calculate the `n`-th Fibonacci number with [Binet's
formula](https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula).

```text
Recursive Fibonacci(100) = 354224848179261915075
LRU cache information: CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)
Binet Fibonacci(100) = 354224848179261915075
Recursive Fibonacci(150) = 9969216677189303386214405760200
LRU cache information: CacheInfo(hits=149, misses=151, maxsize=128, currsize=128)
Binet Fibonacci(150) = 9969216677189303386214405760200
```
```python linenums="1"
def fibonacci_binet(n: int) -> int:
    """Calculate a number in the Fibonacci sequence using Binet's formula."""
    square_root_n = math.sqrt(n)
    return int((((1 + square_root_n) ** n - (1 - square_root_n) ** n) / (2 ** n * square_root_n)))
```

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
`calculate-fibonacci-lru-cache.py` script to ensure that it is working correctly!
This might involve creating different inputs to the function under test, calling
the `calculate_mode` function, and then checking to ensure that it returned the
correct ordered pair as its output.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. Since
this is a source code survey, you should provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is for you to
ensure that you can implement and understand two distinct approaches to using
memoization to speed up the computation of a mathematical function. Students who
want to explore this area further are encouraged to experimentally determine how
much slower the Fibonacci computations would be if either the LRU cache or the
`dict`-based approach were not adopted in an attempt to make the functions
faster.

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
