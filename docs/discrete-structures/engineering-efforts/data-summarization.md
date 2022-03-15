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

## Expected Output

This project invites you to implement a data summarization program called
`datasummarizer`. The `datasummarizer` program takes as input a file of floating
point values and computes their arithmetic mean. Here is an excerpt from the
`input/data.txt` file that contains the floating-point values that the
`datasummarizer` must summarize:

```
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

```
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

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section section of tasks that use
[taskipy](https://github.com/illBeRoy/taskipy):

```toml
[tool.taskipy.tasks]
black = { cmd = "black datasummarizer tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 datasummarizer tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy datasummarizer", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle datasummarizer tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint datasummarizer tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to
automatically run all of the linters designed to check the Python source code in
your program and its test suite. You can also use the command `poetry run task
black` to confirm that your source code adheres to the industry-standard format
defined by the `black` tool. If it does not adhere to the standard then you can
run the command `poetry run black datasummarizer tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task list`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `datasummarizer`. If your program has
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
    you commit to your repository, you can still run checks on your own computer
    by either using Poetry or Docker and GatorGrader.

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
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
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
