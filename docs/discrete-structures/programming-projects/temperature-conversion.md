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

If you study the file called `converter/converter/main.py` you will see that it
has many `TODO` markers that designate the parts of the program that you need to
implement before `converter` will produce correct output. Along with adding
requested source code to the `main` module, you should implement the following
functions in the `convert` module:

- `def convert_celsius_to_fahrenheit(temperature: float) -> float`
- `def convert_fahrenheit_to_celsius(temperature: float) -> float`
- `def convert_temperature(temperature: float, from_unit: units.TemperatureUnitOfMeasurement, to_unit: units.TemperatureUnitOfMeasurement)`

The first two functions in this listing input a `float` value that respectively
represents a temperature in Celsius or Fahrenheit and then converts it to a
`float` representing a respective temperature in Fahrenheit or Celsius. Finally,
the `converted_temperature` function uses source code as in the following
segment to first determine what type of temperature conversion the user
requested and then call the appropriate function. For instance, lines `3` and
`4` show that, when the requested temperature conversion is from Celsius to
Fahrenheit, the `converted_temperature` function will call the
`convert_celsius_to_fahrenheit` function. Alternatively, lines `6` through `7`
show that `convert_temperature` calls `convert_fahrenheit_to_celsius` when a
person requests temperature conversion in the opposite direction.

```python linenums="1"
converted_temperature = 0
# the requested temperature conversion is Celsius --> Fahrenheit
if from_unit.value == "Celsius" and to_unit.value == "Fahrenheit":
    converted_temperature = convert_celsius_to_fahrenheit(temperature)
# the requested temperature conversion is Fahrenheit --> Celsius
elif from_unit.value == "Fahrenheit" and to_unit.value == "Celsius":
    converted_temperature = convert_fahrenheit_to_celsius(temperature)
return converted_temperature
```

Once you have correctly resolved all of the `TODO` markers in the `converter`
program, it should produce the expected output described in the previous
section.

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

```
tests/test_convert.py ........

============================ 8 passed in 0.02s =============================
```

The `test_convert` test suite contains test cases for all of the functions
mentioned in the previous section. Even if the test cases for
`convert_fahrenheit_to_celsius` and `convert_celsius_to_fahrenheit` pass as
expected it is possible that those for `convert_temperature` make not if the way
in which it calls the specific temperature conversion functions is not correct.
When one or more test cases fail, make sure you check to see which ones are
failing so that you can better know where to start the debugging process! The
following test case shows how to test `convert_temperature` when lines `3` and
`4` configure `convert_temperature` to convert from Celsius to Fahrenheit. After
setting the input `temperature` to `0` on line `1` and calling the
`convert_temperature` function on line `5`, the test case checks on line `6`
that the conversion function produced the temperature value of `32`, failing the
test if that is not the case.

```python linenums="1"
def test_convert_celsius_to_fahrenheit_wrapper():
    temperature = 0
    from_unit = units.TemperatureUnitOfMeasurement.celsius
    to_unit = units.TemperatureUnitOfMeasurement.fahrenheit
    converted_temperature = convert.convert_temperature(temperature, from_unit, to_unit)
    assert converted_temperature == 32
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
