from flask import Flask, request, render_template
import sqlite3
import random
from db_utils import add_genre, add_director, add_actor, add_movie, add_movie_genre, add_movie_actor, get_table_length
from search_movies import count_movies_by_year, count_movies_by_year_range, create_index, drop_index    

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_genre', methods=['POST'])
def add_genre_route():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    new_genre = None
    try:
        # Add one unique genre
        new_genre = add_genre(cursor)
        connection.commit()
        if new_genre == "No more unique genres available":
            add_genre_message = "All possible genres have already been added."
        else:
            add_genre_message = f"Successfully added genre: {new_genre}"
    except Exception as e:
        add_genre_message = f"An error occurred while adding genre: {e}"
    finally:
        connection.close()
    return render_template('index.html', add_genre_message=add_genre_message, genre=new_genre)

@app.route('/add_director', methods=['POST'])
def add_director_route():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    new_director = None
    try:
        # Check the current number of directors
        cursor.execute("SELECT COUNT(*) FROM Directors")
        count = cursor.fetchone()[0]

        if count >= 25:
            add_director_message = "Cannot add more directors. The limit of 25 directors has been reached."
        else:
            new_director = add_director(cursor)
            add_director_message = f"Successfully added director: {new_director}"
    except Exception as e:
        add_director_message = f"An error occurred while adding director: {e}"
    finally:
        connection.close()
        print(add_director_message)
    return render_template('index.html', add_director_message=add_director_message, director=new_director)

@app.route('/add_actor', methods=['POST'])
def add_actor_route():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    new_actor = None
    try:
        # Check the current number of actors
        cursor.execute("SELECT COUNT(*) FROM Actors")
        count = cursor.fetchone()[0]

        if count >= 50:  # Assuming we want to limit to 50 actors for example
            add_actor_message = "Cannot add more actors. The limit of 50 actors has been reached."
        else:
            new_actor = add_actor(cursor)
            add_actor_message = f"Successfully added actor: {new_actor}"
    except Exception as e:
        add_actor_message = f"An error occurred while adding actor: {e}"
    finally:
        connection.close()
        print(add_actor_message)
    return render_template('index.html', add_actor_message=add_actor_message, actor=new_actor)

@app.route('/add_movies', methods=['POST'])
def add_movie_route():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    MAX_MOVIES_PER_REQUEST = 1000
    try:
        # Get form data
        number_of_movies = int(request.form['num_movies'])

        if number_of_movies < 0:
            raise ValueError("Number of movies cannot be negative.")
        if number_of_movies > MAX_MOVIES_PER_REQUEST:
            number_of_movies = MAX_MOVIES_PER_REQUEST

        len_genres = get_table_length(cursor, "Genres")
        len_directors = get_table_length(cursor, "Directors")
        len_actors = get_table_length(cursor, "Actors")
        
        if len_genres == 0:
            add_movie_message = "Please add genres before adding movies."
        elif len_directors == 0:
            add_movie_message = "Please add directors before adding movies."
        elif len_actors == 0:
            add_movie_message = "Please add actors before adding movies."
        else:
            # Loop for number_of_movies
            for _ in range(number_of_movies):
                cursor.execute("SELECT GenreID FROM Genres")
                genres = cursor.fetchall()
                genre_id = random.choice(genres)[0]

                cursor.execute("SELECT DirectorID FROM Directors")
                directors = cursor.fetchall()
                director_id = random.choice(directors)[0]

                cursor.execute("SELECT ActorID FROM Actors")
                actors = cursor.fetchall()
                actor_id = random.choice(actors)[0]

                movie_id = add_movie(cursor, genre_id, director_id)
                add_movie_genre(cursor, movie_id, genre_id)
                add_movie_actor(cursor, movie_id, actor_id)
            
            connection.commit()
            add_movie_message = f"Successfully added {number_of_movies} movie(s)!"
    except Exception as e:
        add_movie_message = f"An error occurred while adding movies: {str(e)}"
        print(f"Error in add_movie_route: {str(e)}")
    finally:
        connection.close()
    return render_template('index.html', add_movie_message=add_movie_message)

@app.route('/search_by_year', methods=['POST'])
def search_by_year():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    try:
        year = int(request.form['year'])
        count, exec_time = count_movies_by_year(cursor, year)
        search_year_message = (f"Number of movies found: {count}\n"
                               f"Execution time before indexing: {exec_time:.3f} seconds.")
    except ValueError:
        count = 0
        exec_time = 0
        search_year_message = "Please enter a valid whole number for the year."
    except Exception as e:
        count = 0
        exec_time = 0
        search_year_message = f"An error occurred while searching by year: {e}"
    finally:
        connection.close()
    return render_template('index.html', search_year_message=search_year_message)

@app.route('/search_by_year_range', methods=['POST'])
def search_by_year_range():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    try:
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])

        # Measure execution time with the index
        count, exec_time = count_movies_by_year_range(cursor, start_year, end_year)

        # Prepare the message
        search_year_range_message = (f"Number of movies found from {start_year} to {end_year}: {count}\n"
                                     f"Execution time with indexing: {exec_time:.3f} seconds.")
    except ValueError:
        count = 0
        exec_time = 0
        search_year_range_message = "Please enter valid whole numbers for the start and end years."
    except Exception as e:
        count = 0
        exec_time = 0
        search_year_range_message = f"An error occurred while searching by year range: {e}"
    finally:
        connection.close()
    return render_template('index.html', search_year_range_message=search_year_range_message)

@app.route('/add_index', methods=['POST'])
def add_index_route():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    try:
        create_index(cursor)
        connection.commit()
        add_index_message = "Index created successfully!"
    except Exception as e:
        add_index_message = f"An error occurred while creating the index: {e}"
    finally:
        connection.close()
    return render_template('index.html', index_message=add_index_message)

@app.route('/drop_index', methods=['POST'])
def drop_index_route():
    connection = sqlite3.connect('data/new_movies.db')
    cursor = connection.cursor()
    try:
        drop_index(cursor)
        connection.commit()
        drop_index_message = "Index dropped successfully!"
    except Exception as e:
        drop_index_message = f"An error occurred while dropping the index: {e}"
    finally:
        connection.close()
    return render_template('index.html', index_message=drop_index_message)

if __name__ == '__main__':
    app.run(debug=False)