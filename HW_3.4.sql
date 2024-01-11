SELECT a.title FROM album a
	JOIN musician_album ma ON a.albumid = ma.albumid
	JOIN musician m ON m.musicianid = ma.musicianid
	JOIN musician_genre mg ON mg.musicianid = m.musicianid
	JOIN genre g ON g.genreid = mg.genreid
	GROUP BY m.stage_name, a.title
	HAVING count(mg.genreid) > 1;


SELECT mt.name FROM music_track mt
	LEFT JOIN collectiON_track ct ON mt.trackid = ct.trackid
	WHERE ct.trackid IS NULL;


SELECT m.stage_name FROM musician m
	JOIN musician_album ma ON m.musicianid = ma.albumid
	JOIN album a ON a.albumid = ma.albumid
	JOIN music_track mt ON mt.albumid = a.albumid
	WHERE duratiON = (SELECT mIN(duratiON) FROM music_track);


SELECT a.title, count(mt.trackid) FROM album a
	JOIN music_track mt ON a.albumid = mt.albumid
	GROUP BY a.title
	HAVING count(mt.trackid) IN (
		SELECT count(mt.trackid) FROM album a
		JOIN music_track mt ON a.albumid = mt.albumid
		GROUP BY a.title
		order BY count(mt.trackid)
		limit 1);
