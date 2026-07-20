SELECT Genres.GenreName, AVG(Movies.Rating) AS AverageRating 
FROM Movies 
JOIN MovieGenres ON Movies.MovieID = MovieGenres.MovieID 
JOIN Genres ON MovieGenres.GenreID = Genres.GenreID 
GROUP BY Genres.GenreName;
