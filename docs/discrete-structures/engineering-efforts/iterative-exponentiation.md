# Iterative Exponentiation

## Project Goals

This engineering effort invites you to combine what you learned about the basics
of Python programming to implement a program that can use a `for` loop and/or a
`while` loop to perform a series of exponentiations. The function that you will
implement will repeatedly perform an exponentiation and then save the result of
the computation in the list. Ultimately, the output of the program should
confirm that it is possible to use either a `for` loop or a `while` loop to
produce the same program output! As you learn more about how to translate
mathematical equations into Python functions and you continue to enhance your
[technical skills](/proactive-skills/introduction-proactive-skills/), you will
implement and test a complete Python program while using tools such as the VS
Code text editor, a terminal window, and the Poetry package manager.

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

Perhaps the best way to understand the meaning of these terms is to observe the
output of a completed version of the program. For instance, the command `poetry
run python iterator --forloop --whileloop --minimum 0 --maximum 2` produces the
following output. Can you see the pattern? Please note that the use of both the
flags `--forloop` and `--whileloop` means that the program will iteratively
compute the powers of two with both a `for` loop and a `while` loop.

```
Calculating the powers of 2 from 0 to 2 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? Yes

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2

  Here is the output with the while loop.

   2**0 = 1
   2**1 = 2

Wow, all of that iteration was exhausting! 😂
```

It is important to note that the Python program can also produce the output of
the powers of two using a single type of iteration construct. For instance, the
command `poetry run python iterator --forloop --minimum 0 --maximum 5` produces
the following output:

```
Calculating the powers of 2 from 0 to 5 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2
   2**2 = 4
   2**3 = 8
   2**4 = 16

Wow, all of that iteration was exhausting! 😂
```

???+ note

    Remember, if you want to run `iterator` you must use your terminal to go
    into the GitHub repository containing this project and then go into the
    `iterator` directory that contains the project's source code. Finally,
    remember that before running the program you must run `poetry install` to
    add the dependencies. If you run into errors when using a `poetry run`
    command you can often resolve them by deleting the `.venv` directry and the
    `poetry.lock` file and then trying `poetry install` again.

## Adding Functionality

If you study the file `iterator/iterator/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `iterator` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```shell
================================= FAILURES =================================
__________________ test_calculate_x_values_non_imaginary ___________________

    def test_calculate_x_values_non_imaginary():
        """Check that the calculation of x values works if they are not imaginary."""
        a = 1
        b = 2
        c = 1
>       x_one, x_two = rootfind.calculate_quadratic_equation_roots(a, b, c)
E       TypeError: cannot unpack non-iterable NoneType object

tests/test_rootfind.py:20: TypeError
```

Alternatively, running the program with a command like `poetry run iterator
--a 1 --b 2 --c 1` will not produce any output! This is due to the fact that the
required source code does not yet exist inside of the `iterator` program. One
function that you need to implement is specified by the following signature.

```python linenums="1"
def calculate_quadratic_equation_roots(
    a: float, b: float, c: float
) -> Tuple[Union[float, complex], Union[float, complex]]:
```

This function's type annotations on line `2` suggest that each of its three
inputs are variables of type `float`. On line `3`, the notation `Union[float,
complex]` means that one of the outputs of `calculate_quadratic_equation_roots`
can either be a floating-point value of type `float` or an imaginary number of
type `complex`. The complete annotation of `Tuple[Union[float, complex],
Union[float, complex]]` means that the return value of
`calculate_quadratic_equation_roots` will be a two-tuple of values, with each
component of the two-tuple being either a `float` or a `complex` number. This
function should return values for `x_one` and `x_two` according to the following
equations:

$$
x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}
$$

$$
x_2=\frac{-b-\sqrt{b^2-4ac}}{2a}
$$

To provide a command-line interface to your program, you should also implement a
main function that has the following signature:

```python linenums="1"
def main(
    a: float = typer.Option(1),
    b: float = typer.Option(2),
    c: float = typer.Option(2)
):
```

This function signature shows that `iterator` accepts as input three
parameters called `a`, `b`, and `c` that respectively have default values of
`1`, `2`, and `2`, as seen on lines `2` through `4`. If you run `poetry run
iterator` if should produce this output:

```shell
⭐ Calculating the roots of a quadratic equation with:
   a = 1.0
   b = 2.0
   c = 2.0

⭐ Finished computing the roots of the equation as:
   x_one = (-0.9999999999999999+1j)
   x_two = (-1-1j)
```

## Running Checks

As you continue to add and confirm the correctness of `iterator`'s
functionality, you also study the source code in the `pyproject.toml` file. This
file contains the specification of several tasks that will help you to easily
run checks on your Python source code. Now, you can run commands like `poetry
run task lint` to automatically run all of the linters designed to check the
Python source code in your program and its test suite. You can also use the
command `poetry run task black` to confirm that your source code adheres to the
industry-standard format defined by the `black` tool. If it does not adhere to
the standard then you can run the command `poetry run black iterator tests`
and it will automatically reformat the source code.

```toml
[tool.taskipy.tasks]
black = { cmd = "black iterator tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 iterator tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy iterator", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle iterator tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint iterator tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `iterator`. If your program has all
of the anticipated functionality, you can run the command `poetry run task test`
and see that the test suite passes correctly if you have the correct
implementation of the function(s) that it tests.

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
implemented and used, and answer all of the other questions about your
experiences in completing this project.

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet every aspect of the project's
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
