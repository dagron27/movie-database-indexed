DROP VIEW IF EXISTS DirectorHighestRatedMovies;

CREATE VIEW DirectorHighestRatedMovies AS
SELECT d.DirectorName, m.Title, m.Rating
FROM Movies m
JOIN Directors d ON m.DirectorID = d.DirectorID
JOIN (
    SELECT DirectorID, MAX(Rating) AS HighestRating
    FROM Movies
    GROUP BY DirectorID
) sub ON m.DirectorID = sub.DirectorID AND m.Rating = sub.HighestRating;
