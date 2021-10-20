# Container Cloning

## Project Goals

This assignment invites you to study, repair, and test a Python programs called
`perform-container-cloning`. Specifically, it affords you to opportunity to
continue to practice the task of debugging and testing a Python function that
has defects inside of it. After learning more about how containers are cloned in
a Python program and why this is needed when a program iterates through a
collection while changing it at the same time, you will find a fix the fault in
the provided source code. Once you have fixed the defect, you will document a
provided test case that (i) creates an input for a function, (ii) passes that
input to the function under test, (iii) captures the output of the function
under test, and (iv) asserts that the captured function output equals the
expected output if the function was implemented correctly. Instead of using a
test automation framework to run the provided test you will run a function to
complete the aforementioned steps.

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

## Code Survey

If you change into the `source` directory of your GitHub repository, you will
see one Python file called `perform-container-cloning.py` and
`perform-abs-computation.py`. The `perform-container-cloning` module contains a
defective function with the signature `def is_prime(x: int) -> bool`. Your task
is to identify and fix the defects inside of this function! To aid your
debugging efforts, you should use and extend the `def test_is_prime() -> None`
function that should subject the `is_prime` function to several tests. The first
test in the `test_is_prime` is implemented in the following fashion:

```python linenums="1"
def test_is_prime() -> None:
    """Implement test cases for the is_prime function."""
    input_zero = 0
    expected_output_zero = False
    output_zero = is_prime(input_zero)
    if output_zero is not expected_output_zero:
        print("Expected output not correct for input of zero!")
    else:
        print("Expected output correct for input of zero!")
```

In the first part of this function, line `3` indicates that the test will input
the value of `0` to the `is_prime` function and line `4` shows that the expected
output of `is_prime` for this input is `False` because `0` is not a prime
number. Line `5` of this function calls the `is_prime` function with the
previously constructed input and then lines `6` through `9` provide some
diagnostic output that explains whether or not the output was correct.
Specifically, if the actual output from the function is not equal to the
expected output, then line `7` displays a message indicating that the output is
not correct. When the expected output is equal to `is_prime`'s actual output,
then line `9` displays a message revealing that the function works correctly.
Even though this test does not use a specific test automation framework it
illustrates the key steps that a test case should take to both find defects and
establish a confidence in the correctness of `is_prime`.

After adding more test cases to the `perform-container-cloning` module, you should
follow the same process when you debug and test the `abs` function in the
`perform-abs-computation` module. Ultimately, you should ensure that both of the
defective functions no longer have defects inside of them! For instance, when
the test cases for the `is_prime` function are passing correctly they should
produce the following output:

```
Expected output correct for input of zero!
Expected output correct for input of one!
Expected output correct for input of two!
Expected output correct for input of forty-one!
```

## Running Checks

Since this project does not use [Poetry](https://python-poetry.org/) to manage
project dependencies and virtual environments, it does not support the use of
commands like `poetry run task test`. However, you can leverage the relevant
instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about this project's program.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. Since
this is a source code survey, you should provide output from running each of the
provided Python programs on your own laptop and then explain how the program's
source code produced that output. A specific goal for this project is to ensure
that you can explain each defect that you found in the function and how the test
cases that you implemented helped you to find it. You should also reflect on how
the tests that you created as part of this source code survey are similar to and
different from the ones you might create with a framework like
[Pytest](https://docs.pytest.org/).

## Project Assessment

Since this project is source code survey, it is aligned with the **remembering**
and **understanding** levels of [Bloom's
taxonomy](proactive-learning/blooms-taxonomy/). You can learn more about how a
proactive programming expert will assess your work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet the project's specification.

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
