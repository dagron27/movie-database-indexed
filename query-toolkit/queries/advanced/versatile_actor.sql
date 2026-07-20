SELECT Actors.ActorName, COUNT(DISTINCT Genres.GenreID) AS GenreCount
FROM Actors
JOIN MovieActors ON Actors.ActorID = MovieActors.ActorID
JOIN Movies ON MovieActors.MovieID = Movies.MovieID
JOIN MovieGenres ON Movies.MovieID = MovieGenres.MovieID
JOIN Genres ON MovieGenres.GenreID = Genres.GenreID
GROUP BY Actors.ActorName
ORDER BY GenreCount DESC
LIMIT 3;
