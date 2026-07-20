from random_data import genres, generate_genre, generate_person, generate_movie

ALLOWED_TABLES = {"Genres", "Directors", "Actors", "Movies", "MovieGenres", "MovieActors"}

def get_table_length(cursor, table_name):
    if table_name not in ALLOWED_TABLES:
        raise ValueError(f"Unknown table name: {table_name!r}")
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

def add_genre(cursor):
    added_genres = set()
    cursor.execute("SELECT GenreName FROM Genres")
    existing_genres = {row[0] for row in cursor.fetchall()}
    new_genre = None
    
    if len(existing_genres) >= len(genres):
        new_genre = "No more unique genres available"
    else:
        while True:
            genre = generate_genre()[1]
            if genre not in existing_genres and genre not in added_genres:
                cursor.execute("INSERT INTO Genres (GenreName) VALUES (?)", (genre,))
                added_genres.add(genre)
                existing_genres.add(genre)
                new_genre = genre
                break

    cursor.connection.commit()
    return new_genre

# Function to add directors to the database
def add_director(cursor):
    person = generate_person()
    cursor.execute("INSERT INTO Directors (DirectorName, BirthDate) VALUES (?, ?)", 
                   (person["name"], person["birthday"]))
    cursor.connection.commit()
    director_info = f"{person['name']}, {person['birthday']}"
    return director_info

# Function to add actors to the database
def add_actor(cursor):
    person = generate_person()
    cursor.execute("INSERT INTO Actors (ActorName, BirthDate) VALUES (?, ?)", 
                   (person["name"], person["birthday"]))
    cursor.connection.commit()
    actor_info = f"{person['name']}, {person['birthday']}"
    return actor_info

# Function to add movies to the database, update MovieGenres, and add actors to MovieActors
def add_movie(cursor, genre_id, director_id):
    movie = generate_movie(genre_id, director_id)
    title, year, rating, description, director_id = movie
    
    # Insert into Movies table
    cursor.execute("INSERT INTO Movies (Title, ReleaseYear, Rating, Description, DirectorID) VALUES (?, ?, ?, ?, ?)", 
                   (title, year, rating, description, director_id))
    
    # Get the last inserted MovieID
    movie_id = cursor.lastrowid
    return movie_id

def add_movie_genre(cursor, movie_id, genre_id):
    cursor.execute("INSERT INTO MovieGenres (MovieID, GenreID) VALUES (?, ?)", (movie_id, genre_id))

def add_movie_actor(cursor, movie_id, actor_id):
    cursor.execute("INSERT INTO MovieActors (MovieID, ActorID) VALUES (?, ?)", (movie_id, actor_id))