# Public repository for DBST2UE 2024

## Session 4 - 03/04/2024

#### Task 1 - Setup Fixtures and write tests

Complete the tasks 2 and 3 from the past session (see [session.03/README.md](session.03/README.md)).

#### Task 2 - ER Modeling

Identify possible entities and relationships among them, their attributes, cardinalities, and participations. If necessary, use features from the Extended ER.

Discuss your design.

##### Description:

A music database is designed to store details of a music collection, including the albums in the collection, the artists who made them, the tracks on the albums, and when each track was last played.

The music database could be used to manage your music collection, for instance, as backend of an app running on your smart phone.

Because this database is for a personal collection, it does not have to be complex. It must store only the relationships between artists, albums, and tracks, thus ignoring other details (e.g., music genres, music label).

Nevertheless, the music database must fulfill the following requirements:

The music collection consists of albums that are made by exactly one artist. An artist can make one or more albums that contains one or more tracks. Artists, albums, and tracks each have a name. Artists can have a nickname (forget PDiddy) and groups count as a single artist. Albums have a publication year. Each track is on exactly one album and has a time length (measured in seconds).

When a track is played, the date and time the playback began (to the nearest second) should be recorded; this is used for reporting when a track was last played, as well as the number of times music by an artist, from an album, or a track has been played.

#### Task 3 - More ER Modeling

The database of Task 2 is simple by design; however, in the real world many of the assumptions made to design it are not valid. Thus, you must extend it with the following features:

- Support for compilations or various-artists albums in which each track may be by a different artist and may have its own associated album-like details (e.g., recording date and time). 

- Album details, such as when and where it was recorded, the producer and label, the band members or sidemen who played on the album (e.g., featuring), and even the album artwork.

- Smarter track management, such as modeling that allows the same track to appear on many albums, and track ratings.
 
- Playlists, a user-controlled collection of tracks. For example, you might create a playlist of your favorite tracks from an artist.

#### References:
The description of the music database is taking from: 
[O'Reilly Learning My SQL](https://www.oreilly.com/library/view/learning-mysql/0596008643/ch04s04.html)

Additional examples of Music related databases can be found on: [Geeks For Geeks](https://www.geeksforgeeks.org/how-to-design-a-database-for-music-streaming-app/)

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
