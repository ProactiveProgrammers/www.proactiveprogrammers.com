# Using GitHub

## Understanding Git

[Git](https://git-scm.com/) is a version control system that enables a proactive
programmer to incrementally document and save their work on a project. In
addition to installing Git on your computer you need to setup an account on
GitHub! Before you do so, it is worth taking some time to read a tutorial on
[Automated Version
Control](https://swcarpentry.github.io/git-novice/01-basics/index.html). After
you understand what version control is and why you should use it, you are ready
to install Git on your computer and create and configure a GitHub account! To
get started, please read [Installing
Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow
the instructions for your computer's operating system. If you want to learn more
about Git commands that you can use, make sure to read the [Git Cheatsheet from
GitHub](https://training.github.com/downloads/github-git-cheat-sheet/).

The projects on this site expect you to use [GitHub](https://github.com/) to
receive starting source code and, if you are an Allegheny College student,
submit your projects for assessment. As such, it is important for you to be able
to securely communicate with the GitHub servers! In the remainder of these steps
you will create an account on GitHub and ensure that you can securely
communicate with the GitHub servers.

- If you do not already have a GitHub account, then please go to the GitHub web
  site and create one, making sure that, if you are a student at Allegheny
  College, you use your `allegheny.edu` email address so that you can join
  GitHub as a student at an accredited educational institution. You are also
  encouraged to sign up for GitHub's "Student Developer Pack" at [Student
  Developer Pack](https://education.github.com/pack), qualifying you to receive
  free software development tools. Additionally, please add a description of
  yourself and an appropriate professional photograph to your GitHub profile.
  Unless your username is taken, you should also pick your GitHub username to be
  the same as Allegheny's Google-based email account. If you are not enrolled at
  Allegheny College, then you can create a GitHub account with any name you
  prefer.

- If you have never done so before, you must use the `ssh-keygen` program to
  create secure-shell keys that you can use to support your communication with
  GitHub. This task requires you to type commands in a program that is known as
  a terminal. Your terminal will display as a box into which you can type
  commands. If you have already installed your terminal and it runs commands
  correctly, then you may need to further install `ssh-keygen` if it is not
  already installed on your computer.

- After starting the terminal, you will need to type the `ssh-keygen` command in
  it. Follow the prompts to create your keys and save them in the default
  directory. That is, you should press ++"Enter"++ after you are prompted to
  "`Enter file in which to save the key ...  :`" and then type your selected
  passphrase whenever you are prompted to do so. Please note that a "passphrase"
  is like a password that you will type when you need to prove your identify to
  GitHub. What files does `ssh-keygen` produce? Where does this program store
  these files by default? Before moving on to the next step, take time to read
  the [About
  SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/about-ssh)
  documentation provided by GitHub.

- Once you have created your SSH keys, you need to upload them to GitHub. First,
  you must log into GitHub and look in the right corner for an account avatar
  with a down arrow. Click on this link and then select the "Settings" option.
  Now, scroll down until you find the "SSH and GPG keys" label on the left,
  click to create a "New SSH key", and then upload your ssh key to GitHub. You
  can copy your SSH key to the clipboard by going to the terminal and typing a
  command like `cat ~/.ssh/id_rsa.pub` command and then highlighting this
  output. When you are completing this step in your terminal, please make sure
  that you only highlight the letters and numbers in your key &mdash; if you
  highlight any extra symbols or spaces then this step may not work correctly.
  Then, paste this into the GitHub text field in your web browser.

- Now that your SSH keys are uploaded to GitHub you should try to clone a GitHub
  repository to your computer and confirm that the keys are working as expected.
  You might want to clone the GitHub repository that hosts the source code for
  this web site. Or, you can clone another repository on GitHub that seems
  interesting to you! If you want to clone the repository that contains the
  source code for this web site, go to
  [github/www.proactiveprogrammers.com](https://github.com/ProactiveProgrammers/www.proactiveprogrammers.com/)
  and click the green button with the "Clone" label. After following the
  instructions you should run a command like `git clone
  git@github.com:ProactiveProgrammers/www.proactiveprogrammers.com.git` in your
  terminal window. If everything worked correctly then you should see the source
  code for this site on your computer! It is also worth pointing out that the
  repository that you cloned is a public one and, once you start to clone
  private GitHub repositories, you will again need to confirm that your SSH keys
  are supporting secure communication correctly.
