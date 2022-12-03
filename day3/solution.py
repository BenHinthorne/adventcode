## day 3

# split lines in two (rucksacks)
# find common in each rucksack
# converst score
# sum
import math

class Sack:
    def __init__(self, contents):
        self.contents = contents
        self.c1 = contents[:math.floor((len(contents)/2))]
        self.c2 = contents[math.floor((len(contents)/2)):]
        
    def show(self):
        print(self.c1)
        print(self.c2)
    
    def find(self):
        for c in self.c1:
            if c in self.c2:
                return c
        return ''

class Group:
    def __init__(self, lines):
        sacks = []
        for l in lines:
            sacks.append(Sack(l))
        self.sacks = sacks
    
    def find(self):
        for c in self.sacks[0].contents:
            if c in self.sacks[1].contents and c in self.sacks[2].contents:
                return c
        return ''

## ascii table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
## used for conversions
def score(c):
    if c == str.lower(c):
        return ord(c) - 96
    else:
        return ord(c) - 38

def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines

def solv_puzzle(filename):
    lines = readfile(filename)
    total_1 = 0
    total_2 = 0
    group_lines = []
    for l in lines:
        s = Sack(l)
        total_1 += score(s.find())
        group_lines.append(l)
        if len(group_lines) == 3:
            g = Group(group_lines)
            total_2 += score(g.find())
            group_lines = []
        
    return total_1, total_2


def main():
    print(solv_puzzle("input-test.txt"))
    print(solv_puzzle("input-real.txt"))

if __name__ == "__main__":
    main()
