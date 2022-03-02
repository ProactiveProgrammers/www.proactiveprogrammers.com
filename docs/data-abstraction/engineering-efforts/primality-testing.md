# Primality Testing

## Project Goals

This assignment invites you to implement a program that features multiple
algorithms for performing primality testing. You will implement two algorithms
that conduct a search to determine whether or not the number input to the
program is prime. The exhaustive search algorithm will examine all possible
elements of a search space while, in contrast, the efficient one will use extra
conditional logic to restrict the search space. In addition to adding source
code the provided Python files, you will conduct an experiment to determine
which algorithm is the fastest and estimate by how much it is faster. As you
enhance your [technical
skills](/proactive-skills/introduction-proactive-skills/) and explore the
experimental evaluation of algorithms, you will continue to program with tools
such as VS Code and a terminal window and the Python programming language and
the Poetry package manager.

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

This project invites you to implement a number squaring program called
`primality`. The program accepts as input a number, like `49979687`, a
description of an approach (that can either be `efficient` or `exhaustive`), and
a boolean flag to indicate whether or not the program should profile its
execution. When `primality` is run in `exhaustive` mode it checks all integer
values in `range(2, number)` if `number` is the integer value subject to
primality testing. After you finish the correct implementation of all the
program's features, running it with the command `poetry run primality --number
49979687 --approach efficient --profile` will produce output like the following:

```shell
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1, 49979687
✨ Was this a prime number? Yes

🔬 Here's profiling data from performing primality testing on 49979687!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 22:10:56  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.870     CPU time: 0.869
/   _/                      v4.0.3

Program: primality --number 49979687 --approach efficient --profile

0.870 primality  primality/main.py:93
└─ 0.870 primality_test_efficient  primality/main.py:77
```

Did you notice that this program produces profiling data about how long it took
to run the `primality` program in `efficient` mode with the input `49979687`?
This is because of the fact that it uses the
[Pyinstrument](https://github.com/joerick/pyinstrument) program to collect
execution traces and efficiency information about the program. For this run of
the program, it took about `0.870` seconds to determine that `49979687` was a
prime number. Is that fast or not? Well, let's run the `primality` program in
`exhaustive` mode and measure by how much it is slower! Specifically, running
the command `poetry run primality --number 49979687 --approach exhaustive
--profile` produces the following output:

```shell
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1, 49979687
✨ Was this a prime number? Yes

🔬 Here's profiling data from performing primality testing on 49979687!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 22:34:38  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 1.739     CPU time: 1.738
/   _/                      v4.0.3

Program: primality --number 49979687 --approach exhaustive --profile

1.738 primality  primality/main.py:93
└─ 1.738 primality_test_exhaustive  primality/main.py:57
```

If `exhaustive` mode of `primality` takes `1.738` and `efficient` mode only
takes `0.870`, how much faster is `efficient` mode compared to `exhaustive`? If
$T_f$ denotes the execution time of `efficient` mode and $T_x$ denotes the
execution time of `exhausitve` mode, then the following equation defines
$T_{\Delta}$, or the percentage change in the execution time when running
`primality` in `efficient` mode instead of `exhaustive`.

$$
T_{\Delta} = \frac{T_x - T_f}{T_x} \times 100
$$

Using this equation with the timing values of $T_x = 1.738$ and $T_f = 0.87$
from Pyinstrument shows that `efficient` mode is $(1.738
- 0.87) / 1.738 * 100 = 49.9427$ percent faster than `exhaustive` mode. When you
check the source code in the GitHub repository for this project you will see
why! Unlike `exhaustive` mode, the `efficient` mode of `primality` does not
check for even divisors of `number` bigger than two, instead only determining
if `number` is divisible by any odd number in `range(3, x, 2)`. In retrospect,
it makes sense that `efficient` is about $50$ percent faster than
`exhaustive` because, by not checking the even numbers, it does not do half
of `exhaustive`'s work.

It is worth noting that you do not have to run `primality` in the `profile` mode
that uses Pyinstrument. For instance, running the program with `poetry run
primality --number 49979687 --approach exhaustive` would run the program in
`exhaustive` mode and perform the same computation without collecting the
performance data. You can display `primality`'s help menu and learn more about
the features it should support by typing `poetry run primality --help` to
display the following:

```shell
Usage: primality [OPTIONS]

  Use iteration to perform primality testing on a number.

Options:
  --number INTEGER                [default: 5]
  --profile / --no-profile        [default: False]
  --approach [exhaustive|efficient]
                                  [default: efficient]
  --install-completion            Install completion for the current
                                  shell.

  --show-completion               Show completion for the current shell,
                                  to copy it or customize the
                                  installation.

  --help                          Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce the output displayed in this section. As explain in the
next section, you are invited to add the features needed to ensure that
`primality` produces the expected output!

???+ note

    Don't forget that if you want to run the `primality` program you must use
    your terminal window to first go into the GitHub repository containing this
    project and then go into the `primality` directory that contains the
    project's source code. Finally, remember that before running the program you
    must run `poetry install` to add its dependencies, such as Pyinstrument,
    Pytest, and Rich.

## Adding Functionality

If you study the file `primality/primality/main.py` you will see that it has
many `TODO` markers that designate the parts of the program that you need to
implement before `primality` will produce correct output. If you run the
provided test suite with the command `poetry run task test` you will see that it
produces a message suggesting that there is a syntax error in the program. Along
with creating instances of the `Typer` and `Profiler` classes, you will need to
resolve all of the syntax errors so that you can run `primality` and its test
suite. You must also implement all of these functions:

- `def human_readable_boolean(answer: bool) -> str`
- `def pretty_print_list(values: Iterable[int]) -> str`
- `def primality_test_exhaustive(x: int) -> Tuple[bool, List[int]]`
- `def primality_test_efficient(x: int) -> Tuple[bool, List[int]]`

The following source code illustrates how to use Pyinstrument to collect the
timing information for the execution of the `efficient` approach for primality
testing, as implemented in the function `primality_test_efficient`. First, line
`1` creates an empty `primality_tuple` and lines `2` and `3` confirm that the
person using the program requested to profile the execution of the `efficient`
approach. Using Pyinstrument, line `4` starts the profiler and line `6` stops
it, with line `5` making the call to the `primality_test_efficient` function.
When the person running `primality` did not use `--profile`, then line `8` calls
`primality_test_efficient` without using Pyinstrument.

```python linenums="1"
primality_tuple: Tuple[bool, List[int]]
if approach.value == PrimalityTestingApproach.efficient:
    if profile:
        profiler.start()
        primality_tuple = primality_test_efficient(number)
        profiler.stop()
    else:
        primality_tuple = primality_test_efficient(number)
```

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black primality tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 primality tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy primality", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle primality tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint primality tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black primality tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `primality`. If your program has all of
the anticipated functionality, you can run the command `poetry run task test`
and see that the test suite produces output like this:

```shell
collected 7 items

tests/test_primality.py .......
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
to evaluate the efficiency of the two different modes (i.e., `exhaustive` and
`efficient`) of the `primality` program.

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
