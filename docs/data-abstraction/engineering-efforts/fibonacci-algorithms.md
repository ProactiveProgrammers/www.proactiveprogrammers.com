# Fibonacci Algorithms

## Project Goals

This assignment invites you to implement a program that features multiple
algorithms for computing the numbers in the Fibonacci sequence that is
recursively defined by the following equations for the $n$-th Fibonacci number
$F(n)$.

$$
F(0) = 0
$$

$$
F(1) = 1
$$

$$
F(n) = F(n-1) + F(n-2)
$$

This recursive definition of the Fibonacci sequences yields the values $0, 1, 1,
2, 3, 5, \ldots$ where the value of any Fibonacci number, denoted $F(n)$, is
computed by adding together $F(n-1)$ and $F(n-2)$ and the other starting values
are defined in the first two equations. Since there are different ways to
compute the values in the Fibonacci sequence, this project invites you to
implement and evaluate their performance.

Specifically, you will implement and experimentally evaluate the following
Fibonacci algorithms: (i) a `list`-based approach that uses iteration, (ii) a
`list`-based approach that uses recursion, (iii) a `tuple`-based approach that
uses iteration, and (iv) a `tuple`-based approach using recursion. Along with
adding source code to the provided Python files, you will conduct an experiment
to determine which algorithm is the fastest and aim to understand why it is the
best based on its choice of a data container (i.e., `list` or `tuple`) and its
algorithmic approach (i.e., `iterative` or `recursive`).

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

This project invites you to implement a Python program, called
`fibonaccicreator`, that features different ways to compute all of the numbers
in the Fibonacci sequence up to a specified maximum number. After you finish a
correct implementation of all the program's features, running it with the
command `poetry run fibonaccicreator --number 10 --approach recursivelist
--display`, it will produce output like the following.

```
🧳 Awesome, the chosen type of approach is the recursivelist!

🧮 The program will compute up to the 10th Fibonacci number!

✨ This is the output from the recursivelist function:

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   30.484375 megabytes

Estimated peak memory according to the operating system:
   38.78515625 megabytes

Estimated execution time according to the simple timer:
    0.01 seconds
```

This output shows that, for instance, the zeroth Fibonacci number is `0`, the
fifth Fibonacci number is `5`, and the tenth Fibonacci number is `55`. This
program output also shows the amount of memory consumed by the `recursive`
implementation of the Fibonacci calculation that stores the data in a `list`
that contains 11 values in it. Importantly, this output also shows that, since
the program had to compute so few of the numbers in the Fibonacci sequence, it
did so in an amount of time that was not measurable by the program's execution
timer. It is worth noting that if you run the `fibonaccicreator` to request a
different data container and algorithm combination with a command like `poetry
run fibonaccicreator --number 10 --approach iterativetuple --display` it should
produce the same numbers in the Fibonacci sequence. With that said, remember
that if you are running an experiment to evaluate the performance of
`fibonaccicreator` when it computes a large Fibonacci number, you should not use
the `--display` parameter since it will cause too much output to appear in your
terminal window.

Don't forget that you can display `fibonaccicreator`'s help menu and learn more
about its features by typing `poetry run fibonaccicreator --help` to show the
following output. This help menu shows that `fibonaccicreator` also has a
`--pyinstrument` flag that enables it to produce a web-based output that shows
the function calls made by the `fibonaccicreator` and the performance results
created by the [Pyinstrument](https://github.com/joerick/pyinstrument) package.

```
Usage: fibonaccicreator [OPTIONS]

  Create the list of Fibonacci values in a specified approach.

Options:
  --approach TEXT       [required]
  --number INTEGER      [required]
  --display             [default: False]
  --pyinstrument        [default: False]
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it
                        or customize the installation.

  --help                Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce the output displayed in this section. As the next
section explains, you should add the features needed to ensure that
`fibonaccicreator` produces the expected output!

???+ note

    Don't forget that if you want to run the `fibonaccicreator` program you must use
    your terminal window to first go into the GitHub repository containing this
    project and then go into the `fibonaccicreator` directory that contains the
    project's source code. Finally, remember that before running the program you
    must run `poetry install` to add its dependencies, such as Pyinstrument,
    Pytest, and Rich.

## Adding Functionality

If you study the file `fibonaccicreator/fibonaccicreator/main.py` you will see
that it has many `TODO` markers that designate the parts of the program that you
need to implement before `fibonaccicreator` will produce correct output. Once
you complete a task associated with a `TODO` marker, make sure that you delete
it and revise the prompt associated with the marker into a meaningful comment.
To ensure that the program works correctly, you must implement all of these
functions in the `fibonacci` module:

- `def fibonacci_recursivelist(number: int) -> List[int]`
- `def fibonacci_recursivetuple(number: int) -> Tuple[int, ...]`
- `def fibonacci_iterativetuple(number: int) -> Tuple[int, ...]`
- `def fibonacci_iterativelist(number: int) -> List[int]`

After finishing your implementation of `fibonaccicreator` you should conduct an
experiment to evaluate the efficiency of the different algorithms that it
provides. You should refer to the `writing/reflection.md` file for more details
about the experiment that you should conduct and how you must configure the
`fibonaccicreator` program to collect data. Ultimately, you need to answer the
following three research questions:

- Is the `fibonaccicreator` faster when it uses the `recursive` or the
  `iterative` method?
- Is the `fibonaccicreator` faster when it stores data in a `list` or a `tuple`
  data container?
- Which configuration of the `fibonaccicreator` is the most memory efficient?
- Overall, what is the fastest approach for computing and storing the Fibonacci
  sequence?
- Overall, are there modes of the `fibonaccicreator` that are less suitable for
  Python?

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black fibonaccicreator tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 fibonaccicreator tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy fibonaccicreator", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle fibonaccicreator tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint fibonaccicreator tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black fibonaccicreator tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `fibonaccicreator`. If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following. It is
worth noting that the name of the test suite is `test_fibonacci` because the
functions mentioned in the previous section exist in the `fibonacci` module.

```
collected 5 items

tests/test_fibonacci.py .....
```

This project comes with other tasks that you can run once you have used Poetry
to install all of the dependencies. For instance, if you find that your Python
source code is not in adherence with the required formatting rules, you can run
`poetry run task black` to automatically return it to the correct format! You
can also run commands like `poetry run task mypy` to check the program's use of
data types and `poetry run task pylint` to ensure that your source code adheres
to other established programming conventions. You can use these built-in tasks
to understand and improve your code's quality!

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
completing this project. A specific goal of the reflection for this project is
to evaluate the efficiency of the different algorithms and data containers
implemented as part of the `fibonaccicreator` program.

In addition to explicitly answering the aforementioned research questions,
please make sure that you explain why the performance trends are evident in your
data by referencing and explaining the source code that implements each of the
algorithms implemented in the `fibonaccicreator`. Once you have finished
addressing the prompts in the `writing/reflection.md` file that have `TODO`
makers given as reminders, make sure that you either delete the prompt or
carefully integrate a revised version of it into your writing.

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
specification.

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
