# Python Programming

## Introduction

Before you attempt to install the Python programming language on your computer,
it is worth taking time to build a mental model about what a Python program
actually is and what happens when it runs on your computer. Sounds abstract,
right? In a way, it is! But, building and regularly updating a mental model for
Python programs will eliminate some of the confusion that arises when your
program does something initially unexpected.

## Notional Machine

[//]: # (Note that the phrase "notional machine" must appear on one line)

The book called [Teaching Tech
Together](https://teachtogether.tech/en/index.html) summarizes, in twelve
statements, a notional machine for the syntax, semantics, and behavior of a
Python program. Please read the twelve components of the [notional machine for
Python](http://teachtogether.tech/en/#s:models-notional) and identify both the
parts of it that you understand the best and those that are confusing. You can
share your ideas with the [proactive
community](/proactive-community/community-connections/) and then clarify points
that are confusing for others and receive feedback on your own points of
confusion. Although you should develop an intuitive understanding of all twelve
parts of the notional machine, let's review some of them now!

- **Every piece of data is stored in a two-part structure. The first part says
  what type the data is and the second part is the actual value**: This means
  that we can think of the variables in a Python program as a "box" that
  has two regions in it. The first region stores the type of data (e.g., it is a
  `str` that stores character-based data consisting of letters and symbols) and
  the second region stores the actual data itself (e.g., the word `"proactive"`
  could be stored inside of an variable of type `str`).

- **Booleans, numbers, and character strings are never modified after they are
  created**: This means that variables of type `bool`, `int`, and `str` are
  immutable and thus they never change once they are created and stored in the
  memory of a Python program. Knowing that these variables do not change after
  creation will help you to avoid some fundamental misunderstandings that often
  lead to defects in your program and thwart your goal to becoming a proactive
  programmer.

- **When code is executed, Python steps through the instructions, doing what
  each one tells it to in turn**: This reveals that the Python programming
  language has an interpreter, called `python`, that you can use to run a Python
  program.[^1] Intuitively, the process of running a Python program involves the
  interpreter running each instruction and then following its control flow that
  shows which instruction to run next.

## Installing Python

Now that you have an intuitive understanding of how a program written in the
Python programming language works, you are ready to install it on your own
computer! In his book [Introduction to Computation and Programming Using
Python](https://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-third-edition)
[John Guttag](https://people.csail.mit.edu/guttag/) writes "By now, all of the
important public domain Python libraries have been ported to Python 3. Today,
there is no reason to use Python 2." Given this observation, this site
encourages you to install the most up-to-date Python 3 version on your computer
and ensure that it is invoked by the running command `python` in your terminal
window. To get started with the installation of Python, you should review
tutorials like these:

* [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
* [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
* [How to Install Python 3 and Set Up a Local Programming Environment on Windows
  10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

If you are learning to become a proactive programmer while using a computer
running either a Linux or a MacOS, then you should install Python 3.10 by using
either the tool called [Pyenv](https://github.com/pyenv/pyenv) or the tool
called [asdf](https://asdf-vm.com/). If you are instead using a computer that
runs Windows 10, then you can attempt to install Python 3.10 using either
[Pyenv-win](https://github.com/pyenv-win/pyenv-win) or the installation
instructions in one of the aforementioned articles. Please remember that, if
you are installing Python on Windows it should either be a complete version of
the most recent version of Python (i.e., Python 3.10) and it should be
executable through the use of the `python` command in your terminal. You can
confirm that you have the correct version of Python installed on your computer
by typing `python --version` in your terminal window and then looking for the
expected version number. It is important that you do not install and attempt to
use any older versions of the Python programming language than Python 3.8.

Now that you have Python 3.10 installed on your computer you should complete all
of the steps in the tutorial called [Getting Started with Python in VS
Code](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter).
When you complete this tutorial make sure that select your installed version of
Python through VS Code and write, run, and debug a "Hello World!" program
written in Python. Along with confirming that you can run the "Hello World!"
Python program in VS Code, you should ensure that you can run the same program
in your terminal window.

Depending on your computer's hardware, operating system, and supporting
software, you will find numerous tutorials that will explain how to install all
of the software development tools needed for proactive programming. For
instance, [Ian Wootten](https://www.ianwootten.co.uk/)'s article called [Setting
Up a New M1 mac for
Development](https://www.ianwootten.co.uk/2021/03/05/setting-up-a-new-m1-mac-for-development/)
explains, among many other steps, how to install Python on a laptop running
MacOS. Regardless of which approach you adopt for installing Python on your
compute, make sure that you take careful notes at each step and plan for having
to repeat specific steps until you can confirm that you can implement and run a
simple program on your computer. If you get stuck or if you have advice to
share, make sure that you connect with the other members of the [proactive
community](/proactive-community/community-connections/)!

Now you are ready to install a tool that supports Python packaging!

[^1]: Many proactive programmers benefit from using
  [pyenv](https://github.com/pyenv/pyenv) on either MacOS or Linux and
  [pyenv-win](https://github.com/pyenv-win/pyenv-win) on Windows 10 to manage
  the installation of the Python interpreter on their computers. It is worth
  noting that these programs will install the Python programming language under
  the name `python` and not, for instance, `python3`.

--8<-- "includes/abbreviations.md"
