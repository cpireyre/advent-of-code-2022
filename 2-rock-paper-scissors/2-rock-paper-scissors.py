# Part I

# val = {}
# val['X'] = 1
# val['Y'] = 2
# val['Z'] = 3

# A = X = Rock, B = Y = Paper, C = Z = Scissors

# match = {}

# match[('A', 'X')] = DRAW
# match[('A', 'Y')] = WIN
# match[('A', 'Z')] = LOSE
               
# match[('B', 'X')] = LOSE
# match[('B', 'Y')] = DRAW
# match[('B', 'Z')] = WIN
               
# match[('C', 'X')] = WIN
# match[('C', 'Y')] = LOSE
# match[('C', 'Z')] = DRAW

# Part II
match = {}

ROCK, PAPER, SCISSOR = 1, 2, 3
LOSE, DRAW, WIN = 0, 3, 6

match[('A', 'X')] = SCISSOR + LOSE
match[('A', 'Y')] = ROCK + DRAW
match[('A', 'Z')] = PAPER + WIN
               
match[('B', 'X')] = ROCK + LOSE
match[('B', 'Y')] = PAPER + DRAW
match[('B', 'Z')] = SCISSOR + WIN
               
match[('C', 'X')] = PAPER + LOSE
match[('C', 'Y')] = SCISSOR + DRAW
match[('C', 'Z')] = ROCK + WIN

def score(left, right):
    return match[left, right]

def parse(line):
    return (line[0], line[2])

def tournament(input):
    with open(input, 'r') as games:
        total = sum(score(g[0], g[1]) for g in map(parse,games))
    return total

print(tournament("2-input.txt")) # 16862
