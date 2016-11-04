-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- CREATE NEW DATABASE
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


-- PLAYERS TABLE
CREATE TABLE players (
 	id SERIAL primary key, 
 	name TEXT);

 -- MATCHES TABLE
CREATE TABLE matches (
 	id serial primary key, 
 	winner int references players (id), 
 	loser int references players (id));



 -- Standings VIEW
 -- joining of players and matches table
 -- returns (ID,Name,# of wins, # of matches played)

CREATE VIEW standings as SELECT players.id, players.name, (SELECT count(matches.winner) 
	FROM matches WHERE players.id = matches.winner) AS wins, (SELECT count(matches.id) 
	FROM matches WHERE players.id = matches.winner OR players.id = matches.loser) AS matches
	FROM players ORDER BY wins DESC, matches DESC;

