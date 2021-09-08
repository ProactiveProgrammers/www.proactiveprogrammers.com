# Software Tools

## Project Goals

This engineering effort invites you to combine what you learned about the basics
of Python programming to implement a useful program that can search for a word
in a file. Leveraging all your [technical
skills](/proactive-skills/introduction-proactive-skills/), you will use programs
such as VS Code and a terminal window and the Python programming language and
the Poetry package manager.

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

This project invites you to implement a file searching program called `search`.
The `search` program takes as input a word (e.g., "proactive") and determines
whether or not it is in the text of a file provided on the input. For instance,
if the file called `input/proactive.txt` contains inside of the text on the main
page of this web site, then searching for the word `proactive` with the
command `poetry run search --word ethical --dir input --file proactive.txt`
yields:

```shell
😃 Searching through the file called input/proactive.txt!

Was the word "ethical" found in the file input/proactive.txt? Yes
```

When you search for a word that does not appear inside of the input file with a
command like `poetry run search --word conundrum --dir input --file
proactive.txt` then the program will produce the following output:

```shell
😃 Searching through the file called input/proactive.txt!

Was the word "conundrum" found in the file input/proactive.txt? No
```

Once your program is working correctly, you should also try to use if and
specify a file that is not available on your computer! For instance, if you run
it with the command `poetry run search --word proactive --dir input --file
notfound.txta` then it will not perform a search and instead produce the
following output:

```shell
😃 Searching through the file called input/notfound.txt!

🤷 input/notfound.txt was not a valid file
```

???+ note

    Don't forget that if you want to run the `search` program you must use your
    terminal window to first go into the GitHub repository containing this
    project and then go into the `search` directory that contains the project's
    source code. Finally, remember that before running the program you must run
    `poetry install` to add the dependencies.

## Adding Functionality

If you study the file `search/search/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `search` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```
================================== ERRORS ==================================
__________________ ERROR collecting tests/test_search.py ___________________
tests/test_search.py:5: in <module>
    from search import main
search/main.py:31: in <module>
    ???
E   NameError: name 'cli' is not defined
========================= short test summary info ==========================
ERROR tests/test_search.py - NameError: name 'cli' is not defined
!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!
============================= 1 error in 0.11s =============================
```

Alternatively, running the program with a command like `poetry run search --word
ethical --dir input --file proactive.txt` will produce the following output:

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/gkapfham/.pyenv/versions/3.9.2/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 790, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  [...]
    @cli.command()
NameError: name 'cli' is not defined
```

This output suggests that the `cli` variable was not correctly declared! After
declaring the `cli` variable in the appropriate fashion, following the relevant
instructions in the description of the [technical
skills](/proactive-skills/introduction-proactive-skills/), you should find the
other `TODO` markers and correctly resolve them. For instance, you can add this
function to the `main.py` file:

```python
def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False
```

In addition to `confirm_valid_file`, you must completely implement these
functions:

- `def human_readable_boolean(answer: bool) -> str`
- `def word_search(text: str, word: str) -> bool`
- `def word(word: str = typer.Option(None), dir: Path = typer.Option(None), file: Path = typer.Option(None)) -> None`
