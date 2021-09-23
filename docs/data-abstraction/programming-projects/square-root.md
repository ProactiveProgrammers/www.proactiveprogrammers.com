# Square Root

## Project Goals

This assignment invites you to implement a program that features multiple
algorithms for computing the square root of a number. You will implement two
algorithms that use iteration constructs to approximate the square root of a
number. For a given step size and a tolerance level saying how close the
approximation must be, the exhaustive algorithm check if each possible answer is
within a specified tolerance for the square root's approximation. In contrast,
the efficient algorithm will use bisection search to rapidly prune the search to
the best possible approximation of the number's square root. In addition to
adding source code and documentation to the provided Python files, you will
conduct an experiment to determine which algorithm is the fastest and estimate
by how much it is faster. As you enhance your [technical
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

This project invites you to implement a number comparison program called
`squareroot`. The program accepts through its command-line a single integer
value. If you run the program correctly, it will accept as input the single
number numbers and return the largest odd number as long as at least one of the
numbers is odd. In the situation in which none of the numbers are odd, it will
return the smallest number. If you run the program with the command `poetry run
squareroot --number 25000 --approach exhaustive --profile` it produces the
following output:

```shell
🧮 Attempting to calculate the square root of 25000!

✨ Was this search for the square root successful? Yes
✨ How many guesses did it take to compute the solution? 1581139
✨ The best approximation for the square root of 25000 is 158.1139000041253

🔬 Here's profile data from performing square root computation on 25000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 10:25:39  Samples:  507
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.508     CPU time: 0.508
/   _/                      v4.0.3

Program: squareroot --number 25000 --approach exhaustive --profile

0.507 primality  squareroot/main.py:106
└─ 0.507 compute_square_root_exhaustive  squareroot/main.py:36
   ├─ 0.396 [self]
   └─ 0.111 abs  <built-in>:0
         [2 frames hidden]  <built-in>
```

If you run the program with the command `poetry run squareroot
--first 4 --second 10 --third 20` then it produces output like:

```shell
🧮 Attempting to calculate the square root of 25000!

✨ Was this search for the square root successful? Yes
✨ How many guesses did it take to compute the solution? 27
✨ The best approximation for the square root of 25000 is 158.11389312148094

🔬 Here's profile data from performing square root computation on 25000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 10:29:41  Samples:  0
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.000     CPU time: 0.000
/   _/                      v4.0.3

Program: squareroot --number 25000 --approach efficient --profile

No samples were recorded.
```

It is worth noting that the `exhaustive` algorithm took `1581139` guesses to
approximate the square root of `25000` while the `efficient` algorithm only
needed `27`! This shows that `efficient`'s bisection search algorithm is
significantly faster than the `exhaustive` approach. Interestingly, the
[Pyinstrument](https://github.com/joerick/pyinstrument) package reports that it
could not record any performance data for `squareroot` when the program runs in
`efficient` mode. Why do you think that this is the case? Is there any way to
overcome this issue by, for instance, reconfiguring Pyinstrument or changing the
input that you pass to the program? Overall, how much faster is `efficient` in
comparison to `exhaustive`? You can use the equations and suggestions in the
engineering effort about [primality
testing](../../engineering-efforts/primality-testing) to calculate the
percentage change in execution time when running `squareroot` in `efficient`
mode instead of the `exhaustive` mode. Finally, to understand why `efficient` is
faster than `exhaustive` you should study each function's source code and the
textbook's content.

To learn more about how to run this program, you can type the command `poetry
run squareroot --help` to see the following output showing how to use `squareroot`:

```shell
Usage: squareroot [OPTIONS]

  Use iteration to perform square root computation of a number and then
  perform profiling to capture execution time.

Options:
  --number INTEGER                [default: 5]
  --profile / --no-profile        [default: False]
  --approach [exhaustive|efficient]
                                  [default: efficient]
  --install-completion            Install completion for the current shell.
  --show-completion               Show completion for the current shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add the missing features and ensure that `squareroot` produces the
expected output. Once the program is working correctly, it should produce output
similar to that shown in this section.

???+ note

    Don't forget that if you want to run the `squareroot` program you must use
    your terminal to first go into the GitHub repository containing this project
    and then go into the `squareroot` directory that houses the project's code.
    Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

If you study the file `squareroot/squareroot/main.py` you will see that it has
many `TODO` markers that designate the parts of the program that you need to
implement before `squareroot` will produce correct output. In summary, you
should implement the following functions for the `squareroot` program:

- `def compute_square_root_exhaustive(
    x: int, epsilon: float = 0.01
) -> Tuple[bool, float, int]`
- `def compute_square_root_efficient(
    x: int, epsilon: float = 0.01
) -> Tuple[bool, float, int]`

Importantly, you will notice that both `compute_square_root_efficient` and
`compute_square_root_exhaustive` accept the same types of inputs and produce the
same types of outputs.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black squareroot tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 squareroot tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy squareroot", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle squareroot tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint squareroot tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black squareroot tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run `gradle grade` to check your work. If `gradle grade` shows
that all checks pass, you will know that you made progress towards correctly
implementing and writing about `squareroot`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces output like
this:

```shell
collected 4 items

tests/test_squareroot.py ....
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
implemented and tested, squareroot and contrast different implementations of the
Python function called `get_largest_odd`, and answer all of the other questions
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
