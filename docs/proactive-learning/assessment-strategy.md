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

- **GitHub Actions Build Status of Either :fontawesome-solid-check: or
  :fontawesome-solid-times::** Since additional checks on the Python source
  code and/or technical writing are encoded in GitHub Action workflows and,
  moreover, all of the GatorGrader checks are also run in GitHub Actions, your
  work will receive a checkmark grade if the last before-the-deadline build in
  GitHub Actions passes and a ✔  appears in the GitHub commit log instead of an
  ❌. The build status reported by GitHub Actions will only be a ✔ if the
  source code and technical writing in the GitHub repository pass all of both
  the GatorGrader checks and the additional checks.

- **Technical Writing Mastery of Either ✔  or ❌**: Students will also receive a
  ✔ grade when the responses to the technical writing questions presented in the
  `writing/reflection.md` reveal a mastery of technical writing skills. To
  receive a checkmark grade, the submitted writing should have correct spelling,
  grammar, punctuation, and formatting in addition to following the rules of the
  Markdown language. Your work will receive a ✔ grade for this component
  if the build report from GitHub Actions reveals that there are no detected
  mistakes in the technical writing.

- **Technical Knowledge and Skill Mastery of Either ✔  or ❌**: Students will
  also receive a checkmark grade when the GitHub repository reveals that they
  have mastered all of the technical knowledge and skills developed during the
  completion of the laboratory assignment. As a part of this grade, the
  instructor will assess aspects of the project including, but not limited to,
  the use of effective Python source code comments, correct Git commit messages,
  and accurate responses to the technical writing questions.

