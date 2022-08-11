![Integer Squaring](/img/Pro-Data-Abstraction-Integer-Squaring.svg){align=center}

# Integer Squaring

## Project Goals

This engineering effort invites you to combine what you learned about the basics
of Python programming to implement a useful program that can compute the square
for all of the integer values stored inside of a file. As part of this project
you will learn how to navigate the source code in a Python file, perform file
input and output using `Path` objects from `pathlib`, implement Python
functions, and implement and test functions that contain either a `for` and or
a `while` loops. As you enhance your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will implement
a Python program and write technical content in Markdown while using tools
such as VS Code, a terminal window, the Python programming language, and the
Poetry package manager. Ready for some fun with programming? *Okay, let's get
started!*

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
    assignment! To get started, you should click the "Use this template" icon in
    the :material-github:
    [integer-squaring-starter](https://github.com/ProactiveProgrammers/integer-squaring-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Expected Output

This project invites you to implement a number squaring program called `square`.
You can install the dependencies for the `square` program and ensure that it is
ready to run by using your terminal to type the command `poetry install` in the
`square` directory that contains the `pyproject.toml` and `poetry.lock` files.
The program can accept as input a file of numbers, a directory that contains the
this file, and the name of an approach to squaring an integer. If you run the
program correctly, it will iterate through the file of numbers, compute the
square for each number, and output a complete list of the squared values. For
instance, if you run the program with the command `poetry run square --approach
for --directory input --file numbers.txt` it produces this output:

```text
😃 Squaring numbers in a file called input/numbers.txt!

[
    5184,
    841,
    3721,
    1764,
    1936,
    ...
]
```

In addition to having a feature that lets you square numbers using a `for` loop,
the `square` program can perform the same task by using a `while` loop! If you
run the program with the command `poetry run square --approach while --directory input
--file numbers.txt` then the program should produce the same output as given
above this paragraph. If you run the command `poetry run square --help` you
should see the following output that explains how to use the `square` program:

```shell
 Usage: square [OPTIONS]

 Provide a command-line interface for iteratively squaring all integers
 in a file.

╭─ Options ─────────────────────────────────────────────────────────────╮
│ --approach                  [for|while]  [default: for]               │
│ --directory                 PATH         [default: None]              │
│ --file                      PATH         [default: None]              │
│ --install-completion                     Install completion for the   │
│                                          current shell.               │
│ --show-completion                        Show completion for the      │
│                                          current shell, to copy it or │
│                                          customize the installation.  │
│ --help                                   Show this message and exit.  │
╰───────────────────────────────────────────────────────────────────────╯
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explain in the next section, you are
invited to add all of the missing features and ensure that `square` produces the
expected output. Once the program is working correctly, you should also try to
use it when specifying a file that is not available on your computer! For instance,
if you run it with the command `poetry run square --approach for --directory input
--file numberswrong.txt` then it will not perform the number squaring and
instead produce the following output:

```shell
😃 Squaring numbers in a file called input/numberswrong.txt!

🤷 input/numberswrong.txt was not a valid file! Sorry, cannot square the
numbers!
```

???+ note

    Don't forget that if you want to run the `square` program you must use your
    terminal window to first go into the GitHub repository containing this
    project and then go into the `square` directory that contains the project's
    source code. Finally, remember that before running the program you must run
    `poetry install` to add the dependencies.

## Adding Functionality

If you study the file `square/square/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `square` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```text
================================ ERRORS =================================
_________________ ERROR collecting tests/test_square.py _________________
tests/test_square.py:4: in <module>
    from square import main
square/main.py:54: in <module>
    ???
E   NameError: name 'cli' is not defined
======================== short test summary info ========================
ERROR tests/test_square.py - NameError: name 'cli' is not defined
!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!
=========================== 1 error in 0.14s ============================
```

Alternatively, running the program with a command like `poetry run square
--approach for --directory input --file numbers.txt` will produce the following
output:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/gkapfham/.asdf/installs/python/3.10.5/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/gkapfham/working/teaching/github-classroom/proactive-programmers/data-abstraction/starters/engineering-efforts/integer-squaring-starter/square/square/main.py", line 54, in <module>
    @cli.command()
NameError: name 'cli' is not defined
```

This output suggests that the `cli` variable was not correctly defined! After
correctly resolving this issue --- all while following the relevant instructions
in the description of the [technical
skills](/proactive-skills/introduction-proactive-skills/) --- you should find
the other `TODO` markers and correctly resolve them. For instance, you can add
this function to the `main.py` file:

```python linenums="1"
def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False
```

Line `1` of this function defines the signature of `confirm_valid_file`, showing
that it will take as input a `Path` object and return as output a `bool` to
indicate whether or not the file is valid. Lines `4` through `7` confirm that
the `file` is valid and `True` if it is both not `None` and a valid file.
Alternatively, line `9` returns `False` to indicate that `file` is not valid. In
addition to `confirm_valid_file`, you must also implement these functions:

- `def compute_square_while(value: int) -> int`
- `def compute_square_for(value: int) -> int`
- `def compute_square_iterative(contents: str, square_function: Callable[[int], int]) -> List[int]:`

It is worth noting that the `compute_square_iterative` function is a
higher-order function that accepts as one of its inputs the `square_function`
that should be either `compute_square_for` or `compute_square_while`. The person
running the `square` program can pick which of these functions the program will
call by specifying either `for` or `while` as one of the program's command-line
arguments. The `square` program uses the Typer package and the following source
code to ensure that the program only accepts one of these two options. For
instance, if you try to run the program with the command `poetry run square
--approach recursion --directory input --file numbers.txt` it will produce the
following error message because `recursion` is not a valid option:

```text
Usage: square [OPTIONS]
Try 'square --help' for help.
╭─ Error ───────────────────────────────────────────────────────────────╮
│ Invalid value for '--approach': 'recursion' is not one of 'for',      │
│ 'while'.                                                              │
╰───────────────────────────────────────────────────────────────────────╯
```

The `square` program contains the following source code to specify the valid
options:

```python linenums="1"
class IntegerSquareApproach(str, Enum):
    """Define the name of the approach to squaring a number."""

    FOR_LOOP = "for"
    WHILE_LOOP = "while"
```

Line `1` of this code segment defines a new class called `IntegerSquareApproach`
that operates as a enumeration of values. Specifically, an instance of the
`IntegerSquareApproach` will have a `value` variable that is either equal to
`FOR`, designating that the input integer should be squared through iteration
with a `for` loop or equal to `WHILE`, meaning that it should complete the same
task with a `while` loop. The `square` program uses the `IntegerSquareApproach`
to define the acceptable arguments that a person can pass to it through its
command-line interface.

???+ note

    It is possible that you will become overwhelmed by the details associated
    with Python programming as you implement all of the required functionality
    for the `square` program. If you get stuck on any aspect of this project,
    take the time to write out a list of steps that you have already taken, a
    summary of what worked and did not work, and the current questions that
    you have. After taking these important steps, you can share a status
    update and ask questions in either the [GitHub discussions
    forum](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/discussions)
    or the [Proactive Programmers Discord
    server](https://discord.gg/kjah8MFYbR). Before you ask your question,
    please read the advice concerning how to best participate in the
    [Proactive Programmers
    community](https://proactiveprogrammers.com/proactive-community/community-connections/).

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable tasks like
`lint`. If you are in the `square` directory that contains the `pyproject.toml`
file and the `poetry.lock` file, the tasks in this section make it easy to run
commands like `poetry run task lint` to automatically run all of the linters
designed to check the Python source code in your program and its test suite. You
can also use the command `poetry run task black` to confirm that your source
code adheres to the industry-standard format defined by the `black` tool. If it
does not adhere to the standard then you can run the command `poetry run black
square tests` and it will automatically reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to run the command
`gatorgrade --config config/gatorgrade.yml` to check your work. If the output of
the `gatorgrade` command shows that all the checks pass, then you will know that
you made progress towards correctly implementing and writing about `square`. You
can study the `config/gatorgrade.yml` file in your repository to learn how the
:material-github: [GatorGrade](https://github.com/GatorEducator/gatorgrade)
program runs :material-github:
[GatorGrader](https://github.com/GatorEducator/gatorgrader) to automatically
check your program and technical writing. If your work meets the baseline
requirements and adheres to the best practices that proactive programmers adopt
you will see that all the checks pass when you run `gatorgrade`.

It is worth noting that the test suite for the `square` program is missing a
test case! You can create the missing test case by following the example of the
following test:

```python linenums="1"
def test_compute_square_iterative_for_loop():
    """Confirm that the for loop calculates squares correctly for negatives and positives in loop."""
    number_list = """-72
        29
        61
        -42
        44"""
    square_function = main.compute_square_for
    square_list = main.compute_square_iterative(number_list, square_function)
    assert square_list == [72 * 72, 29 * 29, 61 * 61, 42 * 42, 44 * 44]
```

This test case takes the following steps:

- Lines `3` through `7`: Create a `number_list` multiple-line string with integers for squaring
- Line `8`: Defines the `square_function` to be the `compute_square_for` function in `main`
- Line `9`: Calls `compute_square_iterative` with `number_list` and `square_function`
- Line `9`: Stores the output of the `compute_square_iterative` function in `square_list`
- Line `10`: Asserts that the `square_list` variable contains the squares of each number

You should write a new test that follows these steps for the
`compute_square_while` function! Finally, please make sure that you explain all
of the steps in these test cases by adding single-line comments to each line in
every test case function.

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
completing this project.

???+ note

    To ensure that you master the technical and professional skills introduced
    as part of this project you need to participate in deliberate practice that
    "requires both a clear performance goal and immediate informative
    feedback".[^1] After reflecting on the challenges that you faced and
    identifying areas for improvement, make a list of SMART goals that will
    enable you to more effectively put a specific technical skill into practice,
    follow your plan, and continually work to improve.[^2] You can learn more
    about how to best reflect on your experiences and improve before starting
    your next project by reviewing the [technical
    skills](proactive-skills/technical-skills/introduction-technical-skills/)
    that a proactive programmer should master!

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
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

--8<-- "includes/abbreviations.md"

[^1]: See Merriam-Webster for the definition of [Teaching Tech
  Together](https://teachtogether.tech/en/index.html) for more details about how
  to effectively learn technical skills. What practical steps can you take to
  best ensure that you can master the technical skills of a proactive programmer?

[^2]: See the article called [How to write SMART
  goals](https://www.atlassian.com/blog/productivity/how-to-write-smart-goals)
  for an overview of how to create SMART goals that are specific, measurable,
    achievable, relevant, and time-bound. In your view, what are the benefits of
    ensuring that your goals fit into the SMART paradigm?
