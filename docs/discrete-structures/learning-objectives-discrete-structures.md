# Learning Objectives

A proactive programmer studying discrete structures should be able to
effectively demonstrate the mastery of the following learning objectives in the
categories of **mathematical communication** and **rigorous programming**.
According to [Robert Talbert](https://rtalbert.org/), a learning objective must
be "a clear, measurable action that a student should be able to do once the
lesson is over".[^1] For the purposes of this site, these learning objectives
are not for a specific lesson but rather an entire course for either an
Allegheny College student or, for the duration of self-paced learning, all other
emerging proactive programmers.

## Mathematical Communication

### Discrete Structures

  - Given the opportunity to input, store, and output a type of data, pick the
    correct discrete structure (e.g., a number, set, sequence, stream,
    dictionary, or tree) and then:
    - Implement it and integrate it into a correct, well-tested, and
      well-documented Python program consisting of between one hundred and five
      hundred lines of code.
    - Use formal and precise mathematical language to correctly describe the
      representation, behavior, and limitations of the type of data.
    - Justify the decision to use a specific discrete structure to solve a
      problem.
  - Given the formal definition of a discrete structure that uses mathematical
    notation, correctly translate it into a Python program, bearing in mind the
    ways in which the working system may diverge from the formal definition due
    to, for instance, implementation concerns related to computational costs and
    storage overheads.
  - Given the formal definition of a discrete structure and its implementation
    as a Python program, correctly describe its properties, demonstrate and
    verify those properties through testing and/or proof, describe how these
    properties are similar to and/or different from other discrete structures,
    and explain when it is appropriate to use the structure.

### Mathematical Functions

  - Leveraging an understanding of higher-order functions, lambda functions, and
    generating functions, use a problem statement involving one or more discrete
    structures to:
    - Translate the formal notation and equations used in the problem statement
      to an algorithm that describes, in a step-by-step fashion, how to solve
      the problem.
    - Pick the most suitable type of function(s) for the problem, implement it
      in an industry-standard manner using the Python programming language, and
      then use testing to demonstrate its correctness and experimentation to
      evaluate its performance.
    - After using Python type annotations to precisely document the type of the
      input and output of a Python function, use a type checker to confirm that
      all of the mathematical functions in a program communicate in a type-safe
      fashion.
    - Use formal statements to defend the validity of their design,
      implementation, and testing decisions made when solving the problem with
      the chosen function(s).

### Data Analysis

  - Given one or more sets of textual, numerical, categorical, binary, or
    combined data (that may have missing and/or corrupted data values),
    implement, use, and evaluate a Python function that support data analysis
    through these steps:
    - Input, process, and check the data sets to confirm their correctness.
    - Run an appropriate statistical technique (e.g., the calculation of a mean,
      median, or standard deviation) to summarize and analyze the data.
    - Use an appropriate data visualization technique that can create graphs and
      diagrams that highlight the salient properties of the data set (e.g., show
      the general trends in the data set while drawing attention to the
      dispersion of values).
    - Perform an appropriate data processing method that can transform the data
      into any format required by any external functions (e.g., convert from
      JSON to CSV).

## Rigorous Programming

A person learning discrete structures with the mindset of a proactive programmer
will be able to demonstrate mastery of the following programming skills:

### Proficient Python Programming

  - Write short Python functions of ten to twenty lines that have the following
    characteristics:
    - Has function and variable names that adhere to an industry-standard coding
      style.
    - Has descriptive comments for module definition and both the function's
      declaration and the function's code that adhere to an industry-standard
      coding style.
    - Features a source code format that adheres to an industry-standard coding
      style.
    - Passes an automated test suite, written with an industry-standard
      framework such as [Pytest](https://docs.pytest.org/), showing that it
      correctly implements the specification for the function.
    - Has an automated test suite, written with an industry-standard framework
      such as [Pytest](https://docs.pytest.org/), that covers at least the 80%
      of the statements and branches in the function.
    - Performs the specified operation in an efficient fashion, as determined
      through experiments that evaluate the function's performance in seconds or
      milliseconds.
    - Correctly uses assignment statements, iteration constructs, conditional
      logic, function invocation, and function recursion in a way that passes
      the function's test suite, works efficiently, and conveys the intended
      function's purpose in a Pythonic fashion.
    - Correctly uses discrete structure variables such as numbers, tuples, sets,
      streams, and sequences in a way that passes the test suite, works
      efficiently, and conveys the intended purpose of the function in a
      Pythonic fashion.
    - Correctly performs file and console input and output, ensuring that all
      input and output is displayed and stored correctly, is not corrupted, and
      is processed efficiently.
    - Correctly performs calculations for statistical properties of a data set
      (e.g., the mean, median, and standard deviation), while also clearly
      displaying the data, its relevant summarization values, and the
      interpretation of all statistical properties.
  - Writes correct Python programs consisting of between one and five hundred
    lines of source code that correctly solve problems using the aforementioned
    discrete structures.

### Python Programming Tools

  - Use a Python programming environment to complete these tasks
    while implementing a Python program consisting of between one and five
      hundred lines of code:
    - Install, upgrade, and use [Python](https://www.python.org/) 3.8 or 3.9
      programming environment to create, run, and debug a Python program through
      a terminal window and/or a text editor.
    - Use [Poetry](https://python-poetry.org/) to install a Python program's
      dependencies, create a virtual environment, and run a it without error in
      an isolated and self-contained setting.
    - Use [Docker](https://www.docker.com/) to run, in an isolated container and
      without error, a Python program, an automated test suite, and automated
      grading tools such as
      [GatorGrader](https://github.com/GatorEducator/gatorgrader).
    - Use and create a test suite implemented with
      [Pytest](https://docs.pytest.org/) to detect a failure in a Python program
      and then effectively use tools like a text editor and a terminal window to
      find and fix the failure, ultimately confirming that the Python program no
      longer contains the failure and that the fix did not compromise other
      functions in the program.
    - Use a text editor like [VS Code](https://code.visualstudio.com/) to
      participate in a remote and collaborative Python programming session by
      effectively completing the following tasks:
        - Creating and accepting an invitation to collaboratively create a
          Python program.
        - Collaboratively sharing a terminal window with a remote developer.
        - While using text-based chat and/or video communication,
          collaboratively a feature and repair a defect in a Python program.

### Using Version Control

  - Use the [GitHub](https://github.com/) platform and the
    [Git](https://git-scm.com/) version control system in the following fashion:
    - Clone a GitHub repository without error using either a terminal window or
      an extension for Git integration in a text editor like VS Code.
    - Write short and descriptive commit messages that explain the specific way
      in which a commit changes the source code and documentation in the GitHub
      repository.
    - Use GitHub [pre-commit hooks](https://pre-commit.com/) to ensure that all
      of the source code, technical writing, and commit messages adhere to the
      industry standards for content and format.
    - Navigate reports produced by [GitHub
      Actions](https://github.com/features/actions) so as to determine which
      aspects of a GitHub repository do and do not adhere to a project's
      specification.
    - Use the [GitHub Flow model](https://guides.github.com/introduction/flow/)
      to implement specific features in a branch of a GitHub repository and then
      merge that branch to the main one only after all the checks run by GitHub
      Actions pass as required and code reviews confirms the code's correctness.
    - Create and discuss programming and technical writing issues through the
      use of the [GitHub Issue
      Tracker](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/issues)
      and the [GitHub Discussion
      Forum](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/discussions),
      furnishing descriptive titles and problem descriptions that adhere to
      industry best practices and project templates.
    - Submit completed projects that pass all of the instructor-provided and
      industry-standard checks, as evidenced through the report of a passing
      build by [GitHub Actions](https://github.com/features/actions).

## Improving Objectives

As [Robert Talbert](https://rtalbert.org/) explains, a learning objective is
**clear** when it is "clear from the students' perspective" and **measurable**
when there is "some way to know whether the objective has been met" or "how far
away the learning is from meeting it". Do you see a way in which we can improve
the learning objectives for discrete structures? If you do, then please
participate in the [proactive
community](../../../proactive-community/community-connections/)
by sharing your ideas for improving them!

[^1]: See [Robert Talbert](https://rtalbert.org/)'s article entitled [How to
  Write Learning
  Objectives](https://rtalbert.org/how-to-write-learning-objectives/) for more
  details about how to design learning objectives for a academic course. From
  your perspective what does it mean to write learning objectives that are both
  clear and measurable?
