# Using GatorGrader

[//]: # (Excerpted from prior docs on GatorGrader and Dockagator)

## Introduction

The projects on this web site integrate the
[GatorGrader](https://github.com/GatorEducator/gatorgrader) tool so that an
emerging proactive programmer can receive rapid feedback in either a GitHub
Actions build or in a Docker container running on their computer. Since each
project on this site overviews the checks that GatorGrader runs, the purpose of
this documentation is to explain how to run GatorGrader in a Docker container
using the [DockaGator](https://github.com/GatorEducator/dockagator) Docker image
that runs [GatorGradle](https://github.com/GatorEducator/gatorgradle) and
ultimately results in performing the checks for a specific assignment.

## Non-Interactive Shell

After installing Docker, you can use the following `docker run` command for your
operating system to start `gradle grade` as a containerized application, using
the [DockaGator](https://github.com/GatorEducator/dockagator) Docker image
available on
[DockerHub](https://cloud.docker.com/u/gatoreducator/repository/docker/gatoreducator/dockagator).

=== "Windows"

    ```bash
    docker run --rm --name dockagator \
      -v "%cd%:/project" \
      -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" \
      gatoreducator/dockagator
    ```

=== "Linux and MacOS"

    ```bash
    docker run --rm --name dockagator \
      -v "$(pwd)":/project \
      -v "$HOME/.dockagator":/root/.local/share \
      gatoreducator/dockagator
    ```
The aforementioned command will use `"$(pwd)"` (i.e., the current working
directory) as the project directory and `"$HOME/.dockagator"` as the cached
GatorGrader directory. Please note that both of these directories must exist,
although only the project directory must contain something. Generally, the
project directory should contain the source code and technical writing for an
assignment, as provided to a student by the instructor through GitHub.
Additionally, the cached directory should not contain anything other than
directories and programs created by DockaGator, thus ensuring that they are not
otherwise overwritten during the completion of the assignment.

To ensure that the previous command will work correctly, you should create the
cache directory by running the command `mkdir $HOME/.dockagator` on the MacOS
and Linux operating systems. However, if you are using the Windows operating
system then you will instead need to type the command `mkdir
%HomeDrive%%HomePath%/.dockagator`. Finally, since the above `docker run`
command does not work correctly on the Windows operating system, you will need
to instead run the following command to adapt to the differences in the `cmd`
terminal window:

```bash
docker run --rm --name dockagator \
  -v "%cd%:/project" \
  -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" \
  gatoreducator/dockagator
```

Please note that not all version of the Windows terminal window will correctly
recognize the use of the `%cd%` and `%HomeDrive%%HomePath%` variables. In this
case, you should substitute the actual directory for a specific course
assignment for the `%cd%` variable and the drive letter that contains the
`.dockagator` directory for the `%HomeDrive%%HomePath%` variable. Finally, the
Windows terminal window may not work correctly when you attempt to run a
multi-line command. In this case, you should break up the aforementioned
four-line command into separate lines, like `docker run --rm --name dockagator`
and `-v "%cd%:/project"` and then connect them into a single long line that you
separate by a single space. Here is an example of what the long command would
look like, again assuming that the Windows `cmd` terminal correctly interprets
the `%cd%` and `%HomeDrive%%HomePath%` variables:

```bash
docker run -it --rm --name dockagator -v "%cd%:/project" -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" gatoreducator/dockagator /bin/bash
```

Here are some additional commands that you may need to run when using Docker:

* `docker info`: display information about how Docker runs on your workstation
* `docker images`: show the Docker images installed on your workstation
* `docker container list`: list the active images running on your workstation
* `docker system prune`: remove many types of "dangling" components from your workstation
* `docker image prune`: remove all "dangling" docker images from your workstation
* `docker container prune`: remove all stopped docker containers from your workstation
* `docker rmi $(docker images -q) --force`: remove all docker images from your workstation

