SELECT g.genre_name, count(mg.musicianid) FROM genre g
	JOIN musician_genre mg ON g.genreid = mg.genreid
	GROUP BY g.genre_name;


SELECT a.title, a.release_year, count(mt.trackid) FROM album a
	JOIN music_track mt ON a.albumid = mt.albumid
	WHERE a.release_year BETWEEN 2019 AND 2020
	GROUP BY a.title, a.release_year;


SELECT a.title, avg(mt.duratiON) FROM album a
	JOIN music_track mt ON a.albumid = mt.albumid
	GROUP BY a.title;


SELECT m.stage_name FROM musician m
	JOIN musician_album ma ON m.musicianid = ma.musicianid
	JOIN album a ON a.albumid = ma.albumid
	WHERE a.release_year != 2020;


SELECT c.title FROM collectiON c
	JOIN collectiON_track ct ON c.collectiONid = ct.collectiONid
	JOIN music_track mt ON mt.trackid = ct.trackid
	JOIN album a ON a.albumid = mt.albumid
	JOIN musician_album ma ON ma.albumid = a.albumid
	JOIN musician m ON m.musicianid = ma.musicianid
	WHERE m.stage_name LIKE '%%Crowded%%';
