# Sorting Algorithms

## Project Goals

This engineering effort invites you to implement and use a program called
`listsorting` that performs a doubling experiment to evaluate the performance of
several different sorting algorithms. First, you will follow the [Sorting
Algorithms in Python](https://realpython.com/sorting-algorithms-python/)
tutorial from [Real Python](https://realpython.com/) and add certain sorting
algorithms, like bubble sort and quick sort, to your project. After you have
implemented all of the required sorting algorithms, you will use the provided
benchmarking framework to conduct a doubling experiment. This doubling
experiment will invoke a specific sorting algorithm while repeatedly double the
size of the input to the sorting algorithm for a specific number of doubling
rounds. Since the doubling experiment enables you to calculate a doubling ratio,
it enables you to experimentally predict the likely worst-case time complexity
of each sorting algorithms. In addition to implementing the sorting algorithms
and extending the benchmarking framework, you will use a comprehensive
command-line interface, implemented with [Typer](https://typer.tiangolo.com/),
that allows you to easily control the execution of a doubling experiment.
Finally, you will use your empirical results from using the `listsorting`
program to better understand the performance trade-offs associated with sorting
algorithms implemented in Python.

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

This project invites you to implement a Python program, called `listsorting`,
that features different ways to compute all of the numbers in the Fibonacci
sequence up to a specified maximum number. After you finish a correct
implementation of all the program's features, running it with the command
`poetry run listsorting --starting-size 100 --number-doubles 5 --approach
insertion`, causes it to produce output like the following. With that said,
please remember that when you run the `listsorting` program your computer it
will likely produce different performance results! Importantly, this output
shows that the `listsorting` program ran the insertion sort algorithm, denoted
`insertion`, for a total of `5` rounds in a doubling experiment that created
input sizes that ranged from `100` to `1600`. When `listsorting` runs the
experiment, it uses the [timeit](https://docs.python.org/3/library/timeit.html)
package to measure the `min`, `max`, and `avg` execution time of the algorithm.

```
✨ Conducting an experiment to measure the performance of list sorting!

   The chosen sorting algorithm: insertion
   Starting size of the data container: 100
   Number of doubles to execute: 5

✨ Here are the results from running the experiment!

  Input Size    Min time (s)    Max time (s)    Avg time (s)
------------  --------------  --------------  --------------
         100         0.00198         0.00228         0.0021
         200         0.00791         0.00831         0.00804
         400         0.03091         0.03179         0.03129
         800         0.1397          0.14232         0.141
        1600         0.56098         0.58918         0.57665
```

These experimental results suggest that insertion sort has a doubling ratio of
$\frac{0.57665}{0.141} \approx 4.0897$. If you look at the last row of the data
table you will see that, for the input sizes of `1600` and `800`, the average
execution time for insertion sort was $0.57665$ and $0.141$ seconds,
respectively. Dividing the execution time for the larger input size by the
execution time of the smaller input size yields the doubling ratio of
approximately $4.0897$, suggestion that insertion sort is a $O(n^2)$ algorithm
because a doubling of the input size caused a quadrupling of the execution time.
Finally, don't forget that you can display `listsorting`'s help menu and learn
more about its features by typing `poetry run listsorting --help` to show the
following output. Don't forget that the `listsorting` program should also run
experiments for the other sorting algorithms, such as bubble sort and quick
sort! You can also run `listsorting` with larger input sizes or more rounds of
input doubling --- but be aware of the fact that your experiments could take a
long time to finish for certain algorithms!

```
Usage: listsorting [OPTIONS]

  Conduct a doubling experiment to measure the performance of list
  sorting for various algorithms.

Options:
  --starting-size INTEGER         [default: 1000000]
  --maximum-value INTEGER         [default: 10000]
  --number-doubles INTEGER        [default: 10]
  --approach [bubble|insertion|merge|quick|tim]
                                  [default: bubble]
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
`listsorting` produces the expected output! Importantly, this project
invites you to add both a recursion-based and reversal-based algorithm for
palindrome checking.

???+ note

    Don't forget that if you want to run the `listsorting` program you must use
    your terminal window to first go into the GitHub repository containing this
    project and then go into the `listsorting` directory that contains the
    project's source code. Finally, remember that before running the program you
    must run `poetry install` to add its dependencies, such as Pyinstrument,
    Pytest, and Rich.

## Adding Functionality

If you study the file `listsorting/listsorting/main.py` you will see
that it has many `TODO` markers that designate the parts of the program that you
need to implement before `listsorting` will produce correct output. Once
you complete a task associated with a `TODO` marker, make sure that you delete
it and revise the prompt associated with the marker into a meaningful comment.
To ensure that the program works correctly, you must implement all of these
functions in the `palindrome` module:

- `def to_chars(word: str) -> str`
- `def is_palindrome(word: str) -> bool`
- `def is_palindrome_recursive(word: str) -> bool`
- `is_palindrome_reverse(word: str) -> bool`

After finishing your implementation of `listsorting` you should repeatedly
run the program in different configurations to confirm that it produces the
correct output. Since the `listsorting` provides a checking mode based on
reversing the string or recursively checking the string, you should make sure
that both approaches work correctly. You should also confirm that the
`listsorting` can correctly determine when a word both is and is not a
palindrome. Here are some examples that show the program's correct execution for
different values for the `--word` and `--approach` arguments. If you correctly
resolve all of the `TODO` markers in the provided source code your program
should produce the same output for each of these commands.

- `poetry run listsorting --word civic --approach reverse`

```
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- `poetry run listsorting --word civic --approach reverse`

```
✨ Awesome, using the reverse approach for palindrome checking!

🔖 Going to check to see if the word "civic" is a palindrome!

😆 Is this word a palindrome? Yes, it is!
```

- `poetry run listsorting --word origin --approach recursive`

```
✨ Awesome, using the recursive approach for palindrome checking!

🔖 Going to check to see if the word "origin" is a palindrome!

😆 Is this word a palindrome? No, it is not!
```

- `poetry run listsorting --word origin --approach reverse`

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
black = { cmd = "black listsorting tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 listsorting tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy listsorting", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle listsorting tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint listsorting tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black listsorting tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `listsorting`. If your program
has all of the anticipated functionality, you can run the command `poetry run
task test` and see that the test suite produces output like the following. If
some of the provided tests do not pass, then you should review the test output
to see what is wrong as you fix any required functions that are broken.

```
tests/test_main.py ....
tests/test_palindrome.py ....
tests/test_util.py ..
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
to continue to explore how test cases help a developer to both establish a
confidence in the correctness of and to find bugs in a Python program. Once you
have finished addressing the prompts in the `writing/reflection.md` file that
have `TODO` makers given as reminders, make sure that you either delete the
prompt or carefully integrate a revised version of it into your writing.

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
