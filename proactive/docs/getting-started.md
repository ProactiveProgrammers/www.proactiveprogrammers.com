# Getting Started

Tada is a tool that systematically runs
a doubling experiment to ascertain the likely worst-case order-of-growth function
for an arbitrary Python function.

## Install Tada

- Operating system: Linux · macOS/OS X · Windows
- Python version: Python 3.6+
- Dependency Management: [Pipenv](https://github.com/pypa/pipenv) · [Poetry](https://github.com/python-poetry/poetry)

### Install Tada with [pip](https://pip.pypa.io/en/stable/)

<div class="termy">

```console
$ pip install tada-predict
---> 100%
Successfully installed tada-predict
```

</div>

### Install through Github Repo

Alternatively, you can also install Tada manually by cloning the repository and
installing the dependencies through either [Pipenv](https://github.com/pypa/pipenv)
or [Poetry](https://github.com/python-poetry/poetry). This is also the common
way if you want to make changes to the code base.

#### Clone the Github Repository

First, you can clone this repository with the following command:

<div class="termy">

```console
$ git clone git@github.com:Tada-Project/tada.git
---> 100%
Successfully cloned tada
```

</div>

#### Install Dependencies

You can install dependencies through either `poetry` or `pipenv` with Tada; you
would first need to install either of these dependency management tool on your
local machine and then install the dependencies like the following:

=== "Poetry"

    <div class="termy">

    ```console
    $ pip install poetry
    ---> 100%
    Successfully installed poetry
    $ poetry install --no-dev
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
    $ pipenv install
    ---> 100%
    Successfully installed dependencies from Pipfile.lock
    ```

    </div>

You can activate the shell with one of the following commands:

=== "Poetry"

    ```shell
    poetry shell
    ```

=== "Pipenv"

    ```shell
    pipenv shell
    ```

## Use Tada

### Run Command

To run Tada, you can just type the following command with the arguments into the
terminal window within your preferred virtual environment:

```shell
tada [-h] --directory DIRECTORY \
          --module MODULE --function FUNCTION \
          --types TYPES [TYPES ...]
```

You can learn about Tada's checks and defaults by typing `tada -h` in your
terminal window and then reviewing the following output.

<div class="termy">

```console
usage: tada [-h] --directory DIRECTORY [DIRECTORY ...]
            --module [MODULE [MODULE ...]
            --function FUNCTION [FUNCTION ...]
            --types TYPES [TYPES ...]
            [--data_directory DATA_DIRECTORY]
            [--data_module DATA_MODULE]
            [--data_function DATA_FUNCTION] [--schema SCHEMA]
            [--startsize STARTSIZE] [--steps STEPS]
            [--runningtime RUNNINGTIME] [--expect EXPECT]
            [--backfill] [--indicator INDICATOR]
            [--maxsize MAXSIZE] [--sorted] [--log] [--md]
            [--contrast] [--level LEVEL]
            [--position] POSITION [POSITION ...]]

optional arguments:
  -h, --help
        show this help message and exit
  --directory DIRECTORY [DIRECTORY ...]
        Path to the package directory with functions to
        analyze (default: None)
  --module MODULE [MODULE ...]
        Module name with functions to analyze (default: None)
  --function FUNCTION [FUNCTION ...]
        Name of the function to analyze (default: None)
  --types TYPES [TYPES ...]
        Data generation type: hypothesis or parameter types
        of the function (default: None)
  --data_directory DATA_DIRECTORY
        Path to the package directory with function to
        generate data (default: None)
  --data_module DATA_MODULE
        Module name with functions to generate data
        (default: None)
  --data_function DATA_FUNCTION
        Name of the data generation function (default: None)
  --schema SCHEMA
        The path to the JSON schema that describes the data
        format (default: None)
  --startsize STARTSIZE
        Starting size of the doubling experiment (default: 1)
  --steps STEPS
        Maximum rounds of the doubling experiment
        (default: 10)
  --runningtime RUNNINGTIME
        Maximum running time of the doubling experiment
        (default: 200)
  --expect EXPECT
        Expected Growth Ratio: O(1) | O(logn) | O(n) |
        O(nlogn) | O(n^2) | O(n^3) | O(c^n). By using this
        argument, the experiment result will be stored in a
        csv file (default: None)
  --backfill
        Enable backfill to shrink experiments size according
        to the Predicted True Value (default: False)
  --indicator INDICATOR
        Indicator value (default: 0.1)
  --maxsize MAXSIZE
        Maximum size of the doubling experiment
        (default: 1500)
  --sorted
        Enable input data to be sorted (default: False)
  --log
        Show log/debug/diagnostic output (default: False)
  --md
        Show results table in markdown format (default: False)
  --contrast
        Show contrast result table. Only works with multiple
        experiments (default: False)
  --viz
        Visualize a simple graph for the result
        (default: False)
  --level LEVEL
        The level of nested data structure to apply doubling
        experiment (default: 1)
  --position POSITION [POSITION ...]
        The position of input data to double in the
        multivariable doubling experiment. Must be the last
        argument (default: [0])

Sample usage:
  tada --directory /path/to/project_directory --module
  module_name.file_name --function function_name
  --types hypothesis
```

</div>

#### Running within Tada Repo

If you are running within the Tada repository, then you could also easily run
Tada with the dependency management tool (or within the activated shell) you
previously installed like this:

=== "Poetry"

    ```shell
    poetry run python tada/tada_a_bigoh.py [-h] --directory DIRECTORY \
          --module MODULE --function FUNCTION \
          --types TYPES [TYPES ...]
    ```

=== "Pipenv"

    ```shell
    pipenv run python tada/tada_a_bigoh.py [-h] --directory DIRECTORY \
          --module MODULE --function FUNCTION \
          --types TYPES [TYPES ...]
    ```

=== "Within Shell"

    ```shell
    python tada/tada_a_bigoh.py [-h] --directory DIRECTORY \
          --module MODULE --function FUNCTION \
          --types TYPES [TYPES ...]
    ```

It is worth noting that when the provided experiment function is relied on an
external Python library, it is likely that Tada might not have this dependency,
and thus, it might cause an error when running the experiment. You can simply
resolve this issue by installing the required dependencies through your chosen
dependency management tool like this:

=== "Poetry"

    ```shell
    poetry add <library-name>
    ```

=== "Pipenv"

    ```shell
    pipenv install <library-name>
    ```

### Quick Start Example

We have provided some code examples in [Speed-Surprises](https://github.com/Tada-Project/speed-surprises)
for you to run Tada in conjunction and experience how Tada automatically suggests
the likely worst-case order-of-growth function for various types of Python function.
You can follow the instructions in [Speed-Surprises](https://github.com/Tada-Project/speed-surprises)
to clone the repository and install the dependencies.

After successfully setting up the repository on your local machine, you can
then run the following command to conduct an experiment for `insertion_sort`
within the `speed-surprises` repository:

```shell
tada --directory . --module speedsurprises.lists.sorting \
     --function insertion_sort --types hypothesis \
     --schema speedsurprises/jsonschema/single_int_list.json
```

Within a minute or so, you will be able to inspect an output similar to the
following with a results table provided at the end of the experiment.

<div class="termy">

```console
$ tada --directory . --module speedsurprises.lists.sorting --function insertion_sort --types hypothesis --schema speedsurprises/jsonschema/single_int_list.json

        Tada!: auTomAtic orDer-of-growth Analysis!
          https://github.com/Tada-Project/tada/
      For Help Information Type: python tada_a_bigoh.py -h

Start running experiment insertion_sort for size 1 →


→ Done running experiment insertion_sort for size 1
.
.
.
→ Done running experiment insertion_sort for size 64
```

</div>

```
+-----------------------------------------------------------------------------+
|             insertion_sort: O(n) linear or O(nlogn) linearithmic            |
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  1   | 4.882118635177613e-07  | 4.6806960487365676e-07 |         0          |
|  2   | 7.456634746551513e-07  | 7.133920059204101e-07  | 1.527335835885569  |
|  4   |  9.27755012257894e-07  | 9.209306488037112e-07  | 1.2442006934655812 |
|  8   | 1.3545460286458332e-06 | 1.3353490028381343e-06 | 1.4600255571233727 |
|  16  | 2.2379635269165037e-06 | 2.2146971740722657e-06 | 1.6521871384125948 |
|  32  | 3.9610248652140306e-06 | 3.913619827270508e-06  | 1.7699237800678478 |
|  64  | 7.2769234293619794e-06 | 7.211799896240237e-06  | 1.837131468996415  |
+------+------------------------+------------------------+--------------------+
O(n) linear or O(nlogn) linearithmic
```

### Features

Tada provides more features and customization on argument parameters for you
to choose. The tool adopts `Hypothesis` and `Hypothesis-jsonschema` to generate
random data for your provided Python function, so that you can easily conduct
a doubling experiment with a dynamic range of data by simply providing a JSON
schema that describes the type and constraints of your function arguments.
Besides, Tada also has a set of built-in data generation functions that would
support most primary types. You can even write your own customized data
generation function for more specific constraints the function might expect. You
can also fine-tune your experiment through the aforementioned CLI arguments from
starting size of the experiment `--startsize` to `--position` that determines which
parameter(s) to double within your function. You can also make use of our
`--backfill` and `--indicator` checks to accelerate your experiment process. Please
be sure to check out [Using Tada](https://tada-predict.netlify.app/using-tada/)
to find out more details about these features.

## Test

Tada comes with an extensive test suite. In order to run the tests, you will
need to clone the git repository and set up the development environment for Tada
using either `pipenv` or `poetry`

See [Test Tada](http://tada-predict.netlify.app/contributing/#test-tada) for
more details and information.
