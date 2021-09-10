# Number Comparison

## Project Goals

This programming project invites you to combine what you learned about the
basics of Python programming to implement a useful program that compares three
numbers that are provided as input to a program. Specifically, the program
should return the largest odd number among the provided inputs, provided that at
least one of the number is odd. When none of the input values are odd, the
program should return the smallest of the three provided values. Along with
adding documentation to the provided source code, you will create your own
Python functions that use both iteration constructs and conditional logic to
implement a correct program that passes the test suite and all checks. As you
enhance your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will program with
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

This project invites you to implement a number comparison program called
`compare`. The program accepts through its command-line three integer values. If
you run the program correctly, it will accept as input the three numbers and
return the largest odd number as long as at least one of the numbers is odd. In
the situation in which none of the numbers are odd, it will return the smallest
number. If you run the program with the command `poetry run compare --first 4
--second 10 --third 21` it produces this output:

```shell
✨ Comparing the numbers 4, 10, and 21!

Looking for the largest odd number ...
... but if there is no odd number, then ...
... looking for the smallest of the three!

Okay, I found the number 21!

😂 It was nice to find an odd number!
```

Alternatively, if you run the program with the command `poetry run compare
--first 4 --second 10 --third 20` then it produces output like:

```shell
✨ Comparing the numbers 4, 10, and 20!

Looking for the largest odd number ...
... but if there is no odd number, then ...
... looking for the smallest of the three!

Okay, I found the number 4!

🤷 Oh well, there were no odd numbers this time!
```

If you run the program without specifying one of the required input numbers by
using, for instance, the command `poetry run compare --first 4 --second 10` then
it will not perform number comparison and instead produce an error message like
the following:

```shell
Usage: compare [OPTIONS]
Try 'compare --help' for help.

Error: Missing option '--third'.
```

To learn more about how to run this program, you can type the command `poetry
run compare --help` to see the following output showing how to use `compare`:

```shell
Usage: compare [OPTIONS]

  Perform number comparison to find the largest odd number.

Options:
  --first INTEGER       [required]
  --second INTEGER      [required]
  --third INTEGER       [required]
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it
                        or customize the installation.

  --help                Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add all of the missing features and ensure that `compare` produces
the expected output. Once the program is working correctly, it should produce
all of the expected output described in this section.

???+ note

    Don't forget that if you want to run the `compare` program you must use your
    terminal window to first go into the GitHub repository containing this
    project and then go into the `compare` directory that contains the project's
    source code. Finally, remember that before running the program you must run
    `poetry install` to add the dependencies.

## Adding Functionality

If you study the file `compare/compare/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `compare` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```
    def test_find_minimum():
        """Confirm that the function can find the minimum of three values."""
        minimum = main.get_minimum(3, 4, 5)
>       assert minimum == 3
E       assert None == 3

tests/test_compare.py:16: AssertionError
```

Alternatively, running the program with a command like `poetry run compare
--first 4 --second 10 --third 21` will not produce any output because `compare`
is missing this functionality! As you complete the tasks near each of the `TODO`
markers, all while following the relevant instructions in the description of the
[technical skills](/proactive-skills/introduction-proactive-skills/), you should
have a version of `compare` that produces all of the expected output.

The `compare` program uses the `get_minimum` function to identify the minimum of
three int values. You can read a test case in the `test_compare.py` test suite
to learn more about how `compare`'s `get_minimum` function should work. For
instance, the following test case confirms that when `get_minimum` receives the
inputs `3`, `4`, and `5` then it should return the value of `3`, regardless of
the order in which the values are input to the function.

```python
def test_find_minimum():
    """Confirm that the function can find the minimum of three values."""
    minimum = main.get_minimum(3, 4, 5)
    assert minimum == 3
    minimum = main.get_minimum(5, 4, 3)
    assert minimum == 3
    minimum = main.get_minimum(4, 3, 5)
    assert minimum == 3
```

If the `get_minimum` function works correctly, then you can start to implement
and test the `get_largest_odd` function in the `compare` program! You can read
some test cases in `test_compare.py` test suite to learn more about how
`get_largest_odd` should work. For example, the following test case confirms
that when `get_largest_odd` receives the values `21`, `4`, and `17` it will
return `21`. In contrast, if it receives the inputs `21`, `4`, and `117` it will
return the value of `117` because that number is also odd and larger than `21`!

```python
def test_largest_odd_can_find_one():
    """Confirm that it is possible to find the largest odd value when it exists."""
    (largest_odd, found) = main.get_largest_odd(21, 4, 17)
    assert largest_odd == 21
    assert found is True
    (largest_odd, found) = main.get_largest_odd(21, 4, 117)
    assert largest_odd == 117
    assert found is True
```

In summary, you should implement the following functions for the `compare`
program:

- `def get_minimum(first: int, second: int, third: int) -> int`
- `def get_largest_odd(first: int, second: int, third: int) -> Tuple[int, bool]`
- `def compare(first: int = typer.Option(...), second: int = typer.Option(...),
  third: int = typer.Option(...)) -> None`

It is worth noting that the `get_largest_odd` function returns two values in the
form of a `Tuple[int, bool]`. The first of this function's output values is the
`int` result either the largest odd number or the smallest even number. The
second `bool` value is a Boolean flag to indicate whether it found an odd number
or not. Specifically, the `get_largest_odd` function should return `True` if it
found an odd number and return `False` otherwise.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black compare tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 compare tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy compare", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle compare tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint compare tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black compare tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run `gradle grade` to check your work. If `gradle grade` shows
that all checks pass, you will know that you made progress towards correctly
implementing and writing about `compare`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces output like
this:

```shell
collected 4 items

tests/test_compare.py ....
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
implemented and tested, compare and contrast different implementations of the
Python function called `get_largest_odd`, and answer all of the other questions
about your experiences in completing this project.

## Project Assessment

Since this project is an engineering effort, it is aligned with the **applying**
and **analyzing** levels of [Bloom's
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
