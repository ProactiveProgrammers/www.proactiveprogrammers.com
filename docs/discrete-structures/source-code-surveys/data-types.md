---
tags:
  - Conditional Logic
  - Data Types
  - Exponentiation Operator
  - Floating Point
  - Iteration Constructs
---

![Discrete Structures](/img/Pro-Discrete-Structures-Data-Types.svg){loading=lazy}

# Data Types

## Project Goals

This assignment invites you to run and observe two Python programs called
`compare-variables` and `demonstrate-variable-limitations`. Instead of using
the [Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a best
practice, these programs are scripts, without any dependencies on other Python
packages, that you can run through the Python interpreter. As you learn a new
way to run a Python program, this project offers you the opportunity to ensure
that you understand how to (i) understand the representation of float-point
variables and (ii) the time and space limitations associated with performing
computations with numbers. Ready to explore some of the limitations of data
variables in Python? *Okay, let's get started!*

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
    [numerical-data-starter](https://github.com/ProactiveProgrammers/numerical-data-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Code Survey

If you change into the `source` directory of your GitHub repository, you will
see two Python files called `compare-variables.py` and
`demonstrate-variable-limitations.py`. You can run the `compare-variables.py`
program by typing `python compare-variables.py` in your terminal window. What
output does the program produce? Can you explain why it produces this output?
The key to understanding this segment of source code is to notice that the
conditional logic in lines `1` through `4` use a programmer's decimal
approximation of $\frac{1}{3}$ while lines `5` through `8` use the fraction
itself.  What does this output tell you about the difference between `.33333`
and `(1/3)` in the Python language?

```python linenums="1"
if .33333 + .33333 + .33333 == 1:
    print(".33333 + .33333 + .33333 is equal to 1")
else:
    print(".33333 + .33333 + .33333 is not equal to 1")
if (1/3) + (1/3) + (1/3) == 1:
    print("1/3 + 1/3 + 1/3 is equal 1")
else:
    print("1/3 + 1/3 + 1/3 is not equal 1")
```

The second Python program is called `demonstrate-variable-limitations.py`
because it uses the exponentiation operator, written as `**`, to raise different
numbers to different powers. As shown on line `1` in the following excerpt from
this program, it is feasible to efficiently perform the computation `2**2**8`,
written as $2^{2^8}$ using mathematical notation. Line `3` also shows that it is
possible to efficiently compute the value of $2^{2^{10}}$ using the Python
expression `2**2**10`. Although not shown in the following source code segment,
the `demonstrate-variable-limitations.py` script also has commented-out source
code that performs the computation `2**2**100`. If you un-comment this source
code and run the program by typing `python floating-point-confusion.py` what
does the output tell you about the challenges of efficiently performing
exponentiation?

```python linenums="1"
feasible_number = 2**2**8
print(f"The value of a feasible number is {feasible_number}")
another_feasible_number = 2**2**10
print(f"The value of another feasible number is {another_feasible_number}")
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

???+ note

    Did you know that :material-github:
    [GatorGrade](https://github.com/GatorEducator/gatorgrade) and
    :material-github:
    [GatorGrader](https://github.com/GatorEducator/gatorgrader) are open-source
    Python programs implemented by [Proactive
    Programmers](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/graphs/contributors)?
    If you finish this source code survey and have extra time, please brainstorm
    some new features that you think these two tools should have, explain your
    idea by raising an issue in the relevant project's GitHub repository, and
    take the first step towards implementing and testing your idea. If the
    maintainers of these tools accept your new feature then you will have helped
    to improve the experience of other people who use GatorGrade and
    GatorGrader!

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. Since
this is a source code survey, you should provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is to ensure
that you can explain how Python programs should use integer numbers and
exponentiation in an efficient and correct fashion.

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
