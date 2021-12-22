# Knapsack Solvers

## Project Goals

This assignment invites you to study, repair, and test a Python programs called
`demonstrate-knapsack-solvers`. The 0/1 Knapsack problem requires a computer
program to determine which items to pick, from a list of items with both costs
and benefits, in order to maximize the benefits while ensuring that the costs do
not exceed a specified maximum cost. As part of this source code survey you will
will implement and run three different greedy solvers called greedy-by-density,
greedy-by-weight, and greedy-by-value that vary in the way in which they select
items. You will also implement and run an exhaustive 0/1 knapsack solver that is
guaranteed to find the optimal solution for a specific problem instance. With
that said, this exhaustive solver must generate the powerset of the set of all
items and is thus only efficient for small knapsack instances. After running all
three of the greedy solvers and then exhaustive solver you will be able to
determine which greedy approach is best suited for the problem instance.

## Project Access

If you are a student enrolled in a Computer Science class at Allegheny College,
you can access this assignment by clicking the link provided to you in Discord.
Once you click this link it will create a GitHub repository that you can clone
to your computer by following the general-purpose instructions in the
description of the [technical
skills](/proactive-skills/introduction-proactive-skills/). Specifically, you
will need to use the `git clone` command to download the project from GitHub to
your computer. Now you are ready to add source code and documentation to the
project and then run the program to learn more about the efficiency and
effectiveness trade-offs associated with different implementations of 0/1
knapsack solvers!

## Code Survey

If you change into the `source/` directory of your GitHub repository, you will
see one Python file called `demonstrate-knapsack-solvers.py`. The
`demonstrate-knapsack-solvers` module contains an incomplete class definition
written as `class Item(object):`. You need to follow the `TODO` markers in this
class definition, by inputting the source code from the text book, for functions
like the constructor `def __init__(self, n, v, w)` and like accessor functions
such as `def get_name(self) -> str`, `def get_value(self) -> int`, `def
get_weight(self) -> int`. Since your textbook does not provide an implementation
of a function for generating the powerset of a set, you will also need to
consult the references in the source code and create your own function. Finally,
you will need to implement the function that uses the generated powerset to
perform an exhaustive search of all possible combinations of input.

To ensure that the `demonstrate-knapsack-solvers.py` script analyzes the same
instance of the 0/1 knapsack problem as is found in the textbook, you should use
the following `build_items` function that is also available in the provided
source code. Lines `3` through `5` of this function respectively create the
input to the knapsack solver that includes the name of the item and its value
and weight (i.e., its cost). The `List` of `Item` objects returned from this
function will be processed by both the greedy and exhaustive solvers.

```python linenums="1"
def build_items() -> List[Item]:
    """Create an instance of a 0/1 knapsack using instances of Item."""
    names = ["Clock", "Painting", "Radio", "Vase", "Book", "Computer"]
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items: List[Item] = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items
```

After you have addressed all of the `TODO` markers inside of the provided source
code, you can run the program by typing the command `python
demonstrate-knapsack-solvers.py` as long as you have changed into the `source/`
directory. If you correctly implemented the program and provided all of the
source code required by the `TODO` markers it should produce the following
output. It is important to note that, at least for this instance of the 0/1
knapsack problem, the `greedy-by-density` greedy solver produces the solution
that is closest to the optimal one given by the exhaustive solver. It is
important to note that, at least for this instance of the 0/1 knapsack problem,
the `greedy-by-density` solver produces the solution that is closest to the
optimal one given by the exhaustive solver.

```text
Running all of the knapsack solvers!

Using greedy-by-value to fill knapsack of size 20
Total value of items taken is 200.0
   (Computer, 200, 20)

Using greedy-by-weight to fill knapsack of size 20
Total value of items taken is 170.0
   (Book, 10, 1)
   (Vase, 50, 2)
   (Radio, 20, 4)
   (Painting, 90, 9)

Using greedy-by-density to fill knapsack of size 20
Total value of items taken is 255.0
   (Vase, 50, 2)
   (Clock, 175, 10)
   (Book, 10, 1)
   (Radio, 20, 4)

Generating the powerset of all items!

Using exhaustive enumeration to fill a knapsack of size 20
Total value of items taken is 275.0
   (Clock, 175, 10)
   (Painting, 90, 9)
   (Book, 10, 1)
```

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
source code produced that output. A specific goal for this project is to ensure
that you can explain the defects that you found in the function and identify all
of the key components of a test case. You should also reflect on how the tests
that you created as part of this source code survey are similar to and different
from the ones you might create with a framework like
[Pytest](https://docs.pytest.org/).

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
