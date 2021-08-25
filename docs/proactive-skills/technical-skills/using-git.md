# Using GitHub

Git is a version control system that enables a proactive programmer to
incrementally document and save their work on a project.

The projects on this site expect you to use a program to securely communicate
the GitHub servers that will host all of the project templates and your
submitted deliverables. In this assignment, you will perform all of the steps to
configure your account on GitHub and you will start your first assignment using
GitHub Classroom. As you will be required to use Git, an industry standard tool,
in all of the remaining laboratory and practical assignments and during the
class sessions, you should keep a record of all of the steps that you complete
and the challenges that you face. You may chat with the course instructor or one
of the technical leaders if you are not able to complete a certain step or if
you are not sure how to proceed.

- If you do not already have a GitHub account, then please go to the GitHub web
  site and create one, making sure that you use your `allegheny.edu` email
  address so that you can join GitHub as a student at an accredited educational
  institution. You are also encouraged to sign up for GitHub's "Student
  Developer Pack" at [Student Developer
  Pack](https://education.github.com/pack), qualifying you to receive free
  software development tools. Additionally, please add a description of yourself
  and an appropriate professional photograph to your GitHub profile. Unless your
  username is taken, you should also pick your GitHub username to be the same as
  Allegheny's Google-based email account. Now, in the `#labs` channel of our
  Slack workspace, please type on one line your full name, `allegheny.edu` email
  address, and your new GitHub username.

- If you have never done so before, you must use the `ssh-keygen` program to
  create secure-shell keys that you can use to support your communication with
  GitHub. But, to start, this task requires you to type commands in a program
  that is known as a terminal. Your terminal program will vary depending on your
  operating system. For instance, if you are running Linux, you can click on an
  icon that contains the `>` symbol or press the "Super" key, start typing the
  word "terminal", and then select that program. Another way to open a terminal
  involves typing the key combination `<Ctrl>-<Alt>-t`. On the Windows operating
  system you may want to use the "Command Prompt" or the "Power Shell" and on
  MacOS you can use "Terminal". Your terminal will display as a box into which
  you can type commands. For the next step, you may need to separately install
  `ssh-keygen` if it is not on your laptop.

- Now that you have started the terminal, you will need to type the `ssh-keygen`
  command in it. Follow the prompts to create your keys and save them in the
  default directory. That is, you should press "Enter" after you are prompted to
  "`Enter file in which to save the key ...  :`" and then type your selected
  passphrase whenever you are prompted to do so. Please note that a "passphrase"
  is like a password that you will type when you need to prove your identify to
  GitHub. What files does "`ssh-keygen`" produce? Where does this program store
  these files by default? Do you have any questions about how to create your SSH
  keys?

- Once you have created your ssh keys, you need to upload them to GitHub. First,
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

- Again, when you are completing these steps, please make sure that you take
  careful notes about the inputs, outputs, and behavior of each command. If
  there is something that you do not understand, then please ask the course
  instructor or the technical leader about it.

