SELECT name, duration
	FROM music_track
	ORDER BY duration DESC
	LIMIT 1;


SELECT name, duration
	FROM music_track
	WHERE duration >= 210
	ORDER BY duration DESC;


SELECT title, release_year
	FROM collection
	WHERE release_year BETWEEN 2018 AND 2020
	ORDER BY release_year DESC;


SELECT stage_name
	FROM musician
	WHERE stage_name NOT LIKE '%% %%';


SELECT name
	FROM music_track
	WHERE name LIKE '%%My%%';
