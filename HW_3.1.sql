INSERT INTO genre(genre_name)
	VALUES ('classical'), ('popular'), ('rock'), ('metal'), ('disco');


INSERT INTO musician(stage_name)
	VALUES ('Brooch'), ('Deposition'), ('Crowded'), ('Dob'), ('Firm'), ('Catastrophe'), ('Aerobatics'), ('Amateur'), ('Risky game'), ('Fleming');


INSERT INTO musician_genre(musicianid, genreid)
	VALUES (1,1), (2,1), (3,2), (4,3), (5,4), (6,4), (7,4), (8,5), (9,5), (10,5);


INSERT INTO album(title, release_year)
	VALUES ('Barrage', 1975), ('Facile', 2020), ('Capricious', 1980), ('Atomaniac', 2019), ('Balanced', 2001), ('Aggressor', 2020), ('Body-guard', 1986), ('Climber', 1998), ('Dryasdust', 2016), ('Duckweed', 2021);


INSERT INTO musician_album(musicianid, albumid)
	VALUES (1,2), (2,5), (3,6), (4,3), (5,10), (6,9), (7,8), (8,3), (9,7), (10,4);

INSERT INTO music_track(name, duration, albumid)
	VALUES ('Collection', 302, 6), ('Detriment', 282, 10), ('Coupled', 428, 9), ('Anecdotic', 419, 1), ('Cave-dweller', 323, 7), ('Foolhardy', 489, 4), ('Armour', 139, 8), ('Degeneration', 414, 8), ('Caricature', 187, 8), ('Fatal', 458, 10), ('Exertion', 348, 5), ('My amulet', 475, 6), ('Chorale', 436, 3), ('Dabbler', 496, 2), ('Ballyhoo', 406, 7);


INSERT INTO collection(title, release_year)
	VALUES ('Brutality', 1995), ('Credulous', 1999), ('Bomb-proof', 1988), ('Frontier', 1975), ('Frenzy', 2021), ('Codger', 1998), ('Clack', 2006), ('Climber', 2008), ('Foolhardiness', 2019), ('Elfin', 2021);


INSERT INTO collection_track(collectionid, trackid)
	VALUES (2,1), (8,2), (7,3), (1,4), (1,5), (10,6), (5,7), (6,8), (3,9), (1,10), (9,11), (8,12), (3,13), (4,14), (3,15);


INSERT INTO musician_genre(musicianid, genreid)
	VALUES (5,1), (10,3);


INSERT INTO music_track(name, duration, albumid)
	VALUES ('Valley', 352, 3), ('The sun', 434, 5);


INSERT INTO album(title, release_year)
	VALUES ('Bear', 2003);

