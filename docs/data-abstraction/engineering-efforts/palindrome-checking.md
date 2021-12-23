# Palindrome Checking

## Project Goals

This engineering effort invites you to implement a program called
`palindromechecker` that can determine whether or not an input word is or is not
a palindrome, or a word that is spelled the same both forwards and backwards.
For instance, the word `civic` is a palindrome because it is spelled the same
both forwards and backwards while `example` is not. Specifically, you will
implement one approach to palindrome checking that uses recursion and another
that reverses the word. In addition to implementing these two approaches for
palindrome checking, you will create a comprehensive command-line interface
using [Typer](https://typer.tiangolo.com/). Along with implementing your own
test cases for the functions that determine whether the word is a palindrome,
you will also add documentation to your `palindromechecker` in the form of
docstrings for both the functions and the module.

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
`palindromechecker`, that features different ways to compute all of the numbers
in the Fibonacci sequence up to a specified maximum number. After you finish a
correct implementation of all the program's features, running it with the
command `poetry run palindromechecker --number 10 --approach recursivelist
--display`, it will produce output like the following.

Don't forget that you can display `palindromechecker`'s help menu and learn more
about its features by typing `poetry run palindromechecker --help` to show the
following output. This help menu shows that `palindromechecker` also has a
`--pyinstrument` flag that enables it to produce a web-based output that shows
the function calls made by the `palindromechecker` and the performance results
created by the [Pyinstrument](https://github.com/joerick/pyinstrument) package.

```
Usage: palindromechecker [OPTIONS]

  Use a method to determine if an input string is a palindrome or not.

Options:
  --word TEXT                     [required]
  --approach [recursive|reverse]  [default: reverse]
  --install-completion            Install completion for the current
                                  shell.

  --show-completion               Show completion for the current shell,
                                  to copy it or customize the
                                  installation.

  --help                          Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce the output displayed in this section. As the next
section explains, you should add the features needed to ensure that
`palindromechecker` produces the expected output! Importantly, this project
invites you to add the following functionality: (i) a recursion-based and
reversal-based algorithm for palindrome checking, (ii) 

???+ note

    Don't forget that if you want to run the `palindromechecker` program you must use
    your terminal window to first go into the GitHub repository containing this
    project and then go into the `palindromechecker` directory that contains the
    project's source code. Finally, remember that before running the program you
    must run `poetry install` to add its dependencies, such as Pyinstrument,
    Pytest, and Rich.

## Adding Functionality

If you study the file `palindromechecker/palindromechecker/main.py` you will see
that it has many `TODO` markers that designate the parts of the program that you
need to implement before `palindromechecker` will produce correct output. Once
you complete a task associated with a `TODO` marker, make sure that you delete
it and revise the prompt associated with the marker into a meaningful comment.
To ensure that the program works correctly, you must implement all of these
functions in the `palindrome` module:

- `def to_chars(word: str) -> str`
- `def is_palindrome(word: str) -> bool`
- `def is_palindrome_recursive(word: str) -> bool`
- `is_palindrome_reverse(word: str) -> bool`

After finishing your implementation of `palindromechecker` you should repeatedly
run the program in different configurations to confirm that it produces the
correct output. Since the `palindromechecker` provides a checking mode based on
reversing the string or recursively checking the string, you should make sure
that both approaches work correctly. You should also confirm that the
`palindromechecker` can correctly determine when a word both is and is not a
palindrome. Here are some examples that show the program's correct execution for
different values for the `--word` and `--approach` arguments. If you correctly
resolve all of the `TODO` markers in the provided source code your program
should produce the same output for each of these commands.

- `poetry run palindromechecker --word civic --approach reverse`

```
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- `poetry run palindromechecker --word civic --approach reverse`

```
✨ Awesome, using the reverse approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- `poetry run palindromechecker --word origin --approach recursive`

```
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "origin" is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

- `poetry run palindromechecker --word origin --approach reverse`

```
✨ Awesome, using the reverse approach for palindrome checking!

🔖 Going to check to see if the word "origin" is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black palindromechecker tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 palindromechecker tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy palindromechecker", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle palindromechecker tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint palindromechecker tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black palindromechecker tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `palindromechecker`. If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following. It is
worth noting that the name of the test suite is `test_fibonacci` because the
functions mentioned in the previous section exist in the `fibonacci` module.

```
collected 5 items

tests/test_fibonacci.py .....
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
implemented as part of the `palindromechecker` program.

In addition to explicitly answering the aforementioned research questions,
please make sure that you explain why the performance trends are evident in your
data by referencing and explaining the source code that implements each of the
algorithms implemented in the `palindromechecker`. Once you have finished
addressing the prompts in the `writing/reflection.md` file that have `TODO`
makers given as reminders, make sure that you either delete the prompt or
carefully integrate a revised version of it into your writing.

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
