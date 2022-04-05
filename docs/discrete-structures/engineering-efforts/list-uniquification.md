# List Uniquification

## Project Goals

This engineering effort invites you to investigate how to use various discrete
structures, such as the dictionary and the set, to extract the unique values
contained inside of a list of strings. In addition to implementing and testing
the functions that perform list uniquification, you will produce the majority of
the functions for the program's command-line interface and input processing. You
will also implement functions that calculate the reduction in size and the
percent reduction in size for a list of strings with an unknown amount of
redundancy. To experimentally assess the efficiency of the `datauniquifier`
program that you implement, this project also invites you to conduct an
experiment to study, for instance, which uniquification process is best at
reducing a list's size.

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

The function 'unique_listcomprehension' took: 0.0063 sec

Estimated overall memory according to the operating system:
   37.921875 megabytes

🔍 So, did this remove a lot of duplicate data?

The number of values removed from the data: 1155
The percent reduction due to uniquification: 2.31%
```

???+ note

    Don't forget that if you want to run the `datauniqifier` you must use your
    terminal to first go into the GitHub repository containing this project and
    then go into the `datauniqifier` directory that contains the project's code.
    Finally, remember that before running the program you must run `poetry
    install` to add the dependencies.

## Adding Functionality

One of your tasks for this project is to address all of the `TODO` markers in
the `analyze`, `extract`, and `main` modules of the `datauniqifier` program.
After you have completed all of the `TODO` markers inside of the provided Python
source code, you should execute the program in a variety of configurations so as
to determine the influence that the size of the input data set, the procedure
chosen for performing uniquification, and the type of data that is input into
the uniquification procedure has on the memory and time efficiency of the
process and the amount of reduction achieved by a specific configuration.

To automatically generate data sets of different sizes, you can use the [CSV
Faker](https://github.com/pereorga/csvfaker) tool that relies on the [Faker
Package](https://github.com/joke2k/faker) package with a command like `csvfaker
--rows 50000 email job > data.txt`. Note that this command will create a data
file called `data.txt` that contains two columns, the first for an `email` and
the second for a `job`. It is also important to note that this command will
generate a data set that contains a total of 50,000 individual records of data.
Please bear in mind that running the `csvfaker` program in this fashion may,
depending on the performance characteristics of your laptop, require a long time
to run. Using the aforementioned approach for running the `csvfaker` program you
should generate different data files and then use them as the input to the
`datauniquifier` program. While everyone learning to be a proactive programmer
is encouraged to use the `csvfaker` tool to generate their own data sets, you
can complete this project's required tasks by using the provided `data.txt` file
in the `input` directory.

Along with varying the size of the data, your experiments should also consider
how the removal of redundant data values varies depending on the type of the
data input into your tool. You can do this by running the program with both
`--column 0` and `--column 1`. Finally, you should notice that the `uniquify.py`
file contains a total of three different procedures for performing
uniquification, with more approaches outlined in the blog post called [Fastest
Way to Uniquify a List in
Python](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6).
You should make sure to run the `datauniquifier` with at least the three
required ways to remove duplication, checking to see if different approaches
vary in terms of their memory consumption and execution time. Along with
noticing the trends in the data sets that you collect, you should also aim to
explain why these trends are evident, leveraging your knowledge of how the
Python programming languages uses discrete structures such as the set.

The evaluation metrics for the efficiency of the `datauniquifier` program are as
follows: (i) execution time of the approach, (ii) estimated memory overhead of
the entire Python program, (iii) reduction in the size of the column of data,
and (iv) percent reduction in the size of the column of data. As you are working
to understand each of these evaluation metrics, make sure that you review the
following Python functions that respectively calculate the reduction and percent
reduction in the size of the data.


```python linenums="1"
def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len(list_start) - len(list_final)
```

```python linenums="1"
def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

If you want to reduce the overall size of a data set through the process of
uniquification, is it better to have a large or a small value for these two
evaluation metrics? Remember, part of your goal for this assignment is to
evaluate how the different configurations of the `datauniquifier` program
influence these four evaluation metrics!

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
