SELECT DISTINCT Actors.ActorName 
FROM Actors 
JOIN MovieActors ON Actors.ActorID = MovieActors.ActorID 
JOIN Movies ON MovieActors.MovieID = Movies.MovieID 
JOIN MovieGenres ON Movies.MovieID = MovieGenres.MovieID 
JOIN Genres ON MovieGenres.GenreID = Genres.GenreID 
WHERE Genres.GenreName = 'Action';
