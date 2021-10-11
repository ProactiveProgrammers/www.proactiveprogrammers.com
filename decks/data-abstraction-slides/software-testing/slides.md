---
# try also 'default' to start simple
theme: default
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: prism
colorSchema: light
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
---

[//]: # (Slide Start {{{)

# Data Abstraction

## Software Testing

<div class="container my-5">
  &nbsp;
</div>

### Gregory M. Kapfhammer

### www.proactiveprogrammers.com

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# <em>Okay</em>, what is this about?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-4;
  }
</style>

<div v-click>

## Key Question

> How can I use the processes of software testing and debugging to establish a
> confidence in the correctness of a Python program?

</div>

<br>

<div v-click>

## Learning Objectives

> To **remember** and **understand** the principles of software testing and
> debugging so as to implement test suites, using Pytest, for programs that find
> bugs and establish a confidence in correctness.


</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-5xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's explore the practice of software testing!
</div>

</div>

</div>


[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are foundations of testing and debugging?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Testing: run a program to try to see if it works
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Debugging: fix a program that is currently broken
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Design for testability ensures testing is possible
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Software Testing in Python

<v-clicks>

-   Python program must be in an **executable state**!

-   Python source code must be **free** of **syntactical errors**

-   Python source code must be **free** of **static semantic errors**

- Key insights about software testing in Python:

    - Purpose of testing is to show that **bugs exists**

    - Testing **cannot prove** the **absence of defects**

    - **Exhaustive testing** of trivial functions is **not possible**

    - A **test suite** is a collection of useful program inputs

    - **Partition testing** divides the input space into groups

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
What are key strategies for software testing?
</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Keys: What is the focus? <em>and</em> What is the scope?
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Closed-box testing focuses on the specification
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<mdi-tooltip-check class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-10 ml-4">
Glass-box testing focuses on the source code
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Closed-Box Software Testing

<v-clicks>

-   Consider the **specification** of the program under test

-   Specifications may exist in a **variety of forms**:

    - Docstring for a function
    - Type annotations for a function
    - Informal specification for a program unit
    - Formal specification for a program unit

-   Python source code must be **free** of **static semantic errors**

- Key insights about software testing in Python:

    - Purpose of testing is to show that **bugs exists**

    - Testing **cannot prove** the **absence of defects**

    - **Exhaustive testing** of trivial functions is **not possible**

    - A **test suite** is a collection of useful program inputs

    - **Partition testing** divides the input space into groups

</v-clicks>

[//]: # (Slide End }}})

---

# Defect Detection with Pylance

```python {all|1-3|4|5-8|9-10|all}
def create_results_zip_file(
    results_dir: Path, results_files: List[str]
 ) -> None:
    """Make a .zip file of all results."""
    with zipfile.ZipFile(
        "results/All-WorkKnow-Results.zip",
        "w",
    ) as results_zip_file:
        for results_file in results_files:
            results_zip_file.write(results_files)
```

<v-click>

<mdi-message-question-outline class="text-8xl absolute top-108 left-8 text-orange-600" />
<mdi-bug class="text-8xl absolute top-105 left-34 text-orange-600" />

</v-click>

<!--

One of WorkKnow's features is that it can create a ZIP file of all the results
that it saves about the history of GitHub Action workflows for different
projects. This feature has come in handy when the data that it downloads is too
large to send to someone on a per-file basis.

When I first wrote this function, I did so in the way that you see right now.
That leads me to my next question:

- Can you find the bug in this program?

Thankfully, Pyright can find it for us!

**CUT IN SHORT VERSION**

After walking through the source code for this function, I have a story to tell
you about how type annotations helped me to implement it correctly!

**Explain each line of source code in the function.**

Although I acknowledge that the defect is a small one and that, in fact, I would
have been able to find it without using type annotations and type checkers, I'm
delighted to report that pyright found it for me immediately! I appreciate
pyright because it works asynchronously in the background, pointing out likely problems
while I focus on the next feature or test that I want to write.

-->

---

<v-click>

## Pyright Feedback in VS Code

<style>
  h2 {
    font-size: 42px;
    @apply text-orange-600 mb-4;
  }
  li {
    font-size: 28px;
    margin-top: 4px;
    margin-bottom: 9px;
    }
  pre {
    @apply text-3xl
  }
</style>

<div class="border-3 rounded-2xl border-gray-700 bg-true-gray-300 p-5 mb-6">

<pre>
Argument of type "List[str]" cannot be
assigned to parameter "filename" of
type "StrPath" in function "write"
</pre>

</div>

</v-click>

<v-click>

```python
with zipfile.ZipFile(
    "results/All-WorkKnow-Results.zip",
    "w",
) as results_zip_file:
    for results_file in results_files:
        results_zip_file.write(results_files)
```

</v-click>

<v-click>

<mdi-bug class="text-8xl absolute top-99 left-215 text-orange-600" />

</v-click>

<v-click>

<mdi-arrow-up class="text-6xl absolute top-118 left-175 text-orange-600" />

</v-click>

<v-click >

<div class="text-8xl ml-100 mt-5">

<code>results_file</code>

</div>

</v-click>

<!--

Let's take a look at the error message that Pyright shared with me!

**Read the error message.**

As soon as I read this message I realized that I need to focus on the call to
the write function and the parameter that I passed to it. After contemplating
Pyright's error again, I realized that I had made a mistake by passing
results_files, a list containing strings, instead of results_file, the specific
file, to the write function.

Yep, one extra s would have caused a major problem when I either ran the test
suite or the program itself! Of course, it is reasonable to ask whether or not I
would have found this bug by other means. Yes, I think that I would have! But,
it was nice to find it so quickly through the use of type annotations and the
Pyright type checker.

-->

---


---

[//]: # (Slide Start {{{)

# Investigating Software Testing

<div class = "mt-10">
</div>

<v-clicks>

-   Correct use of program components in Python programs:

    -   **Q1**: What are the benefits of **recursive** functions?

    -   **Q2**: What are the different ways to implement **Fibonacci**?

    -   **Q3**: What are the **trade-offs** of function choices?

    -   **Q4**: What the benefits of using program **modules**?

    -   **Q5**: How to external **packages** aid Python programmers?

-   Balance the **trade-offs** associated with different functions!

-   Judiciously use **external** program modules when programming

</v-clicks>

[//]: # (Slide End }}})
