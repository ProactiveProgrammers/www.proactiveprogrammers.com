# Using Docker

[//]: # (Stress difficulties, encourage not to upgrade once working)

## Introduction

Docker Desktop and Docker Engine make it possible for a proactive programmer to
download a Docker container that contains all of the software that they need to
complete a programming project. This means that, instead of having to separately
download all of the dependencies for a project, you can download a single Docker
container that contains all of them! Exciting, right? While it is exciting,
there is a challenge as well: Docker Desktop is often difficult to download,
install, and configure on Windows 10 Pro, Windows 10 Enterprise, and MacOS. Once
you have Docker working correctly for all of the Docker contains that the
projects on this site invite you to use, it is best for you to defer any
upgrades to Docker Desktop until you are not facing time-sensitive deadlines.
Before you ensure that your computer meets the requirements for using either
Docker Desktop or Docker Engine, you might want to read the [Docker
Overview](https://docs.docker.com/get-started/overview/).

## Requirements Check

If you are a student at Allegheny College, you must complete your course
projects using a [Department Approved
Laptop](https://www.cs.allegheny.edu/resources/laptops/). This is primarily due
to the fact that your laptop must be approved for running [Docker
Desktop](https://www.docker.com/products/docker-desktop) on MacOS and Windows
and [Docker Engine](https://docs.docker.com/engine/install/ubuntu/) on Linux. If
you are not sure whether or not your computer supports Docker, you can visit the
[Can I Run Docker?](https://www.cs.allegheny.edu/canirundocker/) web site and
the see if Docker will work correctly on it. Of course, if you are not enrolled
at Allegheny College, you also welcome to use Docker to complete and check the
projects on this site! With that said, it is worthwhile to visit the following
web sites and review the requirements for using Docker before you install it.

* [Supported Platforms for Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/#prerequisites)
* [System Requirements for Docker Desktop on MacOS](https://docs.docker.com/desktop/mac/install/#system-requirements)
* [System Requirements for Docker Desktop on Windows](https://docs.docker.com/desktop/windows/install/#system-requirements)

If you don't see your operating system mentioned in the above list, then you
should pick the one that is the closest to what operating system is running on
your computer. For instance, if you run a different type of Linux than Ubuntu,
you should follow, as appropriate, the Ubuntu-based instructions while also
searching for other tutorials that are customized for your specific operating
system. Finally, don't forget that if you use MacOS you need to follow different
instructions depending on whether your computer has an Intel-based or Apple
Silicon-based central processing unit!

## Installing Docker

Docker's web site provides customized instructions for installing Docker! After
carefully reading the steps on the site that mentions your operating system,
take the suggested steps to install and configure Docker on your computer:

* [Install Docker Engine on Linux](https://docs.docker.com/engine/install/)
* [Install Docker Desktop on MacOS](https://docs.docker.com/desktop/mac/install/)
* [Install Docker Desktop on Windows](https://docs.docker.com/desktop/windows/install/)

If your computer runs Windows 10 Home you can only install Docker Desktop if you
have also installed the Windows Subsystem for Linux (WSL) version 2 backend. If
your Windows 10 Home operating system cannot run WSL 2, then you must upgrade
your operating system to either Windows 10 Pro, Windows 10 Enterprise, or
Windows 10 Education. Finally, you should not use Docker Toolbox since it is
deprecated and no longer supported!

## Using Docker

Once you have successfully installed and configured Docker on your computer, you
are ready to confirm that it is working correctly! Depending on your operating
system, you may have a "tray icon" in the shape of a whale: you can click on
this icon and access the settings and menus for Docker. It is also possible for
you to type `docker --version` in your terminal window to discover what version
of Docker you are using. Next, you should complete steps 4 through 6 in [Brian
Hogan](https://bphogan.com/)'s Docker tutorial called [How to Install and Use
Docker on Ubuntu
20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).
Even though parts of this tutorial are customized to using Docker on Ubuntu
Linux, the aforementioned steps will help you learn how to download and use
Docker containers in your terminal window! Here is a summary of the steps:

* Step 4: Working with Docker Images
* Step 5: Running a Docker Container
* Step 6: Managing Docker Containers
