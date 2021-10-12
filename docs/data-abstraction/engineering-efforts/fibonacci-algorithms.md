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
    0.00 seconds

```

Don't forget that you can display `fibonaccicreator`'s help menu and learn more
about its features by typing `poetry run fibonaccicreator --help` to display the
following:

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
functionality to produce the output displayed in this section. As explain in the
next section, you are invited to add the features needed to ensure that
`fibonaccicreator` produces the expected output!

???+ note

    Don't forget that if you want to run the `fibonaccicreator` program you must use
    your terminal window to first go into the GitHub repository containing this
    project and then go into the `fibonaccicreator` directory that contains the
    project's source code. Finally, remember that before running the program you
    must run `poetry install` to add its dependencies, such as Pyinstrument,
    Pytest, and Rich.

## Adding Functionality

If you study the file `fibonaccicreator/fibonaccicreator/main.py` you will see that it
has many `TODO` markers that designate the parts of the program that you need to
implement before `fibonaccicreator` will produce correct output. To ensure that the
program works correctly, you must implement all of these functions before you
start to run the experiments.

- `def generate_random_container(size: int, maximum: int, make_tuple: bool = False) -> Union[List[int], Tuple[int, ...]]`
- `def compute_fibonaccicreator_list_double(input_one: List[Any], input_two: List[Any]) -> List[Any]`
- `def compute_fibonaccicreator_list_single(input_one: List[Any], input_two: List[Any]) -> List[Any]`

The function called `generate_random_container` should automatically create
either a `tuple` or a `list` of the specified `size` and only containing values
that are less than or equal to the `maximum`. The function called
`compute_fibonaccicreator_list_single` should follow the implementation strategy of
its counterpart function called `compute_fibonaccicreator_tuple_single` while still
using the functions appropriate for the `list` structured type. Moreover, the
`compute_fibonaccicreator_list_double` should follow the implementation of
`compute_fibonaccicreator_tuple_double` except for the fact that it should populate
an `list` through the use of a doubly-nested `for` loop. As a reference, here is
the source code for the `compute_fibonaccicreator_tuple_single` function:

```python linenums="1"
def compute_fibonaccicreator_tuple_single(
    input_one: Tuple[Any, ...], input_two: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    """Compute the fibonaccicreator of two provided tuples."""
    result: Tuple[Any, ...] = ()
    for element in input_one:
        if element in input_two:
            result += (element,)
    return result
```

According to the type signature of this function on lines `1` and `2`, the
`compute_fibonaccicreator_tuple_single` function accepts as input two `tuples` that
can contain `Any` type of data and be of an arbitrary size. Lines `6` through
`8` of this function show that it uses the combination of a `for` loop and an
`if` statement to compute the fibonaccicreator of the `tuple`s called `input_one`
and `input_two`. After finding those elements that these `tuple`s contain in
common, `compute_fibonaccicreator_tuple_single` returns the `result` on line `9`.
Since this function processes `tuple`s it is possible that the fibonaccicreator of
the input parameters will be a `result` that contains a value more than once. It
is also worth noting that, since the `tuple` structured type is immutable, this
function uses the `+=` operator on line `8` to create a new `tuple` each time
that it adds data to the `result` variable. You will empirically study the
efficiency of this approach!

After finishing your implementation of `fibonaccicreator` you should conduct an
experiment to evaluate the efficiency of the different algorithms that it
provides. You should refer to the `writing/reflection.md` file for more details
about the experiment that you should conduct and how you must configure the
`fibonaccicreator` program to collect data. Ultimately, you need to answer the
following three research questions:

- Is the fibonaccicreator of two data containers faster with a `list` or a `tuple`?
- Is the fibonaccicreator of two data containers faster with a double or single `for` loop?
- Overall, what is the fastest approach for computing the fibonaccicreator of two
  data containers?

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
correctly implementing and writing about `fibonaccicreator`. If your program has all of
the anticipated functionality, you can run the command `poetry run task test`
and see that the test suite produces output like this:

```
collected 4 items

tests/test_fibonaccicreator.py .......
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
