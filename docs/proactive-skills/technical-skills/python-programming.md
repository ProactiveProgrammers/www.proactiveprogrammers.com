# Python Programming

## Introduction

Before you attempt to install the Python Programming language on your computer,
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
share your ideas in the [proactive
community](/proactive-community/community-connections/) and then clarify points
that are confusing for others and receive feedback on your own points of
confusion. Although you should develop an intuitive understanding of the twelve
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


[^1]: Many proactive programmers benefit from using
  [pyenv](https://github.com/pyenv/pyenv) on either MacOS or Linux and
  [pyenv-win](https://github.com/pyenv-win/pyenv-win) on Windows 10 to manage
  the installation of the Python interpreter on their computers. It is worth
  noting that these programs will install the Python programming language under
  the name `python` and not, for instance, `python3`.

--8<-- "includes/abbreviations.md"
