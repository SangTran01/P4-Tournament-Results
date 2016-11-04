#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute('DELETE FROM matches')
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute('DELETE FROM players')
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute('SELECT * FROM players')

    players = 0
    for row in c.fetchall():
        players += 1

    DB.close()
    return players

def registerPlayer(name):
    """Adds a player to the tournament database.
    
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute('INSERT INTO players (name) VALUES (%s)', (name,))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute('SELECT * FROM standings')


    # players list used to hold tuples then return 
    players = []
    for row in c.fetchall():
        players.append(row)


    print players
    DB.commit()
    DB.close()

    return players

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    # inserting id of winner and id of loser into matches tables 
    c.execute('INSERT INTO matches (winner, loser) VALUES (%s, %s)', (winner, loser,))
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()

    # getting player count
    c.execute('SELECT count(*) from players')

    # gettings standings
    standings = playerStandings()

    # use slice to get a player from standings
    player = [item[0:2] for item in standings]


    # need index to more back/forth in loop
    index = 0
    pairings = []


    for row in c.fetchall():

        while (index < row[0]):
            # adding first player to second player creating a pair
            pair = player[index] + player[index+1]

            pairings.append(pair)

            index = index + 2

        print '-------------------'
        print 'PAIRINGS'
        print '-------------------'
        print pairings

        
        print '-------------------'
        print 'STANDINGS'
        print '-------------------'
        # return id, n, wins,matches
        print playerStandings()
        return pairings

    
    DB.close()