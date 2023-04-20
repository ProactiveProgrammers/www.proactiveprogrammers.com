---
tags:
  - Conditional Logic
  - Iteration Constructs
  - Functions
  - Performance
  - Time Complexity
---

![Containment Checks](/img/Pro-Data-Structures-Containment-Checks.svg){loading=lazy}

# Containment Checks

## Project Goals

This engineering effort invites you to implement and use a program called
`containmentcheck` that conducts an experiment to evaluate the performance of
containment checking using the `in` operator for different types of data
containers like tuples and lists. When you run the completed version of the
`containmentcheck` program it will allow you to specify the size of the
container, the maximum value of the integer values stored in the container, the
type of data container, and whether or not the searching algorithm should look
for a value that does or does not exceed the maximum value in the list. If you
configure it correctly, the `containmentcheck` program will total and average
time for using the `in` operator for the automatically generated lists.
Specifically, `containmentcheck` will use the
[timeit](https://docs.python.org/3/library/timeit.html) package to measure the
performance of the `in` operator for different data containers, following one
of the approaches outlined in the article called [measure execution time with
timeit in Python](https://note.nkmk.me/en/python-timeit-measure/). As you
complete this engineering effort you will experimentally evaluate the claims
in the following articles about the best way to determine if a specific value
exists inside of a data container.

- [Membership testing](https://switowski.com/blog/membership-testing)
- [Python speed](https://wiki.python.org/moin/PythonSpeed)
- [Using key in list to check if key is contained in list](https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html)
- [Why is a set faster than a list in Python?](https://www.quora.com/Why-is-a-set-faster-than-a-list-in-Python)

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
    assignment! To get started, you should click the "Use this template" button
    in the :material-github:
    [containment-checking-starter](https://github.com/ProactiveProgrammers/containment-checking-starter)
    GitHub repository and create your own version of this project's source
    code. After creating your GitHub repository, you can follow all of the
    other steps!

## Expected Output

After you finish a correct implementation of all the `containmentcheck`'s
features you can run it with the command `poetry run containmentcheck --size
32000000 --maximum 50000000 --approach list` and see that it produces output
like the following. It is worth noting that your invocation of the program will
likely produce different results than those provided because of the fact that
your laptop may have different software and hardware, and thus different
performance characteristics, than the one used to run `containmentcheck`. With
that said, a finished version of `containmentcheck` should report both the total
and average time for use the `in` operator for the specified data container and
searching approach.

```
✨ Conducting an experiment to measure the performance of containment checking!
         Type of the data container: list
         Size of the data container: 32000000
         Maximum value for a number in the data container: 50000000
         Should the value to search for exceed the maximum number? No

⏱  Total time for running 10 runs in 3 benchmark campaigns: [2.778451125999709, 2.6102711579987954, 2.6405498099993565]

🧮 Average time for running one of 10 runs in 3 benchmark campaigns: [0.2778451125999709, 0.2610271157998795, 0.26405498099993563]
```

Finally, don't forget that you can display `containmentcheck`'s help menu and
learn more about its features by typing `poetry run containmentcheck --help` to
show the following output. It is worth noting that all of the parameters to the
`containmentcheck` program, excepting those connected to completion of
command-line arguments or the help menu, are required. This means that the
`containmentcheck` will produce an error if you do not specify the four required
parameters that describe the experiment.

```
Usage: containmentcheck [OPTIONS]

  Conduct an experiment to measure the performance of containment
  checking.

Options:
  --size INTEGER               [default: 5]
  --maximum INTEGER            [default: 25]
  --exceed / --no-exceed       [default: False]
  --approach [list|set|tuple]  [default: list]
  --install-completion         Install completion for the current shell.
  --show-completion            Show completion for the current shell, to
                               copy it or customize the installation.

  --help                       Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality to produce the output displayed in this section. As the next
section explains, you should add the features needed to ensure that
`containmentcheck` produces the expected output! After implementing a function
that can automatically generate a data container that has random numerical
values inside of it, you will need to create each of the containment checking
functions for all of the supported data containers (i.e., list, tuple, and set).

???+ note

    Don't forget that if you want to run the `containmentcheck` you must use your
    terminal window to first go into the GitHub repository containing this
    project and then go into the `containmentcheck/` directory that contains the
    project's source code. Finally, remember that before running the program you
    must run `poetry install` to add its dependencies, such as Pytest for
    automated testing and Rich for colorful output!

## Adding Functionality

If you study the file `containmentcheck/containmentcheck/main.py` you will see
that it has many `TODO` markers that designate the functions you must implement
so as to ensure that `containmentcheck` runs the desired experiment and produces
the correct output. Once you complete a task associated with a `TODO` marker,
make sure that you delete it and revise the prompt associated with the marker
into a meaningful comment. Specifically, you will need to implement the
following Python functions:

- `def generate_random_number(maximum: int, exceed: bool = False) -> int`:
  automatically create a random number starting at zero and going up to the
  `maximum` value. When `exceed` is `true` the function should generate a number
  that is greater than the specified maximum value.

- `def generate_random_container(size: int, maximum: int, make_tuple: bool =
  False) -> Union[List[int], Tuple[int, ...]]`: automatically generate a data
  container that must be either of type `List` or type `Tuple`, ensuring that it
  contains exactly `size` numbers that are never bigger than the specified
  `maximum`.

- `def containment_check_list(thelist: List[int], number: int) -> bool`: use the
  `in` operator to perform containment checking for the provided list.

- `def containment_check_tuple(thetuple: Tuple[int], number: int) -> bool`: use
  the `in` operator to perform containment checking for the provided tuple.

- `def containment_check_set(thelist: List[int], number: int) -> bool`: after
  converting the provided list to a set, use the `in` operator to perform
  containment checking for the set. This function will allow you to
  experimentally evaluate the [conventional
  wisdom](https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html)
  that a develop can improve the performance of their Python program by
  converting a list to a set before using the `in` operator.

Ultimately, you should design your own experiment and state and answer your own
research questions, focusing on the following key issues:

- The data container: `set`, `list`, and `tuple`
- The size of the data container: small values (e.g., 1 million numbers) to big
  values (e.g., 32 million numbers)
- Whether or not the value that it being searched for is `in` the list
- The maximum value of the numbers that are inside of the data container

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black containmentcheck --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 containmentcheck", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy containmentcheck", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle containmentcheck tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint containmentcheck", help = "Run the pylint checks for source code documentation" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to
automatically run all of the linters designed to check the Python source code in
your program and its test suite. You can also use the command `poetry run task
black` to confirm that your source code adheres to the industry-standard format
defined by the `black` tool. If it does not adhere to the standard then you can
run the command `poetry run black containmentcheck` and it will automatically
reformat the source code. Along with running tasks like `poetry run task lint`,
you can leverage the relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `containmentcheck`.

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
instance, you should provide the output of the Python program in several fenced
code blocks, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project. A specific goal for this project's reflection is to
ensure that you can explain Python source code that uses the
[timeit](https://docs.python.org/3/library/timeit.html) package to evaluate the
performance of a specific approach to containment checking, as illustrated by
the following code segment.

```python
number_runs = 10
number_repeats = 3
execution_times = timeit.Timer(containment_check_lambda).repeat(
    repeat=number_repeats, number=number_runs
```

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](/proactive-learning/blooms-taxonomy/). You can learn more about how a
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
