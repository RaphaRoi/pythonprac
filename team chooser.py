#!/bin/python3
from random import choice
from random import randint



players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)

chosenTeamName = randint

teamA = []
teamB = []

while len(players) > 0:
  playerA = (choice(players))
  print('Pick for team A:', playerA)
  teamA.append(playerA)
  players.remove(playerA)
  print('Players left:', players)
  
  if players == []:
    break
  
  playerB = (choice(players))
  print('Pick for team B:', playerB)
  teamB.append(playerB)
  players.remove(playerB)
  print('players left:', players)

print(' ')
print('Here are your teams:')
print(' ')

print(teamNames[randint(1, 6)], teamA)
print(teamNames[randint(1, 6)], teamB)

