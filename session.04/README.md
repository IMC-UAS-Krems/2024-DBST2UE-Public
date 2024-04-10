## Session 4 - 03/04/2024

#### Task 1 - Setup Fixtures and write tests

Complete the tasks 2 and 3 from the past session (see [../session.03/README.md](../session.03/README.md)).

An example of tests and pytest conftest.py files defining some fixtures can be found [here](.)

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