Poker
=====

A Texas Hold'Em poker game in Python

Poker.py is the game engine and deck/player generator.  Handles side pots (this took me about a month to work out) just about..

imported modules:

Pokerhands.py is a hand evaluator and scoring tool, takes a value (1-13) of individual cards in a player's hand and returns a score, including facility for tie-breaks/split pots

Pokerstrat.py is a module that allocates player strategies; currently has one AI that plays at random, a Human (needs keyboard input), and one other (see below)

Working on implementing an algorithm for David Sklansky's tournament all-in/fold strategy

Any suggestions on making my sprawling code sleeker welcome

cheers
philip
