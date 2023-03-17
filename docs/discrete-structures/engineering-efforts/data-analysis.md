---
tags:
  - Conditional Logic
  - File I/O
  - Functions
  - Statistics
  - Testing
---

![Data Analysis](/img/Pro-Discrete-Structures-Data-Analysis.svg){loading=lazy}

# Data Analysis

## Project Goals

This engineering effort invites you to extend your knowledge about the basics of
data analysis to implement a program that can statistically analyze a data set
of real-world population records. After you finish the `dataanalysis` program it
will compute the summary statistics (e.g., mean, median, and standard deviation)
of population data from from 1970 until 2019. As you enhance your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will continue to
program with tools such as VS Code and both the Python programming language and
the Poetry package manager. Ultimately, your goal for this project is to create
a program that can efficiently process real-world data about human population
size.

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
    To get started, you should click the "Use this template" icon in the
    :material-github:
    [data-analysis-starter](https://github.com/ProactiveProgrammers/data-analysis-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Expected Output

This project invites you to implement a data summarization program called
`dataanalysis`. The `dataanalysis` program takes as input a file of floating
point values and computes summary statistics about the numbers. Before you
continue to work on this assignment, please make sure that you understand the
meaning of the data in this file. To accomplish this task, you should examine
the discussion of this data set, including its visualization from 1970 until
2019, from the [Residential Population in Crawford County,
PA](https://fred.stlouisfed.org/series/PACRAW0POP) from the [Federal Reserve
Bank of St. Louis](https://fred.stlouisfed.org/). The main goal for this program
is that it should summarize the population data for Crawford County, the county
in which Allegheny College is located. Here is an excerpt from the
`input/data.txt` file that contains the real-world population data values that
the `dataanalysis` program must summarize:

```
1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
1975-01-01,87.000
1976-01-01,87.600
1977-01-01,87.600
1978-01-01,88.000
1979-01-01,88.100
1980-01-01,88.869
```

As this example indicates, the numbers in this file are either strings, that
should be interpreted as a date, or a floating-point value, that is a recording
of a population estimate of people living in Crawford County. After you have
studied and understood the structure of this file's contents, you are ready to
install the project's dependencies with the command `poetry install` and then
run it with the command `poetry run dataanalysis --data-file input/data.txt`.
After you running the program you can use its output and the data visualization
available from the Federal Reserve Bank of St. Louis to better understand the
population trends for Crawford County. Finally, it is worth noting that the
numerical output from the `dataanalysis` program contains four properly indented
floating-point values that are always rounded to two decimal places.

```
📦 The data file contains 50 data values in it!

🚀 Let's do some sophisticated data analysis!

🧮 Here are the results of the data analysis:

    The computed mean is 87.80!
    The computed median is 88.05!

    The computed variance is 3.69!
    The computed standard deviation is 1.92!

💡 What does this tell you about the population of this city?
```

???+ note

    Don't forget that if you want to run the `dataanalysis` you must use your
    terminal to first go into the GitHub repository containing this project and
    then go into the `dataanalysis` directory that contains the project's code.
    Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

If you study the file `dataanalysis/dataanalysis/main.py` you will see that it
has many `TODO` markers that designate the parts of the program that you need to
implement before `dataanalysis` will produce the correct output. If you run the
provided test suite with the command `poetry run task test` or you try to run
the program with the command `poetry run dataanalysis --data-file
input/data.txt` you will see an error message in your terminal window. This is
due to the fact that there are key parts of this program that are missing! In
addition to implementing the program's `main` function you also need to
correctly `import` the correct modules and objects, like `typer`. Along with
adding command-line features to the `main` function in the `main` module, you
need to provide an implementation of the following functions in other provided
Python files:

- `def compute_mean(numbers: List[float]) -> float`
- `def compute_median(numbers: List[float]) -> float`
- `def compute_difference(numbers: List[float]) -> List[float]`
- `def compute_variance(numbers: List[float]) -> float`
- `def compute_standard_deviation(numbers: List[float]) -> float`

It is worth noting that, when appropriate, one of the aforementioned functions
can call another function. For instance, the `compute_standard_deviation` can
call the `compute_variance`, thereby reusing its code and avoiding unnecessary
code duplication. In summary, you must follow all of the instructions next to
the `TODO` markers in the provided source code to implement a program that can
correctly compute the arithmetic mean of the provided data values in the
`dataanalysis/input/data.txt` file. In addition to ensuring that your program is
adequately documented, has the correct industry-standard format, and adheres to
the industry best practices Python programming, you must implement functions
that pass a provided Pytest test suite.

If you look in the files called `test_transform.py` and `test_summarize.py` you
will find the test suites for the `transform` and `summarize` modules. As you
complete your implementation of `dataanalysis` you should repeatedly run these
tests, as explained in the next subsection, to confirm that your program's
functions are working correctly. Your program should both produce the correct
output and the pass the test suite!

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
important to note that `dataanalysis` comes with two test suites, both of
which should pass so as to establish a confidence in the correctness of the
program.

```
collected 13 items

tests/test_summarize.py ...........
tests/test_transform.py ..
```

???+ note

    When you are adding functionality to the `dataanalysis` program, make sure
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

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project. The reflection's objective is to invite you to explain
the Python functions for data summarization and transformation. As part of this
project's reflection you should also consider what technical skills taught in
the field of computer science will continue to be the most relevant in the
future.

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
