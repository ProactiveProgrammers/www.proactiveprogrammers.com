---
tags:
  - Conditional Logic
  - Data Types
  - Iteration Constructs
  - Functions
  - Type Annotations
---

![Contact Searching](/img/Pro-Discrete-Structures-Contact-Searching.svg){loading=lazy}

# Contact Searching

## Project Goals

This programming project invites you to implement a program called
`contactsearcher`. This program takes as input a comma separate value (CSV) file
that contains the email address and job description of a person and a string
that describes a specific job. After reading in and parsing the CSV file, the
`contactsearcher` program will find the email addresses of all the people who
have a job description that contains the provided description. Along with adding
documentation to the provided source code, you will create your own Python
functions that uses iteration constructs and conditional logic to implement a
correct program that passes the test suite and all of the checks. As you enhance
your [technical skills](/proactive-skills/introduction-proactive-skills/), you
will program with tools such as VS Code and a terminal window and the Python
programming language and the Poetry package manager.

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
    assignment! To get started, you should click the "Use this template" icon
    in the :material-github:
    [contact-searching-starter](https://github.com/ProactiveProgrammers/contact-searching-starter)
    GitHub repository and create your own version of this project's source
    code. After creating your GitHub repository, you can follow all of the
    other steps!

## Expected Output

This project invites you to implement a CSV file parsing and searching program
called `contactsearcher`. The program accepts through its command-line interface
the name of a file, in this case `input/contacts.txt`, that contains the contact
information and job title descriptions for some people. For instance, here are
the first lines of this file:

```
tylernelson@gmail.com,Careers adviser
gregory02@medina-mayer.com,"Accountant, chartered management"
jonesmiguel@hotmail.com,Health and safety inspector
rsanchez@yahoo.com,"Surveyor, planning and development"
hillfrank@ward-wood.com,"Scientist, physiological"
aaronhunter@gmail.com,"Surveyor, insurance"
kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer
bakererin@morales.com,"Programmer, multimedia"
```

It is worth noting that the `input/contacts.txt` file contains synthetic data
that the [Faker](https://github.com/joke2k/faker) program automatically
generated. With that said, after you have correctly implemented all of the
required features, running the program with the command `poetry run
contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`
will produce the following output:

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

Notice that the output confirms that there are `100` rows inside of the CSV file
called `input/contacts.txt` and that you instructed the program to return all of
the email addresses for people whose job description contains the word
`engineer`. For the current version of the CSV file, there are twelve people who
have `engineer` in their job description, including `edwardsjacob@gmail.com` who
is a `Chemical engineer` and `joe70@yahoo.com` who is a `Network engineer`.
Since the `contactsearcher` program should return the contact information for
every person who has the provided job description in their job title, searching
for `engin` instead of `engineer` should also return details about
`edwardsjacob@gmail.com` and `joe70@yahoo.com`. To learn more about how to run
this program, you can type the command `poetry run contactsearcher --help` to
see the following output showing how to use `contactsearcher`:

```
Usage: contactsearcher [OPTIONS]

  Search for either an email address of a contact who has a job in the
  file.

Options:
  --job-description TEXT  [required]
  --contacts-file PATH
  --install-completion    Install completion for the current shell.
  --show-completion       Show completion for the current shell, to copy
                          it or customize the installation.

  --help                  Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality needed to produce this output. As explained in the next section,
you are invited to add all of the missing features to ensure that
`contactsearcher` produces the expected output. Once you finish the program, it
should produce all of the expected output.

???+ note

    Recall that if you want to run `contactsearcher` you must use your terminal
    window to first go into the GitHub repository containing this project and
    then go into the `contactsearcher` directory that contains the project's
    source code. Remember that before running the program you must run `poetry
    install` to add the dependencies!

## Adding Functionality

If you study the file called `contactsearcher/contactsearcher/main.py` you will
see that it has many `TODO` markers that designate the parts of the program that
you need to implement before `contactsearcher` will produce correct output.
Along with adding requested source code to the `main` module, you should
implement the function in the `convert` module called
`search_for_email_given_job(job_description: str, contacts: str) ->
List[List[str]]`. This function takes as input two `str` variables called
`job_description` and `contacts`, with the first of these containing, for
instance, `engineer`, and the second containing all of the contents of the
provided CSV file. The `search_for_email_given_job` function should use the
`csv` package's `reader` function to input the CSV file on a row-by-row basis,
and then check each row to see if its job description contains the contents of
the `job_description` variable. If the job description on a specific line has
within it the provided `job_description`, then the function should record the
email address and continue processing the remainder of the file.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black contactsearcher tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 contactsearcher tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy contactsearcher", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle contactsearcher tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint contactsearcher tests", help = "Run the pylint checks for source code documentation" }
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
run the command `poetry run black contactsearcher tests` and it will automatically
reformat the source code.

Along with running tasks like `poetry run task lint`, you can leverage the
relevant instructions in the [technical
skills](/proactive-skills/introduction-proactive-skills/) to enter into a Docker
container and run `gradle grade` to check your work. If `gradle grade` shows
that all checks pass, you will know that you made progress towards correctly
implementing and writing about `contactsearcher`.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces the
following output. As you finish your implementation of the
`search_for_email_given_job` function you can use this test suite to confirm
that it is working correctly. If one of the test cases fails, you can use its
output to help you understand what is not yet working in the function under
test. After all of the test cases pass, you can use the command `poetry run task
all` and `gradle grade` to confirm that other aspects of your source code and
technical writing are correct.

```
tests/test_search.py .....

============================ 5 passed in 0.02s =============================
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

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block and explain the meaning of the Python source code segments that you
implemented and tested. As you answer the reflection's questions, take
particular care as you explain every computational step that occurs when running
the program with a command like `poetry run contactsearcher --job-description
"engineer" --contacts-file input/contacts.txt`.

## Project Assessment

Since this is a programming project, it is aligned with the **applying** and
**analyzing** levels of [Bloom's taxonomy](/proactive-learning/blooms-taxonomy/).
You can learn more about how a proactive programming expert will assess your
work by examining the [assessment
strategy](/proactive-learning/assessment-strategy/). From the start to the end
of this project you may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
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
