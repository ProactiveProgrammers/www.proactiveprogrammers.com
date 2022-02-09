# Collatz Creation

## Project Goals

This engineering effort invites you to investigate how to apply all that
you have learned about Python programming and discrete structures to
implement a program, called `collatzcreation`, that can solve the
[Longest Collatz
Sequence](https://projecteuler.net/index.php?section=problems&id=014)
problem posed by [Project Euler](https://projecteuler.net/). The Collatz
sequence is defined for the positive integers according to the rule that
$n$ becomes $\frac{n}{2}$ when $n$ is even and $3n + 1$ when $n$ is odd.
To date, computer scientists and mathematicians do not know whether or
not the Collatz sequence will terminate with the value of $1$ when it is
started with an arbitrary positive integer $n$. However, for all of the
values tried to date the sequence always yields a Collatz chain (i.e.,
the sequence values that arise from iteratively applying the rules) of a
finite length. The Longest Collatz Sequence problem posed by Project
Euler asks "Which starting number, under one million, produces the
longest chain"? The `collatzcreation` program that you implement for
this project should efficiently produce an answer to this question.

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

As part of this assignment, you are going to implement a `collatzcreator` program
that takes as input a complete document stored in a text file and then performs
an automated analysis of the document's contents. For instance, here is an
excerpt of a text file that you could input into your program. Notably, the
entire file has a total of 5 paragraphs that consist of 19 lines, not including
the blank lines that separate the paragraphs.

```text
Make enables the end user to build and install your package without knowing
the details of how that is done --- because these details are recorded in the
makefile that you supply.

Make figures out automatically which files it needs to update, based on which
source files have changed. It also automatically determines the proper order
for updating files, in case one non-source file depends on another non-source
file.
```

If you run the finished version of the `collatzcreator` program with the command
`poetry run collatzcreator --input-file text/input_one.txt --analyze`, where
`text/input_one.txt` is the file that contains the above excerpt and the
`--analyze` flag tells the program to perform a textual analysis, you should see
the following output in your terminal window. It is worth noting that the
program will also produce additional output that explains how the `supervenn`
package analyzed the sets representing each paragraph in order to produce its
graphical representation of the text document. You can learn more about both the
way in which `supervenn` uses the `FrozenSet` discrete structure and how you
should interpret the visualization that supervenn produces by visiting the
[supervenn](https://github.com/gecko984/supervenn) web site. To see the
visualization produced by `supervenn` you should use a graphics preview program
to load the file `graphics/set-visualization.png`. For the input file called
`text/input_one.txt`, what trends does the visualization show you about the
overlap between the words in the document's paragraphs?

```text
✨ Let's characterize the file and its words!

        The input file contains 23 lines, including blank lines!
        The input file contains 19 lines, not including blank lines!
        The input file contains 5 paragraphs!
        The input file contains 118 unique words across all sets!
        The words that are found across all sets are: {'Make', 'to'}

🖌 Saving the visualization in graphics/set-visualization.png
```

???+ note

    Don't forget that if you want to run the `collatzcreator` you must use your
    terminal to first go into the GitHub repository containing this project and
    then go into the `collatzcreator` directory that contains the project's
    code. Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

If you study the file `collatzcreator/collatzcreator/main.py` you will see that it
has all of the functionality needed to implement the entire command-line
interface. Furthermore, the file `collatzcreator/collatzcreator/visualize.py` shows
that it also has all of the functions needed to use `supervenn` the create a
visualization of the word-level overlap in the provided text file. For this
assignment, the `collatzcreator/collatzcreator/extract.py` file contains the `TODO`
markers that explain how to implement the following functions.

- `def extract_lines_including_blanks(input_lines: str) -> List[str]:`
- `def extract_lines_not_including_blanks(input_lines: str) -> List[str]:`
- `def extract_paragraphs(input_lines: str) -> List[str]:`
- `def extract_unique_words_paragraphs(paragraphs: List[str]) -> List[Set[str]]:`
- `def extract_unique_words(sets: List[Set[str]]) -> Set[str]:`
- `def extract_common_words(sets: List[Set[str]]) -> Set[str]:`

You can study the source code in the `collatzcreator/collatzcreator/main.py` file to
see the input and expected output of each of the above functions. For instance,
here is the way in which the `main` function in the `main.py` file calls the
first function in the above list: `input_line_count =
len(extract.extract_lines_including_blanks(input_text))`. Note that it accepts
as input the `str` called `input_text` that contains the textual input from the
file specified on the command-line interface.

The following code segment provides the complete implementation of the
`extract_lines_including_blanks` function. The function signature on line `1`
shows that `extract_lines_including_blanks` will accept a `str` as input and
return a `List` of `str` as output, with each index in the `List` being a single
line inside of the input `str` called `input_lines`. Line `3` of this function
uses the `splitlines` function to create the required `List` of `str` and then
line `4` returns it. It is important to note that this function does not filter
out the blank lines that `splitlines` returns &mdash; which is the job of the
`def extract_lines_not_including_blanks(input_lines: str) -> List[str]:`
function that you also need to create! Once you have implemented the required
functions, the `collatzcreator` should produce the expected output.

```python linenums="1"
def extract_lines_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, including the blanks lines."""
    lines_text = input_lines.splitlines()
    return lines_text
```

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section section of tasks that use
[taskipy](https://github.com/illBeRoy/taskipy):

```toml
black = { cmd = "black collatzcreator --check", help = "Run the black checks for source code format" }
reformat = { cmd = "black collatzcreator", help = "Run the black reformatter for source code style" }
flake8 = { cmd = "flake8 collatzcreator", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy collatzcreator", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle collatzcreator", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint collatzcreator", help = "Run the pylint checks for source code documentation" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to
automatically run all of the linters designed to check the Python source code in
your program and its test suite. You can also use the command `poetry run task
black` to confirm that your source code adheres to the industry-standard format
defined by the `black` tool. If it does not adhere to the standard then you can
run the command `poetry run black collatzcreator tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task list`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `collatzcreator`. If there are checks
that did not pass correctly, which you can see in either your terminal window or
the logs from GitHub Actions, then you should read them carefully and take the
suggested steps to repair the problems.

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
completing this project. One of the main goals of the reflection is for you to
explain the trends that you see in the different provided text files. You should
also discuss how the `collatzcreator` program uses discrete structures like the
list and the set to automatically characterize the text of a complete document.

## Project Assessment

Since this project is an engineering effort, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet every aspect of the project's
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
