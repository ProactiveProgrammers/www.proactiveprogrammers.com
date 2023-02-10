# Tuple Swapping

## Project Goals

This assignment invites you to run and observe one Python program called
`perform-ordered-pair-swap`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a best
practice, this program is a script, without any dependencies on other Python
packages, that you can run through the Python interpreter. As you continue to
practice a different way to run a Python program, this project invites you to
explore how to (i) find and fix defects in a function and (ii) create and use
fixed-size tuples that can contain arbitrary types of data.

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
see a Python program called `perform-ordered-pair-swap.py`. Your goal for this
project is to find and fix the defects in the function with the signature `def
ordered_pair_swap(pair_one: Tuple[Any, Any], pair_two: Tuple[Any, Any]) ->
Tuple[Tuple[Any, Any], Tuple[Any, Any]]`. When you run the command `python
perform-ordered-pair-swap.py` after correcting the program's defects, it should
produce the following output:

```
Original tuple of ordered pairs: (('A', 1), ('B', 2))
Swapped tuple of ordered pairs: ((2, 'B'), (1, 'A'))
Swapped (again) tuple of ordered pairs: (('A', 1), ('B', 2))
```

It is worth noting that the `ordered_pair_swap` function performs two types of
swapping. It first swaps the values inside of each of the ordered pairs, as
evidenced in the first and second lines of the output, where the first tuple is
input as `('A', 1)` and output as `(1, 'A')`. The second type of swap performed
by the function involves outputting the second tuple first and the first tuple
second, which the second output line illustrating with `((2, 'B'), (1, 'A'))`
for an input of `(('A', 1), ('B', 2))`. The final line of the program output
also illustrates that the tuple swapping process is reversible since the
function can accept as input `((2, 'B'), (1, 'A'))` and produce as output
`(('A', 1), ('B', 2))` &mdash; which is the original tuple that started this the
tuple swapping process!

## Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage
project dependencies and virtual environments, it does not support the use of
commands like `poetry run task test`. However, you can leverage the relevant
instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about this project's program.

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
