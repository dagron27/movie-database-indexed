import time

def count_movies_by_year(cursor, year):
    start_time = time.time()
    cursor.execute("SELECT COUNT(*) FROM Movies WHERE ReleaseYear=?", (year,))
    count = cursor.fetchone()[0]
    end_time = time.time()
    execution_time = end_time - start_time
    return count, execution_time

def count_movies_by_year_range(cursor, start_year, end_year):
    start_time = time.time()
    cursor.execute("SELECT COUNT(*) FROM Movies WHERE ReleaseYear BETWEEN ? AND ?", (start_year, end_year))
    count = cursor.fetchone()[0]
    end_time = time.time()
    execution_time = end_time - start_time
    return count, execution_time

def create_index(cursor):
    cursor.execute("CREATE INDEX idx_year ON Movies(ReleaseYear)")

def drop_index(cursor):
    cursor.execute("DROP INDEX IF EXISTS idx_year")