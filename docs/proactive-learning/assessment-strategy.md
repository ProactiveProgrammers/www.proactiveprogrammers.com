# Assessment Strategy

--8<-- "includes/admonitions/admonish-github.md"

All learners will complete all of their work through an industry-standard
platform called [GitHub](https://www.github.com). If they have not done so
already, learners should create a free GitHub account. They will use this
account and the GitHub repositories associated with it to receive starter
materials and submit the final version of each assignment.

Learners will receive rapid feedback on their work through a tool called
[GatorGrader](https://github.com/GatorEducator/gatorgrader). The instructor will
define GatorGrader checks for each type of assignment and your job will be to
use a programming language, like Python, to implement a complete solution that
passes all of the GatorGrader checks. In addition to running the GatorGrader
tool on your laptop, learners will see the results from running GatorGrader
checks in the [GitHub Actions](https://github.com/features/actions) continuous
integration environment.

Each [assignment type](assignment-types.md) has its own assessment strategy!

--8<-- "includes/admonitions/admonish-external.md"

## Engineering Efforts

Leveraging the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a student receives on an engineering effort will be based on
whether or not it meets the standards for technical work in the fields of
software engineering and discrete structures. Instead of receiving a single
numerical or letter grade for this assignment, the grade for an engineering
effort will have the following components:

- **Percentage of Correct GatorGrader Checks Ranging Between 0 and 100**: The
  submitted Python program must pass all of GatorGrader's checks by, for
  instance, ensuring that it produces the correct output and has all of the
  required characteristics. The technical writing must pass all of
  GatorGrader's checks about, for instance, the length of its output and its
  use of the required Markdown language features for technical writing. For
  this component of the grade for an engineering effort, the project will
  receive a percentage, ranging from 0 to 100, that corresponds to the
  percentage of GatorGrader checks that automatically pass inside of a GitHub
  Actions build.

- **Technical Writing Mastery of Either :fontawesome-solid-check: or
  :fontawesome-solid-times:**: The responses to the technical writing questions
  will receive a :fontawesome-solid-check: when they reveal a mastery of
  technical writing skills. To receive a checkmark grade, the submitted writing
  should have correct spelling, grammar, punctuation, and formatting in
  addition to following the rules of the Markdown language. The technical
  writing will receive a checkmark grade if the build report from GitHub
  Actions reveals no detected mistakes in the technical writing.

- **GitHub Actions Build Status of Either :fontawesome-solid-check: or
  :fontawesome-solid-times::** Since additional checks on the Python source
  code and technical writing are encoded in GitHub Action workflows and,
  moreover, all of the GatorGrader checks are also run in GitHub Actions, an
  engineering effort will receive a checkmark grade if the last
  before-the-deadline build in GitHub Actions passes and a
  :fontawesome-solid-check: appears in the GitHub commit log instead of an
  :fontawesome-solid-times:. The build status reported by GitHub Actions will
  only be a :fontawesome-solid-check: if the source code and technical writing
  in the GitHub repository pass both the GatorGrader checks and the additional
  checks encoded in the configuration of GitHub Actions.

- **Technical Knowledge and Skill Mastery of Either :fontawesome-solid-check:
  or :fontawesome-solid-times:**: An engineering effort will also receive a
  checkmark grade when the content of the GitHub repository reveals the mastery
  of the technical knowledge and skills developed during the completion of the
  project. As a part of this grade, the instructor will assess aspects of the
  project including, but not limited to, the demonstration of the mastery of
  the specific
  [technical](../../proactive-skills/technical-skills/introduction-technical-skills/)
  and
  [professional](../../proactive-skills/professional-skills/introduction-professional-skills/)
  skills associated with proactive programming and the accuracy of the
  responses to the technical writing questions.
