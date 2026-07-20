import sqlite3
import os
from db_utils import generate_movies

def execute_sql_script(cursor, script_name):
    script_path = os.path.join('queries', script_name)
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script {script_name} does not exist.")
    with open(script_path, 'r') as file:
        sql_script = file.read()
    cursor.execute(sql_script)
    return cursor.fetchall()

def main():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    scripts = [
        'retrieve_movie_titles.sql',
        'movies_after_2010.sql',
        'top_5_highest_rated_movies.sql',
        'directors_with_at_least_3_movies.sql',
        'average_rating_per_genre.sql',
        'actors_in_genre.sql',
        'movies_with_at_least_3_actors.sql'
    ]

    # Generate random movies
    num_movies = int(input("Enter the number of movies to generate: "))
    generate_movies(cursor, num_movies)

    with connection:
        for script in scripts:
            try:
                print(f"Executing script: {script}")
                results = execute_sql_script(cursor, script)
                for row in results:
                    print(row)
                print("\n")
            except Exception as e:
                print(f"An error occurred while executing script {script}: {e}")

    # Close connection
    connection.close()

if __name__ == "__main__":
    main()
