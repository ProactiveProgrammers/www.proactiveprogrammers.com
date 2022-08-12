![Numerical Data](/img/Pro-Data-Abstraction-Numerical-Data.svg){loading=lazy}

# Numerical Data

## Project Goals

This assignment invites you to run and observe two Python programs called
`determine-even-odd` and `floating-point-confusion`. Instead of using the
[Poetry](https://python-poetry.org/) tool for managing dependencies and
packaging these programs, which the [technical
skills](/proactive-skills/introduction-proactive-skills/) advise as a best
practice, these programs are scripts, without any dependencies on other Python
packages, that you can run through the Python interpreter. As you learn a new
way to run a Python program, this project offers you the opportunity to ensure
that you understand how to (i) use the modular arithmetic operation (i.e., `%`)
to determine if a number is even or odd and (ii) correctly multiply and add
with float-point variables.

## Project Access

If you are a student enrolled in a Computer Science class at Allegheny College,
you can access this assignment by clicking the link provided to you in Discord.
Once you click this link it will create a GitHub repository that you can clone
to your computer by following the general-purpose instructions in the
description of the [technical
skills](/proactive-skills/introduction-proactive-skills/). Specifically, you
will need to use the `git clone` command to download the project from GitHub to
your computer. Now you are ready to add source code and documentation to the
project so that you can refine your understanding of how to process numerical
data in Python!

## Code Survey

If you change into the `source/` directory of your GitHub repository, you will
see two Python files called `determine-even-odd.py` and
`floating-point-confusion.py`. You can run the `determine-even-odd.py` program
by typing `python determine-even-odd.py` in your terminal window. What output
does the program produce? Can you explain why it produces this output? The key
to understanding this segment of source code is to notice that line `1` uses the
modular arithmetic operation, written as `%`, to compute the remainder that
results from dividing the variable called `value` by `2`. If `2` divides `value`
evenly, then the remainder will be `0` and this code segment concludes that the
number is even. However, if the remainder resulting from dividing `value` by `2`
is not equal to `0`, then there is clear evidence that `value` is odd.

```python linenums="1"
if value % 2 == 0:
    return "even"
else:
    return "odd"
```

The second program is called `floating-point-confusion.py` because it
illustrates some of the initially confusing aspects of using Python's `float`
data type to store decimal values. To understand this program better, it is
important to note that lines `1` and `2` in the following segment illustrate the
respective use of addition and multiplication with float-point numbers. You can
run this program by typing `python floating-point-confusion.py` in your
terminal. Can you explain why it produces this output and what it reveals about
the challenges of doing arithmetic with float-point numbers?

```python linenums="1"
for _ in range(10):
    number = number + 0.1
multiply_number = 10.0 * 0.1
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
that you can explain how Python programs should correctly use modular arithmetic
and floating point numbers to achieve a practical goal.

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
