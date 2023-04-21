---
tags:
  - Conditional Logic
  - Data Types
  - Iteration Constructs
  - Functions
  - Type Annotations
---

![Matrix Processing](/img/Pro-Data-Abstraction-Matrix-Processing.svg){loading=lazy}

# Matrix Processing

## Project Goals

This project invites you to implement a `matrix` program that processes a
two-dimensional "list of lists" called a matrix. The main feature of the program
is that it can count the number of negative numbers inside of a matrix that it
inputs from a file specified on its command-line. In addition to implementing
part of the command-line interface for `matrix` you will add source code that
traverses the input matrix and counts the negative numbers. As you enhance your
[technical skills](/proactive-skills/introduction-proactive-skills/) by
implementing and documenting a Python program, you will continue to explore
tools such as VS Code and a terminal window and the Python programming language
and the Poetry package manager.

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
    [matrix-starter](https://github.com/ProactiveProgrammers/matrix-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Expected Output

As previously mentioned, this project invites you to implement a matrix
processing program program called `matrix`. The program accepts through its
command-line interface a `matrix-file` parameter that designates a file with a
matrix inside of it and the `matrix-dir` that is the directory containing the
specified file. For this project, you should use the `matrix.txt` file inside of
the `input` directory that contains these contents:

```
100,19,9,9
10,9,8,7
6,4,2,-1
4,2,0,-1
3,0,-1,-2
-1,-1,-2,-5
```

After correctly adding all of the required features, you can use Poetry to run
the program with the command `poetry run matrix --matrix-dir input --matrix-file
matrix.txt` and see that it it produces the following output:

```
✨ Searching for negative numbers in a matrix stored in input/matrix.txt!

📦 The matrix contains the following integer values:

---  --  --  --
100  19   9   9
 10   9   8   7
  6   4   2  -1
  4   2   0  -1
  3   0  -1  -2
 -1  -1  -2  -5
---  --  --  --

🧮 The matrix contains 8 negative numbers!
```

To learn more about how to run this program, you can type the command `poetry
run matrix --help` to see the following output showing how to use `matrix`:

```
Usage: matrix [OPTIONS]

  Read in a matrix and count the number of negative numbers.

Options:
  --matrix-dir PATH
  --matrix-file PATH
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it
                        or customize the installation.

  --help                Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add the missing features and ensure that `matrix` produces the
expected output. Once the program is working correctly, it should produce output
similar to that shown in this section.

???+ note

    Don't forget that if you want to run the `matrix` program you must use
    your terminal to first go into the GitHub repository containing this project
    and then go into the `matrix` directory that houses the project's code.
    Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

If you study the file `matrix/matrix/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `matrix` will produce correct output. Specifically, you should
implement these functions in `matrix`:

- `def confirm_valid_file(file: Path) -> bool`
- `def count_negatives_in_matrix(matrix: List[List[int]]) -> int`
- `def matrix(matrix_dir: Path = typer.Option(None), matrix_file: Path = typer.Option(None)) -> None`

Once you have correctly resolved all of the `TODO` markers in the `matrix`
program, it should produce the expected output described in the previous
section. The most important function you need to implement for this project is
`count_negatives_in_matrix`, which has a signature indicating that it accepts as
input a `List` of `List`s that contain `int` values (i.e., `List[List[int]]`)
and returns as output an `int` for the number of negative numbers in the file.
You may assume that the `matrix` parameter that is input to the
`confirm_valid_file` function is organized such that each row and column of the
`matrix` is sorted in a non-increasing order.

The following excerpt of output created by a correct implementation of `matrix`,
which was produced through the use of the
[python-tabulate](https://github.com/astanin/python-tabulate) package,
illustrates the organization of the input matrix. For instance, note that the
first column of the matrix contains the values `100, 10, 6, 4, 3, -1` which are
organized in a non-increasing manner from the top to the bottom of the matrix.
It is also worth noting that all of the other column in the matrix are also
organized in the same non-increasing fashion. Moreover, the third-from-the-top
row of the matrix contains the values `6, 4, 2, -1` while the last row contains
`-1, -1, -2, -5` which are also organized in a non-increasing style.

```
---  --  --  --
100  19   9   9
 10   9   8   7
  6   4   2  -1
  4   2   0  -1
  3   0  -1  -2
 -1  -1  -2  -5
---  --  --  --
```

???+ note

    Before you start to implement the source code required by this project is
    worth pausing to remember that the instructor will give advance feedback to
    any learner who requests it through GitHub and Discord at least 24 hours
    before the project's due date! Seriously, did you catch that? This policy
    means that you can have a thorough understanding of ways to improve your
    project **before** its final assessment! To learn more about this
    opportunity, please read the [assessment
    strategy](../../../proactive-learning/assessment-strategy/) for this site.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black matrix tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 matrix tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy matrix", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle matrix tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint matrix tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black matrix tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run `gradle grade` to check your work. If `gradle grade` shows
that all checks pass, you will know that you made progress towards correctly
implementing and writing about `matrix`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite passes and produces
output like this:

```shell
collected 3 items

tests/test_matrix.py ....
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

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented and tested, compare and contrast the performance of different
implementations of the matrix processing algorithm, and answer all of the other
questions about your experiences in completing this project.

## Project Assessment

Since this is a programming project, it is aligned with the **applying** and
**analyzing** levels of [Bloom's taxonomy](/proactive-learning/blooms-taxonomy/).
You can learn more about how a proactive programming expert will assess your
work by examining the [assessment
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
