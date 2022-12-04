LOSE, DRAW, WIN = 0, 3, 6

val = {}
val['X'] = 1
val['Y'] = 2
val['Z'] = 3

# A = X = Rock, B = Y = Paper, C = Z = Scissors

match = {}

match[('A', 'X')] = DRAW
match[('A', 'Y')] = WIN
match[('A', 'Z')] = LOSE
               
match[('B', 'X')] = LOSE
match[('B', 'Y')] = DRAW
match[('B', 'Z')] = WIN
               
match[('C', 'X')] = WIN
match[('C', 'Y')] = LOSE
match[('C', 'Z')] = DRAW

def score(left, right):
    return match[left, right] + val[right]

def parse(line):
    return (line[0], line[2])

def tournament(input):
    with open(input, 'r') as games:
        total = sum(score(g[0], g[1]) for g in map(parse,games))
    return total

print(tournament("2-input.txt"))
