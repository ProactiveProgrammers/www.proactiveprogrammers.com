---
tags:
  - Conditional Logic
  - Iteration Constructs
  - File I/O
  - Functions
  - Testing
---

![File Searching](/img/Pro-Discrete-Structures-File-Searching.svg){loading=lazy}

# File Searching

## Project Goals

This engineering effort invites you to combine what you learned about the basics
of Python programming to implement a useful program that can search for a word
in a file. As you enhance your [technical
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

???+ note

    If you are an emerging proactive programmer who is not enrolled in a
    Computer Science class at Allegheny College, you can still work on this
    assignment!
    To get started, you should click the "Use this template" icon in the
    :material-github:
    [file-search-starter](https://github.com/ProactiveProgrammers/file-search-starter)
    GitHub repository and create your own version of this project's source code.
    After creating your GitHub repository, you can follow all of the other
    steps!

## Expected Output

This project invites you to implement a file searching program called `search`.
The `search` program takes as input a word (e.g., "proactive") and determines
whether or not it is in the text of a file provided on the input. For instance,
if the file called `input/proactive.txt` contains inside of the text on the main
page of this web site, then searching for the word `proactive` with the
command `poetry run search --word ethical --dir input --file proactive.txt`
yields:

```shell
😃 Searching through the file called input/proactive.txt!

Was the word "ethical" found in the file input/proactive.txt? Yes
```

When you search for a word that does not appear inside of the input file with a
command like `poetry run search --word conundrum --dir input --file
proactive.txt` then the program will produce the following output:

```shell
😃 Searching through the file called input/proactive.txt!

Was the word "conundrum" found in the file input/proactive.txt? No
```

Once your program is working correctly, you should also try to use it when
specify a file that is not available on your computer! For instance, if you run
it with the command `poetry run search --word proactive --dir input --file
notfound.txt` then it will not perform a search and instead produce the
following output:

```shell
😃 Searching through the file called input/notfound.txt!

🤷 input/notfound.txt was not a valid file
```

???+ note

    Don't forget that if you want to run the `search` program you must use your
    terminal window to first go into the GitHub repository containing this
    project and then go into the `search` directory that contains the project's
    source code. Finally, remember that before running the program you must run
    `poetry install` to add the dependencies.

## Adding Functionality

If you study the file `search/search/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `search` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```
================================== ERRORS ==================================
__________________ ERROR collecting tests/test_search.py ___________________
tests/test_search.py:5: in <module>
    from search import main
search/main.py:31: in <module>
    ???
E   NameError: name 'cli' is not defined
========================= short test summary info ==========================
ERROR tests/test_search.py - NameError: name 'cli' is not defined
!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!
============================= 1 error in 0.11s =============================
```

Alternatively, running the program with a command like `poetry run search --word
ethical --dir input --file proactive.txt` will produce the following output:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/gkapfham/.pyenv/versions/3.9.2/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 790, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  [...]
    @cli.command()
NameError: name 'cli' is not defined
```

This output suggests that the `cli` variable was not correctly declared! After
declaring the `cli` variable in the appropriate fashion, following the relevant
instructions in the description of the [technical
skills](/proactive-skills/introduction-proactive-skills/), you should find the
other `TODO` markers and correctly resolve them. For instance, you can add this
function to the `main.py` file:

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

Line `1` of the above source code segment contains the signature for the
`confirm_valid_file` function, showing that it takes as input a `file` variable
that is of type `Path` and returns a `bool` to indicate whether or not the file
is valid. If the conditional logic on lines `4` and `6` confirms that the `file`
variable is both not equal to `None` and is, in fact, a file, then the function
returns `True`. Otherwise, line `9` of `confirm_valid_file` returns `False` to
indicate that the provided `file` is not valid.

In addition to `confirm_valid_file`, you must completely implement these
functions:

- `def human_readable_boolean(answer: bool) -> str`
- `def word_search(text: str, word: str) -> bool`
- `def word(word: str = typer.Option(None), dir: Path = typer.Option(None), file: Path = typer.Option(None)) -> None`

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable tasks like
`lint`. If you are in the `search` directory that contains the `pyproject.toml`
file and the `poetry.lock` file, the tasks in this section make it easy to run
commands like `poetry run task lint` to automatically run all of the linters
designed to check the Python source code in your program and its test suite. You
can also use the command `poetry run task black` to confirm that your source
code adheres to the industry-standard format defined by the `black` tool. If it
does not adhere to the standard then you can run the command `poetry run black
search tests` and it will automatically reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to run the command
`gatorgrade --config config/gatorgrade.yml` to check your work. If your work
meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. You can study the `config/gatorgrade.yml` file in your repository
to learn how the :material-github:
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program runs
:material-github: [GatorGrader](https://github.com/GatorEducator/gatorgrader)
to automatically check your program and technical writing.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces output like
this:

```shell
collected 5 items

tests/test_search.py .....
```

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
taxonomy](/proactive-learning/blooms-taxonomy/). You can learn more about how a
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
