---
tags:
  - Conditional Logic
  - Data Types
  - Functions
  - Iteration Constructs
  - Statistics
---

![Discrete Structures](/img/Pro-Discrete-Structures-Mode-Calculation.svg){loading=lazy}

# Mode Calculation

## Project Goals

This assignment invites you to run and observe one Python program called
`perform-mode-calculation`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a best
practice, this program is a script, without any dependencies on other Python
packages, that you can run through the Python interpreter. The main reason that
you can run the `perform-mode-calculation` as a script is because it does not
have any external package dependencies, instead only using packages that are a
part of the Python language. As you continue to practice a different way to run
a Python program, this project invites you to explore how to (i) import the
`Counter` module from the `collections` package, (ii) implement a function
called `calculate_mode` that can find at most one mode inside of a list of
numbers, and (iii) call the `calculate_mode` function and display the values in
the tuple that it produces.

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

???+ note

    If you are an emerging proactive programmer who is not enrolled in a
    Computer Science class at Allegheny College, you can still work on this
    assignment! To get started, you should click the "Use this template" icon in
    the :material-github:
    [mode-calculation-starter](https://github.com/ProactiveProgrammers/mode-calculation-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Code Survey

If you change into the `source` directory of your GitHub repository, you
will see a Python program called `perform-mode-calculation.py`. Your
goal for this project is to find and fix the defects in the function
with the signature `def calculate_mode(numbers: List[int]) -> Tuple[int,
int]:`. Specifically, this function signature indicates that the
`calculate_mode` function takes as input a list of integer values and
returns a tuple of two integers (i.e., an ordered pair) where the first
value is the number that is the mode and the second value is the number
of times that the mode appeared. To be clear, the `calculate_mode`
function should find the mode of a list of numbers, or the number that
appears most frequently in the list. When you run the command `python
perform-mode-calculation.py` after correcting the program's defects, it
should produce the following output when it looks for a mode in the
`scores = [7, 8, 9, 2, 10, 9, 9, 9]`.

```
The mode of the list of numbers is 9
The mode of the list of was found 4 times!
```

It is worth noting that the `calculate_mode` function will only work correctly
when it is provided with a list that contains a single value for the mode. If
there are multiple values for the mode (i.e., the list `scores = [7, 8, 7, 7, 9,
2, 10, 9, 9, 9]` has both the number `7` and the number `9` as a mode) then it
will not return both of them. How would you need to change the function's
computation and the type of data that it returns in order to ensure that can
return all modes that are evident in the input list? Finally, don't forget that
it is only possible for the program to run correctly if it contains the `import`
statements that make the classes for the type annotations available! This means
that you need to have both `from typing import List` and `from typing import
Tuple` at the top of the `perform-mode-calculation.py`. Since the source code in
the *Doing Math with Python* book uses the `Counter` module, the
`perform-mode-calculation.py` script also needs the statement `from collections
import Counter`.

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
`perform-mode-calculation.py` script to ensure that it is working correctly!
This might involve creating different inputs to the function under test, calling
the `calculate_mode` function, and then checking to ensure that it returned the
correct ordered pair as its output.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. Since
this is a source code survey, you should provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is for you to
improve and document the source code of a function that indexes a tuple in order
to swap its contents.

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
