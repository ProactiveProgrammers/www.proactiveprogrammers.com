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

This project invites you to implement a program called `iterator`. The program
has two flags called `--forloop` and `--whileloop` that control the type of
iteration construct with which the program performs iterative exponentiation. To
best understand the program's behavior it is nice to observe how it operates
when given different command-line arguments. For instance, the command `poetry
run iterator --forloop --whileloop --minimum 0 --maximum 2` produces the
following output. Can you see the pattern? Please note that the use of both the
flags `--forloop` and `--whileloop` means that the program will iteratively
compute the powers of two with both a `for` and `while` loop.

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
command `poetry run iterator --forloop --minimum 0 --maximum 5` produces
the following output demonstrating that the program only ran a `for` loop. As in
the previous output example, this output shows that the program uses the `**`
operator to raise `2` to the power of a number such as `0`, `1`, and `2`. Both
of these output examples also show that the program should contain several lines
of diagnostic output that make it clear how it interpreted the command-line
arguments before it starting to perform iterative exponentiation.

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

While all of the prior examples show that the `iterator` works when
you use `0` as the value for the `--minimum`, it is also important to
point out that it should work when you increase the value for this
parameter. For, instance, when you run the command `poetry run iterator
--forloop --minimum 2 --maximum 10` it should produce the following
output. Note that this output shows that the first exponentiation that
the `iterator` performs is `2**2 = 4` instead of starting with `2**0 =
1` as was the case in the previous runs.

```
Calculating the powers of 2 from 2 to 10 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**2 = 4
   2**3 = 8
   2**4 = 16
   2**5 = 32
   2**6 = 64
   2**7 = 128
   2**8 = 256
   2**9 = 512

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
implement before `iterator` will produce the correct output. If you run the
program before adding all of the source code required by the `TODO` markers then
`iterator` will neither produce the correct output or pass the test suite.
Ultimately, you are invited to add the required functionality to the functions
that have the following signature:

- Functions in the `display` module:
    - `def convert_bool_to_answer(argument: bool)`
    - `def display_list(values: List, indent="")`
- Functions in the `iterate` module:
    - `def calculate_powers_of_two_for_loop(minimum: int, maximum: int)`
    - `def calculate_powers_of_two_while_loop(minimum: int, maximum: int)`

When you are finished implementing both of the iterative approaches, please take
time to evaluate each of them, comparing and contrasting their syntactic
structure. Which one do you think is easier to understand? Why? Can you develop
any good rules of thumb that suggest when it is better to use one type of loop
over the other loop type?

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
