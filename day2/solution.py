## day 2 

points_map = {
    "AX": 4, # Draw + Rock
    "BX": 1, # Loss + Rock
    "CX": 7, # Win + Rock
    "AY": 8, # Win + Paper
    "BY": 5, # Draw+ Paper
    "CY": 2, # Loss + Papaer
    "AZ": 3, # Loss + Scissors
    "BZ": 9, # Win + Scissors
    "CZ": 6, # Draw + Scissors
}

points_map_fixed = {
    "AX": 3, # Loss + Scissors (3)
    "BX": 1, # Loss + Rock (1)
    "CX": 2, # Loss + Paper (2)
    "AY": 4, # Draw + Rock (1)
    "BY": 5, # Draw + Paper (2)
    "CY": 6, # Draw + Scissors (3)
    "AZ": 8, # Win + Paper (2)
    "BZ": 9, # Win + Scissors (3)
    "CZ": 7, # Win + Rock (1)
}

# Represents a single game of RPS
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        return points_map[self.player1 + self.player2]
    
    def fix(self):
        return points_map_fixed[self.player1 + self.player2]

# Represents a set of games of RPS
class Strategy:
    def __init__(self, games):
        self.games = games

    def score(self):
        score = 0
        for g in self.games:
            score += g.play()
        return score
    
    def fix(self):
        score = 0
        for g in self.games:
            score += g.fix()
        return score
    

def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines

def solv_puzzle(filename):
    games = []
    for l in readfile(filename):
        #lines in form of A B
        players = l.split(" ")
        games.append(Game(players[0], players[1]))
    strat = Strategy(games)
    return strat.score(), strat.fix()

def main():
    print(solv_puzzle("input-test.txt"))
    print(solv_puzzle("input-real.txt"))


if __name__ == "__main__":
    main()
