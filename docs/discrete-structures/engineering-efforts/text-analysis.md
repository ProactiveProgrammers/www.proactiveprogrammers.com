# Text Analysis

## Project Goals

This engineering effort invites you to investigate how to use various discrete
structures, such as the dictionary and the set, to analyze all of the text in a
file. This means that your program, called `textanalysis`, must complete tasks
like (i) inputting a text file and storing its contents in a string, (ii)
extracting the paragraphs from the text file, and (iii) extracting the words in
each paragraph. Next, `textanalysis` should identify the unique words in each
paragraph, the unique words in the entire document, and the words that are
evident in all of the paragraphs of the document. To accomplish these tasks your
program will use external packages, such as
[supervenn](https://github.com/gecko984/supervenn), that make it possible to
better visualize and understand the relationships between the sets that
represent each of the paragraphs in the document. As you enhance your knowledge
of discrete structures and your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will continue to
program with VS Code, the Python programming language, and the Poetry package
manager. Ultimately, your goal for this project is to create a program that can
automatically analyze a complete text document.

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

To get started on this engineering effort, please make sure that you read the
blog post entitled [Fastest Way to Uniquify a List in
Python](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6).
As part of this assignment, you are going to implement at least three ways to
remove the duplicate values from one of the columns in a large input file that
contains automatically generated data. Here is a sample of the data that you
input into the program that you will implement as part of this assignment:

```
dana74@mahoney-perez.com,"Administrator, charities/voluntary organisations"
nathanjohnson@davila.net,Software engineer
pbush@gmail.com,"Journalist, newspaper"
timothy75@chang.com,Osteopath
gsparks@yahoo.com,"Psychologist, clinical"
daniel39@gmail.com,Logistics and distribution manager
jason85@ward.com,Logistics and distribution manager
jacobwalton@hotmail.com,Television camera operator
markmcgee@hernandez-roberts.com,IT sales professional
shannon35@allen.com,Ecologist
```

When the program accepts this type of input it will also accept a specific
column for which it should eliminate duplicates through the process of
uniquification. For instance, when the program is run with the command `poetry
run python datauniquifier --approach listcomprehension --column 1 --data-file
inputs/data.txt` then it will remove all of the duplicates from column `1` in
the data file that stores the job descriptions of specific individuals.
Alternatively, if the program was run with the command `poetry run python
datauniquifier --approach listcomprehension --column 0 --data-file
inputs/data.txt` then it will remove all of the duplicates from column `0` in
the data file that stores the email addresses of specific individuals. If we
run the first of these commands two previous commands then the program will
produce output like this:

```
The chosen approach to uniquify the file is: listcomprehension

The data file that contains the input is: input/data.txt

The data file contains 50000 data values in it!

🚀 Let's do some uniquification!

🔍 So, was this an efficient approach to uniquifying the data?

The function 'unique__reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len() - len(list_final)
```

```python
def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

One noteworthy aspect of this program is that it uses the `getattr` function to
"construct" an executable version of a Python function when provided with the
name of the function, as described in this [StackOverflow
reference](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string).
After reading the discussion on StackOverflow, make sure that you understand the
source code line `unique_result_list = function_to_call(data_column_text_list)`.
You should also notice that, instead of accepting as input the full name of a
function, this program accepts the name of the approach and then builds up the
name of the function. Can you find and understand the source code that completes
this task? Finally, this approach adopts a different approach to recording the
execution time of the three functions that perform uniquification, leveraging
the timing "decorator" described in the following function. Make sure that you
review the following [StackOverflow
discussion](https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator)
to understand how this approach works!

```python
def timing(function):
    """Define a profiling function for execution time."""
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("The function %r took: %2.4f sec" % (function.__name__, te - ts))
        return result

    return wrap
```

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section section of tasks that use
[taskipy](https://github.com/illBeRoy/taskipy):

```toml
[tool.taskipy.tasks]
black = { cmd = "black datauniqifier tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 datauniqifier tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy datauniqifier", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle datauniqifier tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint datauniqifier tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black datauniqifier tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task list`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run the command `gradle grade` to check your work. If `gradle
grade` shows that all checks pass, you will know that you made progress towards
correctly implementing and writing about `datauniqifier`. If your program has
all of the anticipated functionality, you can run the command `poetry run task
test-silent` and see that the test suite produces output like the following. It
is important to note that `datauniqifier` comes with three test suites, each of
which should pass so as to establish a confidence in its correctness.

```
tests/test_analyze.py ......                                         [ 54%]
tests/test_extract.py ..                                             [ 72%]
tests/test_uniquify.py ...                                           [100%]
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
completing this project. The finished version of your reflection should fully
describe the influence that the size of the input data set, the procedure chosen
for performing uniquification, and the type of data that is input into the
uniquification procedure has on the memory and time efficiency of the process
and the amount of size reduction achieved by a specific configuration.

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
