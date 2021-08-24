# Python Packaging

## Installing Poetry

It is common for a proactive programmer to run their Python programs in a
virtual environment that contains isolated versions of all the packages on which
a specific program depends. Although there are many different ways to package a
Python program and manage its dependencies, a new tool called
[Poetry](https://python-poetry.org/) offers a flexible and easy-to-use approach.
Bearing in mind that the installation instructions for Poetry vary depending on
whether your computer runs Windows, MacOS, or Linux, follow the installation
instructions in the [Poetry Documentation](https://python-poetry.org/docs/) to
ensure that the `poetry --version` command displays the expected output in your
terminal window.

## Using Poetry

Once you have installed Poetry, you should complete a tutorial called [Building
a Package](https://typer.tiangolo.com/tutorial/package/) where you can learn how
to use Poetry to create a command-line application using the
[Typer](https://typer.tiangolo.com/) package for creating a Python program with
a command-line interface! It is worth noting that this tutorial will ask you to
write Python source code. If you are not yet familiar with the Python
programming language you can copy and paste the code from the tutorial to the
appropriate file that you are editing with VS Code. That is, if you are getting
started as a proactive Python programmer you should focus on learning how to use
Poetry and consider less on learning the Python language. As you complete the
tutorial, make sure that you consider the following commands in Poetry:

* `poetry new`: creates a new Poetry project
* `poetry add`: adds a new dependency to a Poetry project
* `poetry install`: install all dependencies for a Poetry project
* `poetry shell`: enters into a shell containing all dependencies
* `poetry run`: runs a program in a virtual environment
* `poetry build`: build a packaged version of the Poetry project

Please note that, at least for now, you don't need to focus on learning how to
publish the tutorial package to the [Python Package Index](https://pypi.org/)!
With that said, if you are interested in doing so, you should now be able to
install your program with either
[pip](https://docs.python.org/3/installing/index.html) or
[pipx](https://github.com/pypa/pipx) and run it as a stand-alone executable. If
you get stuck on the use of either Poetry or Typer, make sure that you ask for
help from the other members of the [proactive
community](/proactive-community/community-connections/).

After reviewing all of these technical skills, you are ready to learn more about
the professional skills of a proactive programmer!
