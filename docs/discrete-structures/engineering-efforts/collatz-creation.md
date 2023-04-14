---
tags:
  - Data Types
  - Data Visualization
  - Functions
  - Performance
  - Testing
---

![Collatz Creation](/img/Pro-Discrete-Structures-Collatz-Creation.svg){loading=lazy}

# Collatz Creation

## Project Goals

This engineering effort invites you to investigate how to apply all that
you have learned about Python programming and discrete structures to
implement a program, called `collatzcreation`, that can solve the
[Longest Collatz
Sequence](https://projecteuler.net/index.php?section=problems&id=014)
problem posed on [Project Euler](https://projecteuler.net/). The Collatz
sequence is defined for the positive integers according to the rule that
$n$ becomes $\frac{n}{2}$ when $n$ is even and $3n + 1$ when $n$ is odd.
To date, computer scientists and mathematicians do not know whether or
not the Collatz sequence will terminate with the value of $1$ when it is
started with an arbitrary positive integer $n$. However, for all of the
values tried to date the sequence always yields a Collatz chain (i.e.,
the sequence values that arise from iteratively applying the rules) of a
finite length. The Longest Collatz Sequence problem posed by Project
Euler asks "Which starting number, under one million, produces the
longest chain"? The `collatzcreation` program that you implement for
this project should efficiently produce an answer to this question.

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
    assignment!
    To get started, you should click the "Use this template" button in the
    :material-github:
    [collatz-creation-starter](https://github.com/ProactiveProgrammers/collatz-creation-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Expected Output

As part of this assignment, you are going to implement a
`collatzcreator` program that takes as input a complete document stored
in a text file and then performs an automated analysis of the document's
contents. If you run the `collatzcreator` program with the command
`poetry run collatzcreator --minimum 1 --maximum 10 --display` it will
try the numbers `1` through `10` as the input number to the Collatz
Sequence and then calculate the length of the Collatz chain before the
sequence produces the value of `1`. The `collatzcreator` program will
also compute some summary statistics about the length of the Collatz
chains that it constructed when using the inputs that start at the
`minimum` and go up to the `maximum`. When the `collatzcreator` accepts
the input flag of `--display` it will also produce a graph that will
visualize the relationship between the value of the numerical input and
the length of the Collatz chain.

```text
🕵  Let's investigate the behavior of the Collatz sequence!

  The first input to try will be 1
  The last input to try will be 10

The inputs to the Collatz function:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

✨ What is the length of the Collatz chain before the function produces
the value of 1?

📏 The length of the resulting Collatz chain:

[1, 2, 8, 3, 6, 9, 17, 4, 20, 7]

✨ What is the summary information about the length of the Collatz chain?

  The minimum length of a Collatz chain is: 1
  The maximum length of a Collatz chain is: 20
  The mean of the length of a Collatz chain is: 7.70
  The median of the length of a Collatz chain is: 6.50
  The standard deviation of the length of a Collatz chain is: 5.97

🤷 Can you find a pattern between the input number and the length of the
Collatz chain?

📦 Check the file called 'graphs/collatz.pdf' to see a graph that
visualizes the results!
```

???+ note

    Don't forget that if you want to run the `collatzcreator` you must use your
    terminal to first go into the GitHub repository containing this project and
    then go into the `collatzcreator` directory that contains the project's
    code. Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

If you study the file `collatzcreator/collatzcreator/main.py` you will see that
it contains a single `TODO` that reminds you to call the `compute_collatz_chain`
function that takes as input a specific number and returns an `Iterator[int]` as
its output. This means that the `compute_collatz_chain` function should use
`yield` to incrementally produce the `int` values in the Collatz sequence. When
you look at the `collatzcreator/collatzcreator/collatz.py` file you will notice
that the `TODO` marker instructs you to provide a complete implementation of the
aforementioned `compute_collatz_chain` function. Finally, a review of the
`collatzcreator/collatzcreator/summarize.py` will show that you also need to
implement the following functions that characterize the computed Collatz
sequences:

- `def compute_mean(numbers: List[int]) -> float:`
- `def compute_median(numbers: List[int]) -> float:`
- `def compute_difference(numbers: List[int]) -> List[float]:`
- `def compute_variance(numbers: List[int]) -> float:`
- `def compute_standard_deviation(numbers: List[int]) -> float:`

The following source code segment provides a complete implementation of the
`compute_collatz_chain` function. Line `3` of this function firsts `yield`s the
`number` since the first numerical value in the Collatz chain is always the
initially provided number. Next, lines `4` through `9` iteratively compute the
values in the Collatz sequence, continuing until the `number` takes on the value
of `1`. When `number` is even, lines `5` and `6` use the `//` operator to assign
to `number` to the integer value of `number / 2`. When `number` is odd, line `8`
assigns to `number` the value of `3 * number + 1`. Ultimately, the
`compute_collatz_chain` function follows the sequence's definition by which $n$
becomes $\frac{n}{2}$ when $n$ is even and $3n + 1$ when $n$ is odd, only
terminating when the value of $n$ is $1$.

```python linenums="1"
def compute_collatz_chain(number: int) -> Iterator[int]:
    """Compute the numbers in the Collatz sequence for the starting number."""
    yield number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        yield number
```

Finally, don't forget that the [Longest Collatz
Sequence](https://projecteuler.net/index.php?section=problems&id=014) problem
posed on [Project Euler](https://projecteuler.net/) is "Which starting number,
under one million, produces the longest chain"? This means that you will need to
run the program with the following command-line arguments: `poetry run
collatzcreator --minimum 1 --maximum 1000000 --display`. It is important to note
that it is possible that running `collatzcreator` on your laptop with these
command-line arguments may require a significant amount of computation time.
This means that you will either have to wait a long time for `collatzcreator` to
finish or implement a more efficient version of the `compute_collatz_chain`
function! Which approach did you pick?

## Running Checks

As you continue to add and confirm the correctness of `collatzcreator`'s
functionality, you should study the source code in the `pyproject.toml` file.
This file contains the specification of several tasks that will help you to
easily run checks on your Python source code. Now, you can run commands like
`poetry run task lint` to automatically run all of the linters designed to check
the Python source code in your program and its test suite. You can also use the
command `poetry run task black` to confirm that your source code adheres to the
industry-standard format defined by the `black` tool. If it does not adhere to
the standard then you can run the command `poetry run fixformat` and it will
automatically reformat the source code. By following a
[tutorial](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0),
you can configure VS Code to use the `black` tool to automatically reformat the
source code when you save a file.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to run the command
`gatorgrade --config config/gatorgrade.yml` to check your work. If your work
meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. You can study the `config/gatorgrade.yml` file in your repository
to learn how the :material-github:
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program runs
:material-github: [GatorGrader](https://github.com/GatorEducator/gatorgrader)
to automatically check your program and technical writing. You can also run the
command `poetry run task test` to run the Pytest test suites provided in the
files `test_collatz.py` and `test_summarize.py`. Did all of your tests pass?

???+ note

    Don't forget that when you commit source code or technical writing to your
    GitHub repository for this project, it will trigger the run of a GitHub
    Actions workflow. If you are a student at Allegheny College, then running
    this workflow consumes build minutes for the course's organization! As such,
    you should only commit to your repository once you have made substantive
    changes to your project and you are ready to confirm its correctness. Before
    you commit to your repository, you can should run checks on your own computer
    by running `gatorgrade --config config/gatorgrade.yml`.

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project. One of the main goals of the reflection is for you to
explain the trends that you see in the different provided text files. You should
also discuss how the `collatzcreator` program uses discrete structures like the
list and the set to automatically characterize the text of a complete document.

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](/proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet every aspect of the project's
specification.

???+ note

    Before you finish all of the required deliverables required by this project is
    worth pausing to remember that the instructor will give advance feedback to
    any learner who requests it through GitHub and Discord at least 24 hours
    before the project's due date! Seriously, did you catch that? This policy
    means that you can have a thorough understanding of ways to improve your
    project **before** its final assessment! To learn more about this
    opportunity, please read the [assessment
    strategy](../../../proactive-learning/assessment-strategy/) for this site.

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
