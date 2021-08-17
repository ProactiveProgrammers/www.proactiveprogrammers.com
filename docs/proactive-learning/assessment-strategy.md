# Assessment Strategy

--8<-- "includes/admonitions/admonish-github.md"

All learners will complete all of their work through an industry-standard
platform called [GitHub](https://www.github.com). If they have not done so
already, learners should create a free GitHub account. They will use this
account and the GitHub repositories associated with it to receive starter
materials and submit the final version of each assignment.

Learners will receive rapid feedback on their work through a tool called
[GatorGrader](https://github.com/GatorEducator/gatorgrader). The instructor will
define GatorGrader checks for each type of assignment. A learner's job will be
to use a programming language, like Python, to implement a complete solution
that passes all of the GatorGrader checks. Learners should also complete writing
tasks that demonstrate their knowledge of the technical knowledge and skills
developed as part of an assignment. In addition to running the GatorGrader tool
on their laptop, learners will see the results from running GatorGrader checks
in the continuous integration environment called [GitHub
Actions](https://github.com/features/actions).

A learner will receive a separate GitHub repository for each engineering effort
and programming project while all of the source code surveys will exist in a
single GitHub repository. Moreover, each [assignment type](assignment-types.md)
has its own assessment strategy!

--8<-- "includes/admonitions/admonish-external.md"

## Engineering Efforts

Leveraging the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a learner receives on an engineering effort will be based on
whether or not it meets the standards for technical work in the fields of
discrete structures. Instead of receiving a single numerical or letter grade for
this assignment, the grade for an engineering effort will have the following
components:

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

- **Overall Technical Knowledge and Skill Mastery of Either
  :fontawesome-solid-check: or :fontawesome-solid-times:**: An engineering
  effort will also receive a checkmark grade when the content of the GitHub
  repository reveals the mastery of the technical knowledge and skills developed
  during the completion of the project. As a part of this grade, the instructor
  will assess aspects of the project including, but not limited to, the
  demonstration of the mastery of the specific
  [technical](../../proactive-skills/technical-skills/introduction-technical-skills/)
  and
  [professional](../../proactive-skills/professional-skills/introduction-professional-skills/)
  skills associated with proactive programming and the accuracy of the responses
  to the technical writing questions.

## Programming Projects

Again leveraging the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a learner receives on a programming project will be based on
whether or not it meets the standards for technical work in the fields of
discrete structures as evidenced by:

- **GitHub Actions Build Status of Either :fontawesome-solid-check: or
  :fontawesome-solid-times::** A programming project will receive a checkmark
  grade if the last before-the-deadline build in GitHub Actions passes and a
  :fontawesome-solid-check: appears in the GitHub commit log instead of an
  :fontawesome-solid-times:. The build status reported by GitHub Actions will
  only be a :fontawesome-solid-check: if the source code and technical writing
  in the GitHub repository pass both the GatorGrader checks and the additional
  checks pass in GitHub Actions.

## Source Code Surveys

Again leveraging the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a learner receives on a source code survey will be based on
whether or not it meets the standards for technical work in the fields of
discrete structures as evidenced by:

- **GitHub Actions Build Status of Either :fontawesome-solid-check: or
  :fontawesome-solid-times::** A source code survey will receive a checkmark
  grade if the last before-the-deadline build in GitHub Actions passes and a
  :fontawesome-solid-check: appears in the GitHub commit log instead of an
  :fontawesome-solid-times:. The build status reported by GitHub Actions will
  only be a :fontawesome-solid-check: if the source code and program output
  exist in the repository and the program output and the written responses pass
  any checks run in GitHub Actions.

## Advance Feedback

Learners who wish to receive feedback on their work for any assignment should
first open an issue on the issue tracker for their assignment's GitHub
repository, giving an appropriate title and description for the type of feedback
that they would like the instructor to provide. After creating this issue, they
will see that GitHub has created a unique web site that references it. To alert
the instructor to the fact that the issue was created and that you want feedback
on your work, please send it to him by a Slack direct message at least 24 hours
in advance of the project's due date. After the instructor responds to the
issue, please resolve all of the stated concerns and participate in the
discussion until the issue is resolved and ultimately marked as closed.

## Assessment Delivery

The instructor invites learners to incrementally complete all of the
learning objectives for an engineering effort, programming project, and source
code survey. As long as a learner's work passes all of the GatorGrader checks
before an assignment's deadline, they will receive full credit for that part of
an assignment's grade. After the deadline for project submission, all grades for
a project will be reported through a student's GitHub repository using either
messages in the GitHub repository's commit log, issues raised in the issue
tracker, or comments on a pull request in the GitHub repository. Learners should
ask questions about their grade for a project on GitHub so as to facilitate an
effective conversation about the submitted deliverables and to ensure that a
learner can ultimately master all of the technical knowledge and skills
developed as part of that assignment's exploration of a specific topic in the
field of discrete structures.

## Assignment Discussion

Learners who wish to receive feedback on their work for any graded assignment
should leave question in the same region of Github where the instructor
submitted the assignment's grade. For example, if the instructor submits the
grade to a pull request in the repository for an engineering effort, then you
should ask questions about your grade in that pull request, bearing in mind the
need to @-mention the instructor in the body of your comment. Learners can
continue to discuss the graded assignment with the instructor until they
understand all the technical topics that were the focus of the particular
assignment.
