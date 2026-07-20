SELECT Movies.Title, Movies.Rating, Directors.DirectorName 
FROM Movies 
JOIN Directors ON Movies.DirectorID = Directors.DirectorID 
ORDER BY Movies.Rating DESC 
LIMIT 5;
