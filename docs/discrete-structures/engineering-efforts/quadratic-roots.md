# Quadratic Roots

## Project Goals

This engineering effort invites you to combine what you learned about the basics
of Python programming to implement a useful program that can use an equation to
find the roots for a quadratic equation. The program will have a command-line
interface that accepts as input the values `a`, `b`, and `c` for a quadratic
equation of the form $f(x) = a \times x^2 + b \times x + c$. As you learn more
about to translate mathematical equations into Python functions and you continue
to enhance your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will implement
and test a complete Python program while using tools such as the VS Code text
editor, a terminal window, and the Poetry package manager.

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

This project invites you to implement a quadratic root finding program called
`rootfinder`. To learn more about the equations for finding the roots of a
quadratic equation, please try out the [quadratic formula
calculator](https://www.calculatorsoup.com/calculators/algebra/quadratic-formula-calculator.php).
For instance, input `a=1`, `b=2`, and `c=1` into this calculator and see what
answer it produces. After repairing your program, as explained in the next step
of this assignment, it will also be possible for you to run the provided Python
program by typing `poetry run rootfinder --a 1 --b 2 --c 1` in your
terminal window and observing that the programs produces the following output:

```shell
⭐ Calculating the roots of a quadratic equation with:
   a = 1.0
   b = 2.0
   c = 1.0

⭐ Finished computing the roots of the equation as:
   x_one = -1.0
   x_two = -1.0
```

Does the Python program produce the same output as the quadratic formula
calculator site suggests it should? If it does, then try to run the program with
different inputs by typing `poetry run python rootfinder --a 1 --b 1 --c 1`. In
this case, your program should produce the following output:

```shell
⭐ Calculating the roots of a quadratic equation with:
   a = 1.0
   b = 1.0
   c = 1.0

⭐ Finished computing the roots of the equation as:
   x_one = (-0.49999999999999994+0.8660254037844386j)
   x_two = (-0.5-0.8660254037844386j)
```

Is this output the same as what the web-based quadratic formula calculator
produces? Please note that the output of this program includes numbers like
`-0.5-0.8660254037844386j`, which means that this is a program that has an
"imaginary" component. If you would like to learn more about "imaginary" numbers
and how you can intuitively and geometrically interpret them, please read the
[visual and intuitive guide to imaginary
numbers](https://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/),
bearing in mind that the referenced article uses the variable `i` and Python
programs always use the variable `j` to mean the same thing. Finally, please
make sure that you try your program with several additional inputs, always
confirming that it works correctly by using the web-based quadratic formula
calculator.

???+ note

    Remember, if you want to run `rootfinder` you must use your terminal to go
    into the GitHub repository containing this project and then go into the
    `rootfinder` directory that contains the project's source code. Finally,
    remember that before running the program you must run `poetry install` to
    add the dependencies. If you run into errors when using a `poetry run`
    command you can often resolve them by deleting the `.venv` directry and the
    `poetry.lock` file and the trying `poetry install` again.

## Adding Functionality

If you study the file `rootfinder/rootfinder/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `rootfinder` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```shell
================================= FAILURES =================================
__________________ test_calculate_x_values_non_imaginary ___________________

    def test_calculate_x_values_non_imaginary():
        """Check that the calculation of x values works if they are not imaginary."""
        a = 1
        b = 2
        c = 1
>       x_one, x_two = rootfind.calculate_quadratic_equation_roots(a, b, c)
E       TypeError: cannot unpack non-iterable NoneType object

tests/test_rootfind.py:20: TypeError
```

Alternatively, running the program with a command like `poetry run rootfinder
--a 1 --b 2 --c 1` will not produce any output!

In addition to `confirm_valid_file`, you must completely implement these
functions:

- `def human_readable_boolean(answer: bool) -> str`
- `def word_rootfinder(text: str, word: str) -> bool`
- `def word(word: str = typer.Option(None), dir: Path = typer.Option(None), file: Path = typer.Option(None)) -> None`

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section:

```toml
[tool.taskipy.tasks]
black = { cmd = "black rootfinder tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 rootfinder tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy rootfinder", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle rootfinder tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint rootfinder tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black rootfinder tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task list`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `rootfinder`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces output like
this:

```shell
collected 5 items

tests/test_rootfinder.py .....
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

Once you have finished both of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project.

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
