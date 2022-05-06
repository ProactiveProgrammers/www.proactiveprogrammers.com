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
see two Python programs called `create-dog-with-dictionary.py` and
`create-dog-with-list.py`. Importantly, both of these Python programs should
produce the same output! Your goal for this project is to add the source code
required by the `TODO` markers so that the program produces the output that is
given below this paragraph. When you are finished adding the required source
code, both of the aforementioned programs should produce the following output.
With that said, the first line produced by `create-dog-with-dictionary` should
be `Creating dog objects using a dictionary-based approach!` and the first line
produced by `create-dog-with-list.py` should be `Creating dog objects using a
list-based approach!`. As you implement both of these approaches to representing
objects, please take time to reflect on the relative strengths and weaknesses of
both ways to store details about a `Dog` in the computer's memory.

```text
The dog's name is: Bosco
The dog's age is: 6
The dog's breed is: Havanese

The dog's name is: Faith
The dog's age is: 14
The dog's breed is: Havanese
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
encouraged to ensure that `create-dog-with-dictionary` and
`create-dog-with-list` both produce the same output, excepting the fact that
they both output a starting line that is specific to the kind of representation
that they use for the `Dog` object. Finally, you should confirm that the
`create-dog-with-class` program produces similar output to the two
aforementioned programs while also further demonstrating the features that are
unique to this approach.

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
