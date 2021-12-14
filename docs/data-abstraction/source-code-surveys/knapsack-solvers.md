# Knapsack Solvers

## Project Goals

This assignment invites you to study, repair, and test a Python programs called
`demonstrate-knapsack-solvers`. Specifically, it affords you to opportunity to
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
see one Python file called `demonstrate-knapsack-solvers.py`. The
`demonstrate-knapsack-solvers` module contains a defective function with the
signature `def remove_duplicates(list_one: List[Any], list_two: List[Any]) ->
Tuple[List[Any], List[Any]]`. Your task is to identify and fix the defects
inside of this function! To aid your debugging efforts, you should use and
extend the `def test_remove_duplicates() -> bool` function that should subject
the `remove_duplicates` function to several tests. The test called
`test_remove_duplicates` is implemented in the following fashion:

```python linenums="1"
list_one = [1, 2, 3, 4]
list_two = [1, 2, 5, 6]
expected_list_one = [3, 4]
expected_list_two = [5, 6]
test_case_passed = True
(actual_list_one, actual_list_two) = remove_duplicates(list_one, list_two)
if expected_list_one == actual_list_one and expected_list_two == actual_list_two:
    print("Expected output correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]")
else:
    print("Expected output not correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]")
    print(f"   actual_list_one: {actual_list_one}")
    print(f"   actual_list_two: {actual_list_two}")
    test_case_passed = False
return test_case_passed
```

Lines `1` and `2` of this function create two lists, called `list_one` and
`list_two`, that have in common the values `1` and `2`. Lines `3` and `4` of
this function indicate that, if the `remove_duplicates` function worked
correctly, then its output should be a tuple container the lists `[3, 4]` and
`[5, 6]`. After making the assumption that the test case will pass on line `5`,
the function calls `remove_duplicates` and checks to see if the expected output
equals the actual output returned by the function. If the expected output is
correct, then line `8` displays a message indicating that is the case.
Otherwise, lines `10` through `13` signal that the test did not pass and display
diagnostic output to highlight this fact for the tester. Ultimately, if this
test case passes correctly it will help to establish a confidence in the
correctness of `remove_duplicates`. When the test case for the
`remove_duplicates` function passes, then it should produce the following
output:

```
Expected output correct for input lists: [1, 2, 3, 4] and [1, 2, 5, 6]
The test case passed!
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
that you can explain the defects that you found in the function and identify all
of the key components of a test case. You should also reflect on how the tests
that you created as part of this source code survey are similar to and different
from the ones you might create with a framework like
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
