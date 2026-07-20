SELECT Movies.Title, COUNT(MovieActors.ActorID) AS ActorCount 
FROM Movies 
JOIN MovieActors ON Movies.MovieID = MovieActors.MovieID 
GROUP BY Movies.Title 
HAVING ActorCount >= 3;
