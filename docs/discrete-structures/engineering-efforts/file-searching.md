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
    source code.
