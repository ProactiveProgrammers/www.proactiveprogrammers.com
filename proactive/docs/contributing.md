# Contributing Tada

If you would like to participate in the development of Tada, the project maintainers
suggest the use of `Pyenv` to install the latest release of Python 3.6 and/or
Python 3.7. You would also need to install [Git](https://git-scm.com/) if you
have not done so already in order to access the project's Github repository.

The maintainers for Tada use the
[GitHub Flow Model](https://guides.github.com/introduction/flow/) to guide our
engineering of this tool and we invite you to also follow it as you make a
contribution.

## Clone the Github Repository

If you have not cloned the repository yet, you can type in the following
command to clone Tada's Github repository:

<div class="termy">

```console
$ git clone git@github.com:Tada-Project/tada.git
---> 100%
Successfully cloned tada
```

</div>

If you are already a collaborator on the project and would like to contribute
a new feature or bug fix, you should create and publish your new branch via
the following command. Substitute the name of your feature/branch for the
word `feature-name`.

- `git checkout -b feature-name`
- `git checkout master`
- `git push -u origin feature-name`

If you are not yet a collaborator on this project, then we recommend you to first
fork the repository, add your new feature, document and test it as appropriate.

## Install Development Dependencies

You can install dependencies through either `poetry` or `pipenv` with Tada, but
you would first need to install either of these dependency management tool on your
local machine and then install the development dependencies.

Although Tada currently supports both `pipenv` and `poetry`, we recommend you to
use `poetry` as we are also migrating to use `poetry` instead of `pipenv`.

=== "Poetry"

    <div class="termy">

    ```console
    $ pip install poetry
    ---> 100%
    Successfully installed poetry
    $ poetry install
    ---> 100%
    Successfully installed tada-predict and dependencies from lock file
    ```

    </div>

=== "Pipenv"

    <div class="termy">

    ```console
    $ pip install pipenv
    ---> 100%
    Successfully installed pipenv
    $ pipenv install --dev
    ---> 100%
    Successfully installed dependencies from Pipfile.lock
    ```

    </div>

You can activate the shell with one of the following command:

=== "Poetry"

    ```shell
    poetry shell
    ```

=== "Pipenv"

    ```shell
    pipenv shell
    ```

## Make a Pull Request

Finally, you should open a pull request on the GitHub repository for the new
changes that you have created. This pull request should describe the new feature
or bug fix that you are adding and give examples of how to run it on the
command line.

We highly recommend you to provide tests along with the feature that you
implemented and you should not break the existing test cases or features.

## Test Tada

The developers use [Pytest](https://docs.pytest.org/en/latest/) for testing Tada.
To run the provided test suite for Tada's functions within the shell, you can type
the following in your terminal window:

=== "Poetry"

    ```shell
    poetry run pytest tests
    ```

=== "Pipenv"

    ```shell
    pipenv run pytest tests
    ```

The maintainers use statement and branch coverage to inform their testing
activities. Please make sure you maintain or raise the current test coverage when
developing new features. If you want to check the coverage of the test suite
locally, then you can run:

=== "Poetry"

    ```shell
    poetry run pytest --cov-config pytest.cov --cov
    ```

=== "Pipenv"

    ```shell
    pipenv run pytest --cov-config pytest.cov --covs
    ```

If you want to collect the coverage of the test suite and see what lines of code
are not covered, then you can run:

=== "Poetry"

    ```shell
    poetry run pytest --cov-config pytest.cov --cov --cov-report term-missing
    ```

=== "Pipenv"

    ```shell
    pipenv run pytest --cov-config pytest.cov --cov --cov-report term-missing
    ```

## Code linting and Continuous Integration

When making contributions to the project, please make sure that you adhere to the
coding standard that are enforced by automated linting tools such as
[Pylint](https://github.com/PyCQA/pylint) and
[Flake8](https://flake8.pycqa.org/en/latest/). The project uses both Travis CI
and Github Action to build and test the tool in Ubuntu, MacOS, and Windows system
with Python versions of 3.6, 3.7, and 3.8. Following are some of the linting
checks being checked in Travis CI and Github Action platform. You can also run these
checks locally to see if you have conformed to the coding standard.

=== "Poetry"

    ```shell
    poetry run flake8 tada
    poetry run flake8 tests
    poetry run pylint tada
    poetry run pylint tests
    ```

=== "Pipenv"

    ```shell
    pipenv run flake8 tada
    pipenv run flake8 tests
    pipenv run pylint tada
    pipenv run pylint tests
    ```

## Develop Docs

The documentation uses [MkDocs](https://www.mkdocs.org) and the theme
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

MkDocs comes with a built-in dev-server that lets users preview documentation as
they work on it. When developing, make sure you are in the same directory as
the `mkdocs.yml` configuration file (the root directory), and then start the
server by running the `mkdocs serve` command. You will be able to preview the
doc site at `http://127.0.0.1:8000`.

=== "Poetry"

    <div class="termy">

    ```console
    $ poetry run mkdocs serve
    INFO    -  Building documentation...
    INFO    -  Cleaning site directory
    INFO    -  Documentation built in 0.65 seconds
    INFO    -  Serving on http://127.0.0.1:8000
    ```

    </div>

=== "Pipenv"

    <div class="termy">

    ```console
    $ pipenv run mkdocs serve
    INFO    -  Building documentation...
    INFO    -  Cleaning site directory
    INFO    -  Documentation built in 0.65 seconds
    INFO    -  Serving on http://127.0.0.1:8000
    ```

    </div>

## Publish a Release

Tada uses `poetry` and [Github Action](https://github.com/features/actions)
workflow to automate the process of publishing package to
[PyPI](https://pypi.org). The PyPI publish will be made automatically when a
github release is published through a commit that is associated with a
[Git Tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging). All release numbers
in this repository should adhere to the [Semantic Versioning](http://semver.org/)
standard that all GitHub projects are asked to adopt.

In order to make a github release, you should commit your file using a
`git commit` command as followed where the version number should be changed
accordingly:

```shell
git tag 1.0.0
```

The version of the PyPI package will also be automatically set as the tag
version. At this point, you are ready to push the changes with the appropriate
tag by typing the following command:

```shell
git push origin HEAD --tags
```

After waiting for a period of time, a new release of the project will be created
on the Github repository page if all the test cases and linting checks have passed.
Once the Github release has been created successfully, Github Action wil then
publish the latest release to PyPI.
