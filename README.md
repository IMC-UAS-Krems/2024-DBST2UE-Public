# Public repository for DBST2UE 2024

## Session 4 - 03/04/2024

#### Task 1 - Setup Fixtures and write tests

Complete the tasks 2 and 3 from the past session (see [session.03/README.md](session.03/README.md)).

#### Task 2 - 

## Log of Past Sessions

### Session 1 - 06/03/2024

We started the setup of students environment to get ready for the assignment and the exercises in class.

We configured PowerShell/Shell, created an ssh key (in the default location), registered the ssh key into GitHub. 

We checked the installation of `git` and `python`. For the moment we do not enforce any specific version of python.

We accepted the Classroom assignment for DBST2UE and added this repository as git submodule under the name `public`. We committed the changes and pushed back, checked on GitHub that the public folder is actually a link to another repository (e.g., this repository at the time we add the submodule).

We created a python virtual environment called `.venv` in the student repository (besides the `public` folder). Activated the virtual environment, updated `pip`, and installed testing dependencies including `pytest`, `pytest-cov`, and `pytest-mock`. 

Finally, we smoke-tested `pytest` by running it at the root of the probject.

The student repository at this point MUST look like this:

```
.
├── .git
├── .github
├── .gitmodules
├── .venv
├── README.md
└── public
    ├── .git
    ├── .gitignore
    └── README.md
```



### Session 2 - 13/03/2024

We finished to setup the python project, including importing the right submodule, installing pytest, pytest-cov, etc in the virtualenv `.venv`

Dr. Gambi illustrated how to configure and invoke the `pytest-cov` plugin, filter out empty files, test files, and all the files that do not belong to the project. We also included the `__init__.py` files that identify python modules.

We postponed tasks 3 to 5 to Session 3

### Session 3 - 20/03/2024

We finished to install all the dependencies, such as SQLite3 and docker. 

We experimented using docker and docker compose using MariaDB container and instructions. We experimented on how to start a plain container with environmental variables, how to connect to it using `docker exec`, and how to connect to it using port forwarding

We introduced to concept of test fixture, experimented with hardcoded and temporary files to illustrate the problem of state polluting tests.
