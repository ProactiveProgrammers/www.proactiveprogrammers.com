# Temperature Conversion

## Project Goals

This programming project invites you to combine what you learned about the
basics of Python programming to implement a useful program that converts a
temperature value between two different measurement scales, Celsius and
Fahrenheit. The program inputs the temperature reading that it should convert
and a configuration explaining whether it should convert from Celsius to
Fahrenheit or from Fahrenheit to Celsius. Using these inputs the program
performs the conversion and outputs it in the terminal. Along with adding
documentation to the provided source code, you will create your own Python
functions that uses both assignment statements and conditional logic to
implement a correct program that passes the test suite and all of the checks. As
you enhance your [technical
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
`converter`. The program accepts through its command-line a file that contains
integer values encoded as text. If you run the program with the command `poetry
run converter --from-unit Celsius --to-unit Fahrenheit --temperature 22` it
produces this output:

```
🧮 Converting from Celsius to Fahrenheit!

22.00 degrees in Celsius is 71.60 degrees in Fahrenheit
```

Since the program can also convert from Fahrenheit to Celsius, you can also run
it with the command `poetry run converter --from-unit Fahrenheit --to-unit
Celsius --temperature 71.6` and see that it produces the following output:

```
🧮 Converting from Fahrenheit to Celsius!

71.60 degrees in Fahrenheit is 22.00 degrees in Celsius
```

One way in which you can tell that `converter` is working correctly is that,
when given "inverse numbers", the output shows that it converts correctly in
both "directions". For instance, converting `22` degrees Celsius to Fahrenheit
yields `71.6` degrees and converting `71.6` degrees Fahrenheit to Celsius
results in `22` degrees! To learn more about how to run this program, you can
type the command `poetry run converter --help` to see the following output
showing how to use `converter`:

```
Usage: converter [OPTIONS]

  Convert units.from Fahrenheit to Celsius or from Celsius to
  Fahrenheit.

Options:
  --from-unit [Celsius|Fahrenheit]
                                  [default: Celsius]
  --to-unit [Celsius|Fahrenheit]  [default: Fahrenheit]
  --temperature FLOAT RANGE       [default: 98.6]
  --install-completion            Install completion for the current
                                  shell.

  --show-completion               Show completion for the current shell,
                                  to copy it or customize the
                                  installation.

  --help                          Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add all of the missing features to ensure that `converter` produces
the expected output. Once you finish the program, it should produce all of the
expected output described in this section.

???+ note

    Recall that if you want to run the `converter` program you must use your
    terminal window to first go into the GitHub repository containing this
    project and then go into the `converter` directory that contains the
    project's source code. Remember that before running the program you must run
    `poetry install` to add the dependencies!

## Adding Functionality

If you study the file `converter/converter/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `converter` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```
    def test_converter_computation_five_numbers():
        """Confirm that it is possible to converter together five non-zero numbers."""
        number_list = """-72
            29
            61
            -42
            44"""
        converter_value = main.compute_converter(number_list)
>       assert converter_value == ((-72 + 29 + 61 + -42 + 44) / 5)
E       assert 0 == (((((-72 + 29) + 61) + -42) + 44) / 5)
```

Note that this test case fails because of the fact that, by default, the
`compute_converter` function returns `0` instead of the correct arithmetic mean of
the numbers specified in the `number_list` variable. You will need to add source
code to the `compute_converter` function so that it correctly calculates the
converter of the input values!

In summary, you should implement the following functions for the `converter`
program:

- `def compute_converter(contents: str) -> float:`
- `def converter(dir: Path = typer.Option(None), file: Path = typer.Option(None)) -> None:`

It is worth noting that the `compute_converter` function accepts as input a `str`
that is a one-number-per-line encoding of the file that contains the integer
numbers. This means that `compute_converter` will need to iterate through each
line in the file and convert the text-based encoding of the number to an `int`.
The `compute_converter` function should also handle the circumstance in which the
user-provided file (i.e., `numbers.txt`) does not have any numbers inside of it!
If there were no numbers in the file, then the function can return `-1` to
indicate that it did not compute an converter. As you are finishing your
implementation of the `compute_converter` function, you should also ensure that,
if all of the numbers inside of the file are `0`, then it returns an converter of `0`.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black converter tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 converter tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy converter", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle converter tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint converter tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black converter tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run `gradle grade` to check your work. If `gradle grade` shows
that all checks pass, you will know that you made progress towards correctly
implementing and writing about `converter`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces output like
this:

```shell
collected 5 items

tests/test_converter.py .....
```

You will know that the `compute_converter` function correctly returns `0` when all
of the inputs are `0` if the following test case passes:

```python linenums="1"
def test_converter_computation_five_numbers_all_zero():
    """Confirm that it is possible to converter together five zero numbers."""
    number_list = """0
        0
        0
        0
        0"""
    converter_value = main.compute_converter(number_list)
    assert converter_value == 0
```

Lines `3` through `7` of this test case define the `number_list` variable as one
that contains a list of `0` values separated by newlines. The purpose of
`number_list` is to represent the string that would arrive from the input file
if a person ran the `converter` program on the command-line. Line `8` of this test
case calls the `compute_converter` function with the `number_list` as the input
and stores the output in a variable called `converter_value`. Finally, line `9`
confirms that `compute_converter` calculates the converter of the input as `0`.

You will know that the `compute_converter` function correctly returns `-1` when
there is no input to the function if the follow test case passes:

```python linenums="1"
def test_converter_computation_no_provided_numbers():
    """Confirm that it is possible to converter together no numbers."""
    number_list = ""
    converter_value = main.compute_converter(number_list)
    assert converter_value == -1
```

On line `3` in the above source code, this test defines `number_list` as an
empty string, denoted by `""`. Finally, on line `4` it calls the
`compute_converter` function with `number_list` as its input and on line `5` it
confirms that the computed `converter_value` is `-1`, as required by the
specification of the function under test.

Once all of the test cases pass, you can run the all of the automated checks by
typing `poetry run task all` in your terminal and confirming that there are no
errors in the output. If all of the checks pass, then you can run the program
with the command `poetry run converter --dir input --file numbers.txt` and then
confirm that it produces the expected output, including the converter of `-0.95`.

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
Python function called `compute_converter`, and answer all of the other questions
about your experiences in completing this project.

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
