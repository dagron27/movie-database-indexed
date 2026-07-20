-- SQLite

DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies (
    MovieID INTEGER PRIMARY KEY,                -- Unique identifier for each movie
    Title TEXT NOT NULL,                        -- Title of the movie
    ReleaseYear INTEGER,                        -- Year the movie was released
    Rating REAL,                                -- Rating of the movie (e.g., 7.5)
    Description TEXT,                           -- Brief description of the movie
    DirectorID INTEGER,                         -- Foreign key referencing Directors
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID)
);

DROP TABLE IF EXISTS Genres;
CREATE TABLE Genres (
    GenreID INTEGER PRIMARY KEY,                -- Unique identifier for each genre
    GenreName TEXT NOT NULL UNIQUE              -- Name of the genre (e.g., Action, Comedy)
);

DROP TABLE IF EXISTS Directors;
CREATE TABLE Directors (
    DirectorID INTEGER PRIMARY KEY,             -- Unique identifier for each director
    DirectorName TEXT NOT NULL,                 -- Name of the director
    BirthDate TEXT                              -- Birthdate of the director in YYYY-MM-DD format
);

DROP TABLE IF EXISTS Actors;
CREATE TABLE Actors (
    ActorID INTEGER PRIMARY KEY,                -- Unique identifier for each actor
    ActorName TEXT NOT NULL,                    -- Name of the actor
    BirthDate TEXT                              -- Birthdate of the actor in YYYY-MM-DD format
);

DROP TABLE IF EXISTS MovieGenres;
CREATE TABLE MovieGenres (
    MovieGenreID INTEGER PRIMARY KEY,           -- Unique identifier for each movie-genre pair
    MovieID INTEGER NOT NULL,                   -- Foreign key referencing Movies
    GenreID INTEGER NOT NULL,                   -- Foreign key referencing Genres
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

DROP TABLE IF EXISTS MovieActors;
CREATE TABLE MovieActors (
    MovieActorID INTEGER PRIMARY KEY,           -- Unique identifier for each movie-actor pair
    MovieID INTEGER NOT NULL,                   -- Foreign key referencing Movies
    ActorID INTEGER NOT NULL,                   -- Foreign key referencing Actors
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
);
