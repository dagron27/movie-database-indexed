SELECT Directors.DirectorName, COUNT(Movies.MovieID) AS MovieCount 
FROM Movies 
JOIN Directors ON Movies.DirectorID = Directors.DirectorID 
GROUP BY Directors.DirectorName 
HAVING MovieCount >= 3;
