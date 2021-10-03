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

If you study the file `matrix/matrix/main.py` you will see that it has
many `TODO` markers that designate the parts of the program that you need to
implement before `matrix` will produce correct output. In summary, you
should implement the following functions for the `matrix` program:

- `def compute_square_root_exhaustive(x: int, epsilon: float = 0.01) -> Tuple[bool, float, int]`
- `def compute_square_root_efficient(x: int, epsilon: float = 0.01) -> Tuple[bool, float, int]`

Importantly, you will notice that both `compute_square_root_efficient` and
`compute_square_root_exhaustive` accept the same types of inputs and produce the
same types of outputs. In particular, the parameter called `x` is the number
whose square root the function will compute and `epsilon` is the tolerance
parameter describing how close the approximation of `x`'s square root must be.
The notation `Tuple[bool, float, int]` that describes the output of these
functions shows that they each return three values. The first variable in the
return value is a `bool` indicating whether or not the function found an answer
within the tolerance of `epsilon`. Finally, the second returned variable is a
`float` for the calculated value of the square root and the third one is an
`int` for the number of guesses that the algorithm took.

You will also notice that there are some `TODO` markers in the `matrix`
function of the `main` module. In the scope of the conditional logic statement
`if approach.value == matrixCalculationingApproach.efficient` on lines `1`
through `7`, the program should call the function
`compute_square_root_efficient` depending on whether the `profile` variable
specified on the command-line is `True` or `False`. If `profile` is `True`, then
the program should use Pyinstrument to measure its execution time, as
illustrated on lines `3` through `5`. However, if `profile` is `False`, then the
program should only call the `compute_square_root_efficient` as shown on line
`7`. As lines `9` through `15` show, the function should take analogous steps
for its `exhaustive` mode, calling the `compute_square_root_exhaustive` instead
of `compute_square_root_efficient`.

```python linenums="1"
if approach.value == matrixCalculationingApproach.efficient:
    if profile:
        profiler.start()
        square_root_tuple = compute_square_root_efficient(number)
        profiler.stop()
    else:
        square_root_tuple = compute_square_root_efficient(number)
# use the exhaustive square root computation algorithm
elif approach.value == matrixCalculationingApproach.exhaustive:
    if profile:
        profiler.start()
        square_root_tuple = compute_square_root_exhaustive(number)
        profiler.stop()
    else:
        square_root_tuple = compute_square_root_exhaustive(number)
```

Once you have correctly resolved all of the `TODO` markers in the `matrix`
program, it should produce the expected output described in the previous
section. With that said, please bear in mind that, when running `matrix`
with the `--profile` flag it will produce different profiling data depending on
the performance of your computer.

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
implementations of the square root calculation, and answer all of the other
questions about your experiences in completing this project.

## Project Assessment

Since this is a programming project, it is aligned with the **applying** and
**analyzing** levels of [Bloom's taxonomy](proactive-learning/blooms-taxonomy/).
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
