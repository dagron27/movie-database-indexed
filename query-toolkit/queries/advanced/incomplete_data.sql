SELECT 
    Movies.Title, 
    CASE WHEN MovieActors.ActorID IS NULL THEN 'Missing Actor' ELSE 'Has Actor' END AS ActorStatus,
    CASE WHEN MovieGenres.GenreID IS NULL THEN 'Missing Genre' ELSE 'Has Genre' END AS GenreStatus
FROM Movies
LEFT JOIN MovieActors ON Movies.MovieID = MovieActors.MovieID
LEFT JOIN MovieGenres ON Movies.MovieID = MovieGenres.MovieID
WHERE MovieActors.ActorID IS NULL OR MovieGenres.GenreID IS NULL;
