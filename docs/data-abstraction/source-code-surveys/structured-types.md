# Structured Types

## Project Goals

This assignment invites you to run and observe two Python programs called
`compute-tuple-intersection` and `perform-apply-to-each`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a best
practice, these programs are scripts, without any dependencies on other Python
packages, that you can run through the Python interpreter. As you continue to
practice a different way to run a Python program, this project offers you the
opportunity to improve your understanding of how to compute the intersection (or
elements in common) between two tuples that can contain an arbitrary number of
values each of an arbitrary type. You will also learn more about high-order
functions as you implement a program that can apply an arbitrary function to the
contents of an arbitrary length list of `int` values.

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
see two Python files called `compute-tuple-intersection.py` and
`perform-apply-to-each.py`. You can run the `compute-tuple-intersection.py`
program by typing `python compute-tuple-intersection.py` in your terminal
window. This program currently has several `TODO` markers asking you to add
source code from the text book to provide an implementation of a function with
the following signature: `def compute_intersection(tuple_one: Tuple[Any, ...],
tuple_two: Tuple[Any, ...]) -> Tuple[Any, ...]`. Once you have added all of the
required source code your program should produce the following output. Can you
explain why different calls to `compute_intersection` yield an output that
contains the same elements but in a different order?

```
The first tuple: (1, 'a', 2)
The second tuple: ('b', 2, 'a')

The first intersection tuple: ('a', 2)
The second intersection tuple: (2, 'a')
```

The second program in the `source` directory is called `perform-apply-to-each`.
Again, this program has several `TODO` markers that invite you to add source
code from the text book to finish the implementation of the function with the
signature `def apply_to_each(values: List[int], function: Callable) -> None`.
After you have added the required source code your program should produce the
following output. One interesting aspect of the `apply_to_each` function is that
it does not return any values, as indicated by the return type annotation of
`None`. If the function does not return a value, then how can it modify the
`values` input parameter of type `List[int]` as shown in the output? Finally,
you will note that `apply_to_each` accepts a `function` parameter of type
`Callable`, making it a higher-order function. What are the benefits of using
high-order functions in Python programs? How does `apply_to_each` use the
`function` parameter?

```
Values before transformations: [1, -2, 3.33]
Values after applying abs: [1, 2, 3.33]
Values after applying int: [1, 2, 3]
Values after applying squaring: [1, 4, 9]
```

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
source code produced that output. A specific goal for this project is to ensure
that you can explain each component of a function's type signature, including
details about its inputs and outputs.

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
