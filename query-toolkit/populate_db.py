import sqlite3

try:
    # Connect to the SQLite database
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    # Revised data to be inserted
    movies = [
        (1, "Jaws", 1975, 8.0, "A giant great white shark terrorizes a beach town.", 1),
        (2, "E.T. the Extra-Terrestrial", 1982, 7.8, "A troubled child summons the courage to help a friendly alien escape Earth.", 1),
        (3, "Goodfellas", 1990, 8.7, "The story of Henry Hill and his life in the mob.", 2),
        (4, "Taxi Driver", 1976, 8.3, "A mentally unstable Vietnam War veteran becomes a vigilante.", 2),
        (5, "The Godfather", 1972, 9.2, "The aging patriarch of an organized crime dynasty transfers control to his reluctant son.", 3),
        (6, "Apocalypse Now", 1979, 8.4, "During the Vietnam War, Captain Willard is sent to assassinate a rogue colonel.", 3),
        (7, "Pulp Fiction", 1994, 8.9, "The lives of two mob hitmen intertwine with stories of crime.", 4),
        (8, "Kill Bill: Volume 1", 2003, 8.1, "A former assassin awakens from a coma to seek revenge on her ex-colleagues.", 4),
        (9, "Inception", 2010, 8.8, "A thief who steals corporate secrets using dream-sharing technology.", 5),
        (10, "Dunkirk", 2017, 7.9, "Allied soldiers are surrounded by enemy forces and evacuated during a fierce battle in World War II.", 5),
        (11, "Gladiator", 2000, 8.5, "A former Roman General sets out to exact vengeance against the corrupt emperor.", 6),
        (12, "Alien", 1979, 8.4, "The crew of a commercial spacecraft encounter a deadly alien after investigating an unknown transmission.", 6),
        (13, "Fight Club", 1999, 8.8, "An insomniac office worker and a soap maker form an underground fight club.", 7),
        (14, "Se7en", 1995, 8.6, "Two detectives hunt a serial killer who uses the seven deadly sins as his modus operandi.", 7),  # Add a comma here
        (15, "Spider-Man: No Way Home", 2021, 8.3, "Peter Parker faces new challenges and consequences of being Spider-Man.", 8),  
        (16, "Dune", 2021, 8.2, "A noble family becomes embroiled in a war for control over the galaxy's most valuable asset.", 9), 
        (17, "Unbreakable", 2000, 7.3, "A man discovers he has superhero-like abilities after surviving a train crash.", 10),
        (18, "Once Upon a Time in Hollywood", 2019, 7.6, "An aging actor and his stunt double navigate Hollywood in the late 1960s.", 4),
        (19, "Inglourious Basterds", 2009, 8.3, "A group of Jewish soldiers in Nazi-occupied France plan to assassinate Nazi leaders.", 4),
        (20, "Jurassic Park", 1993, 8.1, "Scientists clone dinosaurs to create a theme park, which goes horribly wrong.", 1),
        (21, "Blade Runner", 1982, 8.1, "In a dystopian future, synthetic humans are hunted down by special police operatives.", 3),
        (22, "Schindler's List", 1993, 9.0, "In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.", 1), 
        (23, "Reservoir Dogs", 1992, 8.3, "After a botched robbery, tensions escalate among criminals as they suspect a mole.", 4), 
        (24, "The Hateful Eight", 2015, 7.8, "In the aftermath of the American Civil War, eight strangers seek refuge during a blizzard.", 4)
    ]

    genres = [
        (1, "Drama"),
        (2, "Crime"),
        (3, "Thriller"),
        (4, "Adventure"),
        (5, "Sci-Fi"),
        (6, "Action"),
        (7, "Horror"),
        (8, "War"),
        (9, "Superhero"),    
        (10, "Epic"),
        (11, "Comedy")          
    ]

    directors = [
        (1, "Steven Spielberg", "1946-12-18"),
        (2, "Martin Scorsese", "1942-11-17"),
        (3, "Francis Ford Coppola", "1939-04-07"),
        (4, "Quentin Tarantino", "1963-03-27"),
        (5, "Christopher Nolan", "1970-07-30"),
        (6, "Ridley Scott", "1937-11-30"),
        (7, "David Fincher", "1962-08-28"),
        (8, "Jon Watts", "1981-10-28"),
        (9, "Denis Villeneuve", "1967-10-03"),
        (10, "M. Night Shyamalan", "1970-08-06")
    ]

    actors = [
        (1, "Robert Shaw", "1927-04-09"),     # Starred in "Jaws"
        (2, "Drew Barrymore", "1975-02-22"),  # Starred in "E.T. the Extra-Terrestrial"
        (3, "Ray Liotta", "1954-12-18"),      # Starred in "Goodfellas"
        (4, "Robert De Niro", "1943-08-17"),  # Starred in "Taxi Driver" and "Goodfellas"
        (5, "Marlon Brando", "1924-04-03"),   # Starred in "The Godfather" and "Apocalypse Now"
        (6, "Martin Sheen", "1940-04-03"),    # Starred in "Apocalypse Now"
        (7, "John Travolta", "1954-02-18"),   # Starred in "Pulp Fiction"
        (8, "Uma Thurman", "1970-04-29"),     # Starred in "Kill Bill: Volume 1" and "Pulp Fiction"
        (9, "Leonardo DiCaprio", "1974-11-11"), # Starred in "Inception"
        (10, "Fionn Whitehead", "1997-01-18"), # Starred in "Dunkirk"
        (11, "Russell Crowe", "1974-04-07"),   # Starred in "Gladiator"
        (12, "Sigourney Weaver", "1949-10-08"), # Starred in "Alien"
        (13, "Edward Norton", "1969-08-18"),   # Starred in "Fight Club"
        (14, "Morgan Freeman", "1937-06-01"),   # Starred in "Se7en"
        (15, "Brad Pitt", "1963-12-18"),         # Starred in "Fight Club" and "Se7en"
        (16, "Samuel L. Jackson", "1948-12-21"), # Starred in "Pulp Fiction" and "Unbreakable"
        (17, "Bruce Willis", "1955-03-19"),       # Starred in "Pulp Fiction" and "Unbreakable"
        (18, "Robert Duvall", "1931-01-05"),       # Starred in "Apocalypse Now"
        (19, "Tom Holland", "1996-06-01"),          # Starred in "Spider-Man: No Way Home"
        (20, "Timothée Chalamet", "1995-12-27"),    # Starred in "Dune"
        (21, "Harrison Ford", "1942-07-13")         # Starred in "Blade Runner"
    ]

    movie_genres = [
        (1, 1, 7),   # Jaws - Horror
        (2, 1, 4),   # Jaws - Adventure
        (3, 2, 4),   # E.T. the Extra-Terrestrial - Adventure
        (4, 2, 5),   # E.T. the Extra-Terrestrial - Sci-Fi
        (5, 3, 2),   # Goodfellas - Crime
        (6, 3, 3),   # Goodfellas - Drama
        (7, 4, 3),   # Taxi Driver - Thriller
        (8, 4, 1),   # Taxi Driver - Drama
        (9, 5, 2),   # The Godfather - Crime
        (10, 5, 1),  # The Godfather - Drama
        (11, 6, 3),  # Apocalypse Now - Thriller
        (12, 6, 8),  # Apocalypse Now - War
        (13, 7, 2),  # Pulp Fiction - Crime
        (14, 7, 3),  # Pulp Fiction - Thriller
        (15, 7, 12), # Pulp Fiction - Comedy
        (16, 8, 6),  # Kill Bill: Volume 1 - Action
        (17, 8, 3),  # Kill Bill: Volume 1 - Thriller
        (18, 9, 5),  # Inception - Sci-Fi
        (19, 9, 3),  # Inception - Thriller
        (20, 10, 8), # Dunkirk - War
        (21, 10, 3), # Dunkirk - Thriller
        (22, 11, 6), # Gladiator - Action
        (23, 11, 1), # Gladiator - Drama
        (24, 12, 7), # Alien - Horror
        (25, 12, 5), # Alien - Sci-Fi
        (26, 13, 3), # Fight Club - Thriller
        (27, 13, 1), # Fight Club - Drama
        (28, 14, 2), # Se7en - Crime
        (29, 14, 3), # Se7en - Thriller
        (30, 15, 6), # Spider-Man: No Way Home - Action
        (31, 15, 4), # Spider-Man: No Way Home - Adventure
        (32, 15, 10),# Spider-Man: No Way Home - Superhero
        (33, 16, 5), # Dune - Sci-Fi
        (34, 16, 4), # Dune - Adventure
        (35, 16, 11),# Dune - Epic
        (36, 17, 1), # Unbreakable - Drama
        (37, 17, 10),# Unbreakable - Superhero
        (38, 18, 1), # Once Upon a Time in Hollywood - Drama
        (39, 18, 4), # Once Upon a Time in Hollywood - Adventure
        (40, 18, 12),# Once Upon a Time in Hollywood - Comedy
        (41, 19, 2), # Inglourious Basterds - War
        (42, 19, 3), # Inglourious Basterds - Drama
        (43, 19, 12),# Inglourious Basterds - Comedy
        (44, 20, 4), # Jurassic Park - Adventure
        (45, 20, 5), # Jurassic Park - Sci-Fi
        (46, 21, 5), # Blade Runner - Sci-Fi
        (47, 21, 3),  # Blade Runner - Thriller
        (48, 23, 2), # Reservoir Dogs - Crime 
        (49, 23, 3) # Reservoir Dogs - Thriller
    ]

    movie_actors = [
        (1, 1, 1),   # "Jaws" with Robert Shaw
        (2, 2, 2),   # "E.T. the Extra-Terrestrial" with Drew Barrymore
        (3, 3, 3),   # "Goodfellas" with Ray Liotta
        (4, 3, 4),   # "Goodfellas" with Robert De Niro
        (5, 4, 4),   # "Taxi Driver" with Robert De Niro
        (6, 5, 5),   # "The Godfather" with Marlon Brando
        (7, 5, 18),  # "The Godfather" with Robert Duvall
        (8, 6, 5),   # "Apocalypse Now" with Marlon Brando
        (9, 6, 6),   # "Apocalypse Now" with Martin Sheen
        (10, 6, 18), # "Apocalypse Now" with Robert Duvall
        (11, 7, 7),  # "Pulp Fiction" with John Travolta
        (12, 7, 8),  # "Pulp Fiction" with Uma Thurman
        (13, 7, 16), # "Pulp Fiction" with Samuel L. Jackson
        (14, 7, 17), # "Pulp Fiction" with Bruce Willis
        (15, 8, 8),  # "Kill Bill: Volume 1" with Uma Thurman
        (16, 9, 9),  # "Inception" with Leonardo DiCaprio
        (17, 10, 10),# "Dunkirk" with Fionn Whitehead
        (18, 11, 11),# "Gladiator" with Russell Crowe
        (19, 12, 12),# "Alien" with Sigourney Weaver
        (20, 13, 13),# "Fight Club" with Edward Norton
        (21, 13, 15),# "Fight Club" with Brad Pitt
        (22, 14, 15),# "Se7en" with Brad Pitt
        (23, 14, 14),# "Se7en" with Morgan Freeman
        (24, 15, 19),# "Spider-Man: No Way Home" with Tom Holland
        (25, 16, 20),# "Dune" with Timothée Chalamet
        (26, 17, 17),# "Unbreakable" with Bruce Willis
        (27, 17, 16),# "Unbreakable" with Samuel L. Jackson
        (28, 18, 9), # "Once Upon a Time in Hollywood" with Leonardo DiCaprio
        (29, 18, 15),# "Once Upon a Time in Hollywood" with Brad Pitt
        (30, 19, 15),# "Inglourious Basterds" with Brad Pitt
        (31, 20, 16),# "Jurassic Park" with Samuel L. Jackson
        (32, 21, 21), # "Blade Runner" with Harrison Ford
        (33, 24, 16) # "The Hateful Eight" with Samuel L. Jackson
    ]

    # Insert data into tables using INSERT
    cursor.executemany("INSERT INTO Movies VALUES (?, ?, ?, ?, ?, ?)", movies)
    cursor.executemany("INSERT INTO Genres VALUES (?, ?)", genres)
    cursor.executemany("INSERT INTO Directors VALUES (?, ?, ?)", directors)
    cursor.executemany("INSERT INTO Actors VALUES (?, ?, ?)", actors)
    cursor.executemany("INSERT INTO MovieGenres VALUES (?, ?, ?)", movie_genres)
    cursor.executemany("INSERT INTO MovieActors VALUES (?, ?, ?)", movie_actors)

    # Commit changes and close the connection
    connection.commit() 
    print("Data has been inserted successfully.") 
except sqlite3.Error as error: 
    print("Failed to insert data into sqlite table", error) 
finally: 
    if connection: 
        connection.close()