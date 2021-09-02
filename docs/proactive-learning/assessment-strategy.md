# Assessment Strategy

To ensure that proactive programmers can effectively grow in their knowledge of
software engineering as they study topics such as [data
abstraction](/data-abstraction/introduction-data-abstraction) and [discrete
structures](/discrete-structures/introduction-discrete-structures), the projects
that they complete will be receive rapid and frequent feedback, in adherence to
the grading principles set forth by [Robert Talbert](https://rtalbert.org/).
Specifically, the team of proactive programming experts will conduct assessments
with these principles in mind.[^1]

- **Clearly Defined Standards**: All projects will have a specification that
  clearly defines the characteristics of acceptable program source code and
  technical writing.
- **Helpful Feedback**: Project feedback will offer actionable suggestions for
  ways to better ensure that a source code or technical writing more fully
  adheres to the specification.
- **Scores Suggest Progress**: The scores assigned to a project will offer
  meaningful insight into the progress that a proactive programmer made to more
  fully meet the specification.
- **Reattempts without Penalty**: All projects will have a completion period
  during which a proactive programmer may repeatedly attempt to meet the
  specification without penalty.

--8<-- "includes/admonitions/admonish-github.md"

To support the assessment of projects in adherence to these principles, the team
of proactive programming experts will leverage several software platforms and
tools. All learners will complete all of their work through an industry-standard
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
Actions](https://github.com/features/actions) that is accessible for a GitHub
repository.

A learner will receive a separate GitHub repository for each project on this
site. Each of these GitHub repositories will have a [pull
request](https://docs.github.com/en/github/collaborating-with-pull-requests)
called "Feedback" through which a learner will receive feedback from the team of
proactive programming experts who will assess their work. Moreover, each
[assignment type](assignment-types.md) has its own assessment strategy!

--8<-- "includes/admonitions/admonish-external.md"

## Engineering Efforts

Leveraging the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a learner receives on an engineering effort will be based on
whether or not it meets the standards for technical work in the field of
computer science. Instead of receiving a single numerical or letter grade for
this assignment, the grade for an engineering effort will have these parts:

- **Percentage of Correct GatorGrader Checks Ranging Between 0 and 100**: The
  submitted program source code must pass all of GatorGrader's checks by, for
  instance, ensuring that it produces the correct output and has all of the
  required characteristics. The technical writing must pass all of GatorGrader's
  checks about, for instance, its use of the required Markdown language features
  for technical writing. For this component of the grade for an engineering
  effort, the project will receive a percentage, ranging from 0 to 100, that
  corresponds to the percentage of GatorGrader checks that automatically pass
  inside of a GitHub Actions build.

- **Technical Writing Mastery of Either :fontawesome-solid-check: or
  :fontawesome-solid-times:**: The responses to the technical writing questions
  will receive a checkmark when they reveal a mastery of technical writing
  skills. To receive a checkmark grade, the submitted writing should have
  correct spelling, grammar, punctuation, and formatting in addition to
  following the rules of the Markdown language. The technical writing will
  receive a checkmark grade if the build report from GitHub Actions reveals no
  detected mistakes in the technical writing.

- **GitHub Actions Build Status of Either :fontawesome-solid-check: or
  :fontawesome-solid-times::** Since additional checks on the program source
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
  effort will also receive a checkmark grade when the contents of the GitHub
  repository reveals the mastery of the technical knowledge and skills developed
  during the completion of the project. As a part of this assessment, the
  assessment team will evaluate aspects of the project including, but not
  limited to, the demonstration of the mastery of the specific
  [technical](../../proactive-skills/technical-skills/introduction-technical-skills/)
  and
  [professional](../../proactive-skills/professional-skills/introduction-professional-skills/)
  skills associated with proactive programming and the accuracy of the responses
  to the technical writing questions.

## Programming Projects

Again leveraging the principles of [specification-based
grading](https://www.amazon.com/Specifications-Grading-Restoring-Motivating-Students/dp/1620362422),
the grade that a learner receives on a programming project will be based on
whether or not it meets the standards for technical work in the field of
computer science as evidenced by:

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
whether or not it meets the standards for technical work in the field of
computer science as evidenced by:

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
on your work, please send it to him by a Discord direct message at least 24
hours in advance of the project's due date. After the instructor responds to the
issue in GitHub, please resolve all of the stated concerns and participate in
the discussion until the project meets its specification and the issue is
closed.

## Assessment Delivery

The instructor invites learners to incrementally complete all of the learning
objectives for an engineering effort, programming project, and source code
survey. As long as a learner's work passes all of the GatorGrader checks before
an assignment's deadline, they will receive full credit for that part of an
assignment's assessment. After the deadline for project submission, all
assessments for a project will be reported through a learner's GitHub repository
using messages in the GitHub repository's commit log, issues raised in the issue
tracker, and comments on the "Feedback" pull request in the GitHub repository.

## Assignment Discussion

Learners who wish to receive feedback on their work for any assessed assignment
should ask questions in the same region of Github where the instructor shared
the assignment's final assessment. For example, if the instructor shares the
grade in a pull request in the repository for an engineering effort, then you
should ask questions about your grade in that pull request, bearing in mind the
need to @-mention the instructor in the body of your comment. Learners can
continue to discuss the graded assignment with the instructor until they
understand all the technical topics developed as part of the project.

--8<-- "includes/admonitions/admonish-feedback.md"

## Grade Calculation

The instructor will convert the specification-based grades that a learner
received to a numerical grade for each type of assignment. The following example
illustrates the calculation of a grade under the simplifying assumption that
there are three of each type of assignment with the grade(s) given next to the
name of the assignment:

### Engineering Efforts

- Assignment One: 100%, :fontawesome-solid-check:, :fontawesome-solid-check:, :fontawesome-solid-times:
- Assignment Two: 81%, :fontawesome-solid-times:, :fontawesome-solid-check:, :fontawesome-solid-times:
- Assignment Three: 95%, :fontawesome-solid-times:, :fontawesome-solid-check:, :fontawesome-solid-check:

**Calculation Example**

- Assignment One:

  ```
  (100 + ((1+1+0)/3)*100)/200
          0.833
  ```

- Assignment Two:

  ```
  (81 + ((0+1+0)/3)*100)/200
         0.572
  ```

- Assignment Three:

  ```
  (95 + ((0+1+1)/3)*100)/200
         0.808
  ```

- Overall:

  ```
  (0.833 + 0.572 + 0.808) / 3 * 100
          73.767
  ```

### Programming Projects

- Assignment One: :fontawesome-solid-check:
- Assignment Two: :fontawesome-solid-times:
- Assignment Three: :fontawesome-solid-times:

**Calculation Example**

- Overall:

  ```
  (1+0+0)/3 * 100
        33.33
  ```

### Source Code Survey

- Assignment One: :fontawesome-solid-check:
- Assignment Two: :fontawesome-solid-check:
- Assignment Three: :fontawesome-solid-check:

**Calculation Example**

- Overall:

  ```
  (1+1+1)/3 * 100
        100.00
  ```

## Grade Questions

Before asking the instructor a question about the calculation of either your
assignment grades or your overall course grade, please make sure that you have
already consulted the GitHub repository for each assignment to see your grades
and then calculated your grade using the approach outlined in this document. The
instructor will use your calculations to support the discussion of any questions
that you have about how to calculate either your grade for a project or your
overall grade for a course.

## Conclusion

Unsure about how the instructor will assess your work? Unconvinced that this is
a good approach to project assessment? If you have some ideas for improving the
assessment strategy please share them in the [GitHub Issue
Tracker](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/issues)
or the [GitHub Discussions
Forum](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/discussions)!

[^1]: Check out the article [Finding Common Ground with Grading
  Systems](https://rtalbert.org/finding-common-ground-with-grading-systems/)
  that [Robert Talbert](https://rtalbert.org/) wrote to explain the principles
  of effective grading. From your perspective as an emerging proactive
  programmer who wants to grow in their knowledge and skills, what are the best
  steps for an expert to take when assessing your work?
