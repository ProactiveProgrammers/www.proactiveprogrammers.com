---
tags:
  - Conditional Logic
  - File I/O
  - Functions
  - Numerical Computation
  - Testing
---

![Data Summarization](/img/Pro-Discrete-Structures-Data-Summarization.svg){loading=lazy}

# Data Summarization

## Project Goals

This engineering effort invites you to combine what you learned about the basics
of Python programming and data analysis to implement a useful program that can
summarize a list of floating-point data values stored in a file. However, the
first step towards summarizing the data correctly requires the program to
transform the input data values from a text-based format to a numerical
representation. Along with learning more about how to implement data
transformation and summarization routines you will also explore the basics of
writing your own test cases. As you enhance your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will continue to
program with tools such as VS Code and a terminal window and both the Python
programming language and the Poetry package manager.

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
    [data-summarization-starter](https://github.com/ProactiveProgrammers/data-summarization-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Expected Output

This project invites you to implement a data summarization program called
`datasummarizer`. The `datasummarizer` program takes as input a file of floating
point values and computes their arithmetic mean. Here is an excerpt from the
`input/data.txt` file that contains the floating-point values that the
`datasummarizer` must summarize:

```text
2.5169521900e+0
1.8703141360e+0
-3.4505452520e-2
2.3580068020e+0
1.5516879500e+0
```

As this example indicates, these numbers are floating-point values. Can you
explain why these floating point numbers are written as, for instance,
`2.5169521900e+0`? After you have studied and understood the contents of this
file, you are ready to install the project's dependencies with the command
`poetry install` and then run it with the command `poetry run datasummarizer
--data-file input/data.txt`. Specifically, you will know that your
`datasummarizer` works correctly when it outputs the computed mean as
`0.9919614640914002`. If you did not get this answer, then please confirm the
correctness of your functions for data transformation and summarization.

```text
🔬 The data file contains 100 data values in it! Let's get summarizing!

🧮 The computed mean is 0.9919614640914002!
```

???+ note

    Don't forget that if you want to run the `datasummarizer` you must use your
    terminal to first go into the GitHub repository containing this project and
    then go into the `datasummarizer` directory that contains the project's
    code. Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

If you study the file `datasummarizer/datasummarizer/main.py` you will see that
it has many `TODO` markers that designate the parts of the program that you need
to implement before `datasummarizer` will produce correct output. If you run the
provided test suite with the command `poetry run task test` or you try to run
the program with the command `poetry run datasummarizer --data-file
input/data.txt` you will see an error message in your terminal window. This is
due to the fact that there are key parts of this program that are missing! In
addition to implementing the program's main functions you also need to correctly
`import` the correct modules and objects, like `typer`.

Since the `datasummarizer` program takes as input textual values from an input
file, you will need to implement a data transformation function that can take as
input a string that contains a numerical value on each line and returns a list
of floating-point values suitable for input into a mathematical computation. For
your reference, here is the signature of the `transform_string_to_number_list`
function:

`def transform_string_to_number_list(data_text: str) -> List[float]`

You program also needs to contain a data summarization function that can take as
input a list of floating-point values and then return a single floating-point
value that corresponds to the arithmetic mean of the values in the list. As you
are implementing this function, please ensure that your function can handle
without crashing an empty list of numerical values, returning a "not a number"
(i.e., `NaN`) designator in this situation. Here is the signature of the
`compute_mean` function that you must implement:

`def compute_mean(numbers: List[float]) -> float`

In summary, you must follow all of the instructions next to the `TODO` markers
in the provided source code to implement a program that can correctly compute
the arithmetic mean of the provided data values in the
`datasummarizer/input/data.txt` file. In addition to ensuring that your program
is adequately documented, has the correct industry-standard format, and adheres
to the industry best practices Python programming, you must implement functions
that pass a provided Pytest test suite.

If you look in the files called `test_transform.py` and `test_summarize.py` you
will find the test suites for the `transform` and `summarize` modules. As you
complete your implementation of `datasummarizer` you should run these tests, as
explained in the next subsection, to confirm that your program's functions are
working correctly. Ultimately, it is important for both your program to produce
the correct output and the test suite to pass!

???+ note

    When you are adding functionality to the `datasummarizer` program, make sure
    that you work in an incremental fashion, adding a small feature to the
    system and then confirming that it works correctly through linting, testing,
    and running the program. Once you have added this feature and confirmed that
    it works correctly, you should commit your source code to your GitHub
    repository and confirm that you have improved the build status of your
    project. As you are committing your source code, please pay careful
    attention to the commit message that you write! Specifically, you should
    make sure that your commit message features a sentence with an active verb
    and a clear description of the way in which you changed the source code. You
    can read the article [How to Write a Git Commit
    Message](https://cbea.ms/git-commit/) by [Chris Beams](https://cbea.ms/) to
    learn some suggestions for ways to improve the quality of your Git commit
    messages.

## Running Checks

As you continue to add and confirm the correctness of `datasummarizer`'s
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
to automatically check your program and technical writing. If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following. It is
important to note that `datasummarizer` comes with two test suites, both of
which should pass so as to establish a confidence in the correctness of the
program.

```
collected 6 items

tests/test_summarize.py ....
tests/test_transform.py ..
```

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
completing this project. The reflection's objective is to invite you to explain
the Python functions for data summarization and transformation.

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
